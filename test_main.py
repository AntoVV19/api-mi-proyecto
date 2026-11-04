from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)

def test_crear_libro():
    r = cliente.post("/libros", json={"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "precio": 49.90})
    assert r.status_code == 201
    assert r.json()["id"] == 1

def test_libro_no_existente():
    r = cliente.get("/libros/99")
    assert r.status_code == 404
