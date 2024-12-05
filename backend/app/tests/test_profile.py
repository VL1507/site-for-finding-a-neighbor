from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# def test_create_profile():
#     response = client.post(f"/api/v1/create_profile")
#     assert response.status_code == 201
#     assert response.json() == {
#         "name": "Bob",
#         "gender": "1",
#         "status": "0",
#         "smoking": "8",
#         "go_to_bed_at": "666",
#         "get_up_in": "999",
#     }