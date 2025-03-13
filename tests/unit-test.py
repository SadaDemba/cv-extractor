from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur l'API d'extraction de CV !"}

def test_extract_endpoint():
    with open("example.pdf", "rb") as file:
        response = client.post("/extract/", files={"file": file})
    assert response.status_code == 200
