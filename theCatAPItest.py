from unittest import mock
import requests
from theCatAPI import get_random_cat_image

@mock.patch("requests.get")
def test_successful_request(mock_get):
    mock_url = "https://cdn2.thecatapi.com/images/mock_image.jpg"
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"url": mock_url}]
    mock_get.return_value = mock_response

    result = get_random_cat_image()
    assert result == mock_url

@mock.patch("requests.get")
def test_unsuccessful_request(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    result = get_random_cat_image()
    assert result is None

@mock.patch("requests.get")
def test_request_exception(mock_get):
    mock_get.side_effect = requests.RequestException

    result = get_random_cat_image()
    assert result is None

