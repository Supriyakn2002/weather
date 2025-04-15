from weather import get_weather
from unittest.mock import patch

@patch("requests.get")
def test_get_weather_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "current": {"temp_c": 25, "condition": {"text": "Sunny"}, "humidity": 60}
    }

    result = get_weather("Bangalore", "fake_api_key")

    assert result == {
        "city": "Bangalore",
        "temp_c": 25,
        "condition": "Sunny",
        "humidity": 60
    }

@patch("requests.get")
def test_get_weather_failure(mock_get):
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {}

    assert get_weather("InvalidCity", "fake_api_key") is None

