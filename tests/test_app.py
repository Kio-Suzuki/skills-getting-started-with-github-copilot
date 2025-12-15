import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_api_root():
    response = client.get("/api-root")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["message"] == "API está funcionando"

# Adicione mais testes conforme necessário para outras rotas