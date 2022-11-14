import psycopg2
from starlette.testclient import TestClient

from src.openapi_server.models.table_schema import TableSchema


class TestEditValue:
    def test_edit_value(
            self,
            client: TestClient,
            mock_database_with_filled_table_connection: psycopg2.extensions.cursor,
            test_database_name: str,
            test_table_schema: TableSchema,
    ):
        edit_value_and_location = {
            "row_id": 1,
            "column_name": "first",
            "value": 2
        }

        response = client.request(
            "PATCH",
            "/database/{databaseId}/table/{tableId}/edit_value".format(
                databaseId=test_database_name,
                tableId=test_table_schema.table_name,
            ),
            headers={},
            json=edit_value_and_location,
        )

        assert response.status_code == 201

    def test_edit_value_range(
            self,
            client: TestClient,
            mock_database_with_filled_table_connection: psycopg2.extensions.cursor,
            test_database_name: str,
            test_table_schema: TableSchema,
    ):
        edit_value_and_location = {
            "row_id": 1,
            "column_name": "sixth",
            "value": {
                "low": "FFFFFE",
                "high": "FFFFFF",
            }
        }

        response = client.request(
            "PATCH",
            "/database/{databaseId}/table/{tableId}/edit_value".format(
                databaseId=test_database_name,
                tableId=test_table_schema.table_name,
            ),
            headers={},
            json=edit_value_and_location,
        )

        assert response.status_code == 201


    def test_edit_value_color(
            self,
            client: TestClient,
            mock_database_with_filled_table_connection: psycopg2.extensions.cursor,
            test_database_name: str,
            test_table_schema: TableSchema,
    ):
        edit_value_and_location = {
            "row_id": 1,
            "column_name": "fifth",
            "value":  "FFFFFE",
        }
        response = client.request(
            "PATCH",
            "/database/{databaseId}/table/{tableId}/edit_value".format(
                databaseId=test_database_name,
                tableId=test_table_schema.table_name,
            ),
            headers={},
            json=edit_value_and_location
        )

        assert response.status_code == 201

