from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_user():
    user_id = 1
    response = client.get(f"/api/v1/user/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"id": user_id, "is_admin": False}

    user_id = 100
    response = client.get(f"/api/v1/user/{user_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

    user_id = "String"
    response = client.get(f"/api/v1/user/{user_id}")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["path", "user_id"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": user_id,
            }
        ]
    }
