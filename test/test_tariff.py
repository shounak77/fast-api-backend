
def test_create_tariff(client):
    """Test creating a new tariff"""
    new_tariff = {
        "name": "Test2",
        "description": "TestDescreption",
        "rate": 0.10,
        "currency": "RUB",
        "tax_rate": 0.06,
        "code": "H7K9I"
    }
    response = client.post("/tariffs/", json=new_tariff)
    assert response.status_code == 200  # Expect 200 OK
    assert response.json()["name"] == new_tariff["name"]
    assert response.json()["rate"] == new_tariff["rate"]