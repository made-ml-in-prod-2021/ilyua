from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_predict():
    response = client.post(
        "/predict/",
        json={"f1":0.1,"f2":0.3,"f3":1,"f4":0.9},
    )
    assert response.status_code == 200

