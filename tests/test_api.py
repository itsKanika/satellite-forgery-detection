from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_detection_endpoint():
    with open("tests/sample.jpg", "rb") as f:
        response = client.post(
            "/api/v1/detect",
            files={"image": ("test.jpg", f, "image/jpeg")}
        )
    assert response.status_code == 200
    data = response.json()
    assert "confidence" in data
    assert isinstance(data["is_authentic"], bool)

def test_invalid_file():
    response = client.post(
        "/api/v1/detect",
        files={"image": ("test.txt", b"fake content", "text/plain")}
    )
    assert response.status_code == 400