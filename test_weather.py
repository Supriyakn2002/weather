import pytest
from weather import get_weather

def test_get_weather_success(monkeypatch):
    class MockResponse:
        status_code = 200
        def json(self):
            return {
                "current": {
                    "temp_c": 25,
                    "condition": {"text": "Sunny"},
                    "humidity": 60
                }
            }

    def mock_get(*args, **kwargs):
        return MockResponse()

    # Mocking requests.get
    import requests
    monkeypatch.setattr(requests, "get", mock_get)

    api_key = "fake_api_key"
    city = "Bangalore"
    result = get_weather(city, api_key)

    assert result["city"] == "Bangalore"
    assert result["temp_c"] == 25
    assert result["condition"] == "Sunny"
    assert result["humidity"] == 60

def test_get_weather_failure(monkeypatch):
    class MockResponse:
        status_code = 404
        def json(self):
            return {}

    def mock_get(*args, **kwargs):
        return MockResponse()

    import requests
    monkeypatch.setattr(requests, "get", mock_get)

    result = get_weather("InvalidCity", "fake_api_key")
    assert result is None
