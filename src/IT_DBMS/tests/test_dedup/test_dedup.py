import psycopg2
from starlette.testclient import TestClient

from src.openapi_server.apis.utils import are_rows_equal, find_ids_of_duplicates
from src.openapi_server.models.table_schema import TableSchema

def test_dedup(
        client: TestClient,
        mock_database_with_filled_duplicate_table_connection: psycopg2.extensions.cursor,
        test_database_name: str,
        test_table_schema: TableSchema
):
    response = client.request(
        "POST",
        "/database/{databaseId}/table/{tableId}/dedup".format(
            databaseId=test_database_name,
            tableId=test_table_schema.table_name,
        ),
        headers={},
        json={},
    )

    assert response.status_code == 201

def test_dedup_are_rows_equal(row1, row2):
    assert are_rows_equal(row1, row2) is True

def test_dedup_are_rows_equal_bad(row1, row2):
    row2[1] = "bad"
    assert are_rows_equal(row1, row2) is False

def test_dedup_ids(row1, row2):
    assert find_ids_of_duplicates([row1, row2]) == {2}