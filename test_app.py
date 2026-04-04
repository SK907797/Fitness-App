from app import app

def test_login_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_dashboard_redirect():
    client = app.test_client()
    response = client.get("/dashboard")
    assert response.status_code == 302

def test_add_client():
    client = app.test_client()
    response = client.post("/add_client", data={"name": "TestUser"})
    assert response.status_code == 302