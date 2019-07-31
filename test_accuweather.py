from http import HTTPStatus
import os

def test_forecast_request(client):
    data = {
        "location":"Pune"
    }
    url = "/forecast"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_forecast_request_fail(client):
    data = {
        "location":"test city"
    }
    url = "/forecast"
    response = client.post(url, json=data)
    assert response.json ==  {'success': False, 'error': 'Location not found!'}

def test_forecast_bad_request(client):
    os.environ['API_KEY'] = 'asdasdasd'
    data = {
        "location":"Pune"
    }
    url = "/forecast"
    response = client.post(url, json=data)
    print("response {}", response.json)
    assert response.status_code ==  {'success': False, 'error': 'AccuWeather responded with a 401!'}