import pytest
import responses
from theCatAPI import get_random_cat_image

@responses.activate
def test_successful_request():
    mock_url = "https://cdn2.thecatapi.com/images/mock_image.jpg"
    responses.add(
        responses.GET,
        "https://api.thecatapi.com/v1/images/search",
        json=[{"url": mock_url}],
        status=200
    )

    result = get_random_cat_image()
    assert result == mock_url

@responses.activate
def test_unsuccessful_request():
    responses.add(
        responses.GET,
        "https://api.thecatapi.com/v1/images/search",
        status=404
    )

    result = get_random_cat_image()
    assert result is None

@responses.activate
def test_request_exception():
    responses.add(
        responses.GET,
        "https://api.thecatapi.com/v1/images/search",
        body=Exception("Network error")
    )

    result = get_random_cat_image()
    assert result is None
