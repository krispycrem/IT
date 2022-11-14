# coding: utf-8
import json
import logging
import re
from typing import Dict, List, Optional, Any  # noqa: F401
import uuid

import psycopg2._range
from sh import pg_dump, psql

import starlette
from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status, HTTPException, UploadFile,
)
from psycopg2._range import NumericRange
from sqlalchemy.orm import Session
from starlette.responses import FileResponse, StreamingResponse

from src.openapi_server.apis.utils import get_meta_db, hateoas_links, \
    populate_cols_with_type, get_name, get_type, is_color, are_rows_equal, find_ids_of_duplicates
from src.openapi_server.database.crud.database import save_database_metadata
from src.openapi_server.database.crud.table import save_table_metadata, delete_table_metadata, \
    fetch_all_tables_for_database
from src.openapi_server.database.crud.table_columns import get_columns
from src.openapi_server.database.utils import get_db_connection
from src.openapi_server.models.column_type import ColumnType
from src.openapi_server.models.database_create_post201_response import DatabaseCreatePost201Response
from src.openapi_server.models.database_create_post_request import DatabaseCreatePostRequest
from src.openapi_server.models.edit_value_location import EditValueLocation
from src.openapi_server.models.table_schema import TableSchema

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/database/create",
    responses={
        201: {"model": DatabaseCreatePost201Response, "description": "Database has been created"},
        400: {"description": "An error occured during database creation."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def create_database(
    response: Response,
    database_create_post_request: DatabaseCreatePostRequest = Body(None, description=""),
    meta_database: Session = Depends(get_meta_db),
) -> DatabaseCreatePost201Response:
    """Create an empty database"""
    database_name = database_create_post_request.database_name
    pattern = re.compile("[a-zA-Z]")
    if not pattern.match(database_name):
        raise HTTPException(status_code=400, detail="Bad request!")
    connection, cursor = get_db_connection()
    try:
        cursor.execute(f"CREATE DATABASE {database_name};")
        logger.info(f"Created database {database_name}")
        save_database_metadata(database_name=database_name, session=meta_database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        connection.close()

    response.status_code = 201
    response_data = DatabaseCreatePost201Response(
        database_name=database_create_post_request.database_name,
        links=hateoas_links(database=database_name)
    )
    return response_data


@router.post(
    "/database/{databaseId}/table/create",
    responses={
        201: {"model": TableSchema, "description": "Table created!"},
        400: {"description": "Such a table can&#39;t be created."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def create_table(
    response: Response,
    databaseId: str = Path(None, description="Database Name"),
    table_schema: TableSchema = Body(None, description=""),
    meta_database: Session = Depends(get_meta_db),
) -> TableSchema:
    """Create a new table"""
    connection, cursor = get_db_connection(database=databaseId)
    columns_string = ""
    datatypes_mapping = {
        ColumnType.STRING: "VARCHAR",
        ColumnType.REAL: "NUMERIC",
        ColumnType.CHAR: "VARCHAR(1)",
        ColumnType.INTEGER: "INTEGER",
        ColumnType.COLOR_INTERVAL: "int4range",
        ColumnType.COLOR: "VARCHAR"
    }
    try:
        columns_string += f"id SERIAL CONSTRAINT {table_schema.table_name}PK PRIMARY KEY,"
        for column, column_type in table_schema.columns.items():
            columns_string += f"{column} {datatypes_mapping[column_type]},"
    except Exception as e:
        raise HTTPException(status_code=400, detail="Bad column type!")
    columns_string = columns_string[:-1]
    try:
        save_table_metadata(
            database=databaseId,
            table_schema=table_schema,
            session=meta_database
        )
        cursor.execute(f"CREATE TABLE {table_schema.table_name} ("
                       f" {columns_string} "
                       f");")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Table creation failed: {str(e)}")
    finally:
        connection.close()
    response.status_code = 201
    table_schema.links = hateoas_links(database=databaseId, table=table_schema.table_name)
    return table_schema


@router.delete(
    "/database/{databaseId}/table/{tableId}",
    responses={
        200: {"description": "Deletion succesful"},
        400: {"description": "An error occured during deletion."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def drop_database_table(
        response: Response,
        databaseId: str = Path(None, description="Database name"),
        tableId: str = Path(None, description="Table name"),
        meta_database: Session = Depends(get_meta_db),
) -> dict:
    """Drop table from database"""
    connection, cursor = get_db_connection(database=databaseId)
    try:
        cursor.execute(f"DROP TABLE {tableId};")
        delete_table_metadata(database=databaseId, table=tableId, session=meta_database)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        connection.close()
    response.status_code = 200
    return hateoas_links(database=databaseId)

@router.post(
    "/database/{databaseId}/table/{table_id}/add_row",
    responses={
        201: {"description": "Row added successful"},
        400: {"description": "An error occurred during adding a new row."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
def add_row(
    response: Response,
    row_data: str = Form(default=None),
    databaseId: str = Path(None, description="Database Name"),
    table_id: str = Path(None, description="Table Name"),
    meta_db_connection: Session = Depends(get_meta_db),
) -> dict:
    """Add a row to a table"""
    non_file_columns = json.loads(row_data)
    request_columns = populate_cols_with_type(non_file_columns)

    actual_columns = get_columns(
            database_name=databaseId,
            table_name=table_id,
            session=meta_db_connection,
    )

    if not actual_columns:
        raise HTTPException(status_code=400, detail="Bad request!")

    for actual_column in actual_columns:
        if request_columns[get_name(actual_column)]["type"] != get_type(actual_column):
            raise HTTPException(status_code=400, detail="Bad request!")

    connection, cursor = get_db_connection(database=databaseId)
    try:
        column_string = ""
        value_string = ""
        data_vector = []
        for request_column, column_info in request_columns.items():
            column_string += f"{request_column},"
            if column_info['type'] == ColumnType.COLOR_INTERVAL:
                column_info['value'] = NumericRange(
                    lower=int(column_info['value']['low'], 16),
                    upper=int(column_info['value']['high'], 16),
                    bounds="[]",
                )
            elif column_info['type'] == ColumnType.COLOR:
                column_info['value'] = "_" + column_info['value']
            value_string += "%s,"
            data_vector.append(column_info['value'])
        column_string = column_string[:-1]
        value_string = value_string[:-1]

        cursor.execute(f"INSERT INTO {table_id} ( {column_string} ) VALUES ( {value_string} );", tuple(data_vector))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        connection.close()
    response.status_code = 201
    return hateoas_links(database=databaseId, table=table_id)


@router.patch(
    "/database/{databaseId}/table/{tableId}/edit_value",
    responses={
        201: {"description": "Update successful."},
        400: {"description": "Bad request."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def edit_table_value(
    response: Response,
    databaseId: str = Path(None, description="Database Name"),
    tableId: str = Path(None, description="Table Name"),
    edit_value_location: EditValueLocation = Body(None, description=""),
    meta_db_connection: Session = Depends(get_meta_db),
) -> dict:
    """Update value for specified column name and row ID."""
    column = get_columns(
        database_name=databaseId,
        table_name=tableId,
        session=meta_db_connection,
        column_name=edit_value_location.column_name
    )

    edit_value_dict = {
        edit_value_location.column_name: edit_value_location.value
    }
    typed_edit_value_dict = populate_cols_with_type(edit_value_dict)

    if not column or typed_edit_value_dict[edit_value_location.column_name]["type"] != get_type(column):
        raise HTTPException(status_code=400, detail="Bad request!")

    try:
        connection, cursor = get_db_connection(database=databaseId)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to connect to the database")

    if typed_edit_value_dict[edit_value_location.column_name]["type"] == ColumnType.COLOR_INTERVAL:
        edit_value_location.value = NumericRange(
            lower=int(edit_value_location.value["low"], 16),
            upper=int(edit_value_location.value["high"], 16),
            bounds="[]",
        )
    elif typed_edit_value_dict[edit_value_location.column_name]["type"] == ColumnType.COLOR:
        edit_value_location.value = "_" + edit_value_location.value

    try:
        cursor.execute(f"UPDATE {tableId} "
                       f"SET {edit_value_location.column_name} = %s "
                       f"WHERE id = {edit_value_location.row_id};", (edit_value_location.value,))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        connection.close()
    response.status_code = 201
    return hateoas_links(database=databaseId, table=tableId)


@router.get(
    "/database/{databaseId}/table/{tableId}",
    responses={
        200: {"model": List[dict], "description": "Success!"},
        400: {"description": "Bad request."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def get_table_data(
    response: Response,
    databaseId: str = Path(None, description="Database Name"),
    tableId: str = Path(None, description="Table Name")
) -> dict:
    """Get specified tables."""
    connection, cursor = get_db_connection(databaseId)
    try:
        cursor.execute(f"SELECT * FROM {tableId};")
        result = list(map(list, cursor.fetchall()))
        for row in result:
            for i in range(len(row)):
                if type(row[i]) is str and row[i][0] == "_":
                    row[i] = row[i][1:]
                elif type(row[i]) is psycopg2._range.NumericRange:
                    row[i] = {
                        "low": f"{row[i].lower:x}",
                        "high": f"{row[i].upper - 1:x}"
                    }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        connection.close()
    response.status_code = 200
    return {"result": result, "links": hateoas_links(database=databaseId, table=tableId)}



@router.post(
    "/database/{databaseId}/table/{tableId}/dedup",
    responses={
        201: {"description": "Deduplication successful"},
        400: {"description": "An error occurred during projection operation."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def dedup_table(
    response: Response,
    databaseId: str = Path(None, description="Database Name"),
    tableId: str = Path(None, description="Table Name"),
    meta_db_connection: Session = Depends(get_meta_db)
) -> dict:
    """Return a projection of a database to specific columns"""

    connection, cursor = get_db_connection(databaseId)
    try:
        cursor.execute(f"SELECT * FROM {tableId};")
        result = list(map(list, cursor.fetchall()))

        for row in result:
            for i in range(len(row)):
                if type(row[i]) is str and row[i][0] == "_":
                    row[i] = row[i][1:]
                elif type(row[i]) is psycopg2._range.NumericRange:
                    row[i] = (f"{row[i].lower:x}", f"{row[i].upper - 1:x}")

        ids_to_delete = find_ids_of_duplicates(result)
        if len(ids_to_delete) > 0:
            arg_list = ["%s" for i in range(len(ids_to_delete))]
            arg_string = ",".join(arg_list)
            cursor.execute(f"DELETE FROM {tableId} WHERE id IN ({arg_string});", tuple(ids_to_delete))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        connection.close()
    response.status_code = 201
    return {"links": hateoas_links(database=databaseId, table=tableId)}



@router.get(
    "/database/{databaseId}/tables",
    responses={
        200: {"model": List[dict], "description": "Success!"},
        400: {"description": "Bad request."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def get_all_tables(
    databaseId: str = Path(None, description="Database Name"),
    meta_db_connection: Session = Depends(get_meta_db),
) -> dict:
    """Get all tables."""
    tables = fetch_all_tables_for_database(database=databaseId, session=meta_db_connection)
    return {"tables": tables, "links": hateoas_links(database=databaseId)}


@router.post(
    "/database/read_dump",
    responses={
        201: {"description": "Database has been read from dump"},
        400: {"description": "An error occured during database creation."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
def database_read_dump_post(
    dump: UploadFile = Form(None, description=""),
    database: str = Form(None),
    table_schema: str = Form(None),
    meta_db_connection = Depends(get_meta_db)
) -> dict:
    """Read database from dump"""
    contents = dump.file.read()
    try:
        psql('-d', database, '-h', 'localhost', '-U', 'postgres', _env={"PGPASSWORD": "postgres"},_in=contents)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    columns = json.loads(table_schema)["columns"]
    table_name = json.loads(table_schema)["table_name"]
    table_schema = TableSchema(columns=columns, table_name=table_name)

    for table in fetch_all_tables_for_database(database=database, session=meta_db_connection):
        delete_table_metadata(database=database, table=table.name, session=meta_db_connection)
    save_table_metadata(database=database, table_schema=table_schema, session=meta_db_connection)
    return {"links": hateoas_links(database=database)}


@router.get(
    "/database/{databaseId}/get_dump",
    responses={
        200: {"description": "Dump created and returned to the user!"},
        400: {"description": "Dump creation failed / no such database."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def get_dump(
    databaseId: str = Path(None, description="Database Name"),
) -> StreamingResponse:
    """Create a dump of a database"""
    file_path = f"dump.sql"
    with open(file_path, 'wb') as f:
        pg_dump('-h', 'localhost', '-U', 'postgres', databaseId, _out = f, _env={"PGPASSWORD": "postgres"})

    def iterfile():
        with open(file_path, mode="rb") as file_like:  #
            yield from file_like

    return StreamingResponse(iterfile())

