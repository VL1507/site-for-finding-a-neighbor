from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app
from utils.access_token import create_access_token

client = TestClient(app)


def test_():
    response = client.get("/")
    assert response.status_code == 404


def test_2plus2():
    assert 2 + 2 == 4


# def test_qqq():
#     response = client.get("/qqq")
#     assert response.status_code == 200
#     assert response.history[0].status_code == 307


# def test_tg_aouh():
#     token = create_access_token({"tg_user_id": 1111}, 1)
#     response = client.get(f"/tg_aouh/{token}")
#     assert response.status_code == 200

# token = "11111"
# response = client.get(f"/tg_aouh/{token}")
# assert response.status_code == 307


# def test_api_create_profile():
#     response = client.post(
#         "/api/create_profile", data={"gender": "male", "status": "student"}
#     )
#     assert response.status_code == 200
#     assert response.json() == {"OK": 200}


# def test_me():
#     response = client.get("/me")
#     assert response.status_code == 200
#     # assert response.json() == {"msg": "Hello World"}
#     # print(response.headers.items())
#     assert response.history[0].status_code == 307
#     assert len(response.history) == 1


# test_me()
