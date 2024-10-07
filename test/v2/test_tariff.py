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
    print(response.json())
    assert response.status_code == 200 
    assert response.json()["code"] == 200
    assert response.json()["data"]["name"] == new_tariff["name"] 
    assert response.json()["data"]["rate"] == new_tariff["rate"]