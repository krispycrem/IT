from fastapi import HTTPException

from src.openapi_server.database.sql_alchemy import SessionLocal
from src.openapi_server.database.utils import get_db_connection
from src.openapi_server.models.column_type import ColumnType


def is_color(hex_repr: str):
    try:
        int_repr = int(hex_repr, 16)
    except Exception as e:
        return False
    if int_repr >= 0 and int_repr < 16**6:
        return True
    return False


def get_meta_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def populate_cols_with_type(non_file_cols: dict):
    typed_values = {}
    for key, val in non_file_cols.items():
        if type(val) is int:
            typed_values[key] = {
                "type": ColumnType.INTEGER
            }
        elif type(val) is float:
            typed_values[key] = {
                "type": ColumnType.REAL,
            }
        elif type(val) is str and len(val) == 1:
            typed_values[key] = {
                "type": ColumnType.CHAR
            }
        elif type(val) is dict and \
            type(val.get("low")) is str and \
            type(val.get("high")) is str and \
            int(val.get("low"), 16) < int(val.get("high"), 16) and \
            is_color(val.get("low")) and is_color(val.get("high")):
                typed_values[key] = {
                    "type": ColumnType.COLOR_INTERVAL
                }
        elif type(val) is str and is_color(val):
            typed_values[key] = {
                "type": ColumnType.COLOR
            }
        elif type(val) is str:
            typed_values[key] = {
                "type": ColumnType.STRING
            }
        else:
            raise HTTPException(status_code=400, detail="Bad data!")
        typed_values[key]["value"] = val
    return typed_values



def table_has_data(database, table):
    connection, cursor = get_db_connection(database)
    try:
        cursor.execute(f"SELECT * FROM {table};")
        results = len(cursor.fetchall())
    finally:
        connection.close()
    return results > 0

def hateoas_links(
        database: str = None,
        table: str = None,
):
    link_dictionary = {
        "read_from_dump": "/database/read_dump",
    }
    if database:
        link_dictionary["get_dump"] = "/database/{database}/get_dump"
        link_dictionary["create_table"] = "/database/{database}/table/create"
        link_dictionary["get_all_tables"] = "/database/{databaseId}/tables"
    if table:
        link_dictionary["add_row"] = "/database/{databaseId}/table/{table_id}/add_row"
        link_dictionary["delete_table"] = "/database/{databaseId}/table/{tableId}"
        link_dictionary["dedup"] = "/database/{databaseId}/table/{table_id}/dedup"
        link_dictionary["get_data_from_table"] = "/database/{databaseId}/table/{tableId}"
    if database and table and table_has_data(database, table):
        link_dictionary["edit_value"] = "/database/{databaseId}/table/{tableId}/edit_value"
    return link_dictionary


def get_type(column):
    return column[1]

def get_name(column):
    return column[0]

def are_rows_equal(row_1, row_2):
    row_1 = row_1[1:]
    row_2 = row_2[1:]
    for x,y in zip(row_1, row_2):
        if x != y:
            return False
    return True

def find_ids_of_duplicates(result):
    ids_to_delete = set()
    i = 0
    while i < len(result):
        fixed_row = result[i]
        j = i + 1
        while j < len(result):
            moving_row = result[j]
            if are_rows_equal(fixed_row, moving_row):
                ids_to_delete.add(moving_row[0])
            j += 1
        i += 1

    return ids_to_delete
