""" Name of tests important here. """
import requests

""" Environment tests should be name test_<slug>_environment. This is how we know what to update on the dashboard. """

def test_completely_new_environment():
    response = requests.get("https://httpbin.org/ip")
    assert response.status_code == 201


def test_arrangement_environment():
    response = requests.get("https://httpbin.org/ip")
    assert response.status_code == 200


def test_party_environment():
    response = requests.get("https://httpbin.org/ip")
    assert response.status_code == 201


def test_dirty_cache_environment():
    response = requests.get("https://httpbin.org/ip")
    assert response.status_code == 201


def test_aem_environment():
    response = requests.get("https://httpbin.org/ip")
    assert response.status_code == 200


def test_product_catalogue_environment():
    response = requests.get("https://httpbin.org/ip")
    assert response.status_code == 200
