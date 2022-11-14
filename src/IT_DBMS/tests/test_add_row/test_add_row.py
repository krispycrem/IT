import psycopg2
from psycopg2._range import Range
from starlette.testclient import TestClient

from src.openapi_server.models.table_schema import TableSchema


class TestAddRow:

    def test_add_row(
            self,
            client: TestClient,
            mock_database_with_table_connection: psycopg2.extensions.cursor,
            test_database_name: str,
            test_table_schema: TableSchema,
    ):
        response = client.request(
            "POST",
            "/database/{databaseId}/table/{table_id}/add_row"
                .format(
                    databaseId=test_database_name,
                    table_id=test_table_schema.table_name
                ),
            headers={},
            files={
                "row_data": (None, '{'
                            '   "first": 1,' 
                            '   "second": 1.2,'
                            '   "third": "c",'
                            '   "fourth": "str",'
                            '   "fifth": "111111",'
                            '   "sixth": {'
                                   '    "low": "FFFFFE",'
                                   '    "high": "FFFFFF"'
                                   '}'
                            '}'),
            }
        )
        assert response.status_code == 201




