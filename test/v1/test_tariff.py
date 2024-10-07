V1_URL_PREFIX = "/v1/tariffs"

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
    response = client.post(f"{V1_URL_PREFIX}/", json=new_tariff)
    assert response.status_code == 200  # Expect 200 OK
    assert response.json()["name"] == new_tariff["name"]
    assert response.json()["rate"] == new_tariff["rate"]


def test_read_tariff_by_id(client, test_tariff):
    """Test reading a tariff by ID"""
    response = client.get(f"{V1_URL_PREFIX}/{test_tariff.id}") 
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
    response = client.put(f"{V1_URL_PREFIX}/{test_tariff.id}", json=updated_tariff)
    assert response.status_code == 200
    assert response.json()["name"] == updated_tariff["name"]
    assert response.json()["rate"] == updated_tariff["rate"]
    
    
def test_delete_tariff(client, test_tariff):
    """Test deleting a tariff"""
    # Ensure the tariff exists before trying to delete it. This is to ensure it does not fail silently
    response = client.get(f"{V1_URL_PREFIX}/{test_tariff.id}")
    assert response.status_code == 200
    assert response.json()["name"] == "UpdatedTariff"

    delete_response = client.delete(f"{V1_URL_PREFIX}/{test_tariff.id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["name"] == "UpdatedTariff"

    confirm_response = client.get(f"{V1_URL_PREFIX}/{test_tariff.id}")
    assert confirm_response.status_code == 404  # Tariff should no longer exist