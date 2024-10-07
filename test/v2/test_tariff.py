V2_URL_PREFIX = "/v2/tariffs"

def test_create_tariff(client):
    """Test creating a new tariff (v2)"""
    new_tariff = {
        "name": "TestV2",
        "description": "TestDescription",
        "rate": 0.06247,
        "currency": "RUB",
        "tax_rate": 0.06,
        "code": "H7K9I"
    }
    
    response = client.post(f"{V2_URL_PREFIX}/", json=new_tariff)
    assert response.status_code == 200 
    assert response.json()["code"] == 200
    assert response.json()["data"]["name"] == new_tariff["name"] 
    assert response.json()["data"]["rate"] == new_tariff["rate"]

    
def test_read_tariff_by_id(client, test_tariff):
    """Test reading a tariff by ID"""
    response = client.get(f"{V2_URL_PREFIX}/{test_tariff.id}")  
    assert response.status_code == 200
    assert response.json()["data"]["name"] == test_tariff.name 

def test_read_tariff_not_found(client):
    """Test retrieving a tariff by ID (v2) - Tariff Not Found"""
    
    non_existent_tariff_id = 2356  # this ID does not exist in the DB
    

    response = client.get(f"{V2_URL_PREFIX}/{non_existent_tariff_id}")
    
    assert response.json()["code"] == 404
    assert response.json()["message"] == "Tariff not found"
    assert response.json()["errors"]["tariff_id"] == non_existent_tariff_id
    
    
def test_query_tariffs_by_name(client):
    response = client.get(f"{V2_URL_PREFIX}?name=TestTariff")
    assert response.json()["code"] == 200
    assert response.json()["data"][0]["name"] == "TestTariff"


def test_query_tariffs_by_code(client):
    response = client.get(f"{V2_URL_PREFIX}?code=99LBN")
    assert response.json()["code"] == 200
    assert response.json()["data"][0]["code"] == "99LBN"


def test_query_tariffs_by_currency(client):
    response = client.get(f"{V2_URL_PREFIX}?currency=RUB")
    assert response.json()["code"] == 200
    assert response.json()["data"][0]["currency"] == "RUB"


def test_update_tariff(client, test_tariff):
    """Test updating an existing tariff"""
    updated_tariff = {
        "name": "UpdatedTariff",
        "description": "This will be deleted in the next test",
        "rate": 0.15,
        "currency": "USD",
        "tax_rate": 0.07,
        "code": "NEW45"
    }
    response = client.put(f"{V2_URL_PREFIX}/{test_tariff.id}", json=updated_tariff)
    assert response.status_code == 200
    assert response.json()["data"]["name"] == updated_tariff["name"]
    assert response.json()["data"]["rate"] == updated_tariff["rate"]
    

def test_delete_tariff(client, test_tariff):
    """Test deleting a tariff"""

    response = client.get(f"{V2_URL_PREFIX}/{test_tariff.id}")
    assert response.json()["code"] == 200
    assert response.json()["data"]["name"] == "UpdatedTariff"

    delete_response = client.delete(f"{V2_URL_PREFIX}/{test_tariff.id}")
    assert delete_response.json()["code"] == 200
    assert delete_response.json()["data"]["name"] == "UpdatedTariff"


    confirm_response = client.get(f"{V2_URL_PREFIX}/{test_tariff.id}")
    assert confirm_response.json()["code"] == 404 
    