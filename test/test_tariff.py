
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


def test_read_tariff_by_id(client, test_tariff):
    """Test reading a tariff by ID"""
    response = client.get(f"/tariffs/{test_tariff.id}") 
    assert response.status_code == 200
    assert response.json()["name"] == test_tariff.name
    
    
def test_update_tariff(client, test_tariff):
    """Test updating an existing tariff"""
    updated_tariff = {
        "name": "UpdatedTariff",
        "description": "This will be deleted in the next test",
        "rate": 0.15,
        "currency": "USD",
        "tax_rate": 0.07,
        "code": "UPD45"
    }
    response = client.put(f"/tariffs/{test_tariff.id}", json=updated_tariff)
    assert response.status_code == 200
    assert response.json()["name"] == updated_tariff["name"]
    assert response.json()["rate"] == updated_tariff["rate"]