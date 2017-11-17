""" Name of tests important here. """
import requests
import pytest
from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError

""" Environment tests should be name test_<slug>_environment. This is how we know what to update on the dashboard. """

def test_aem_environment():
    assert requests.get("https://google.com").status_code == 200


def test_mdm_environment():
    assert requests.get("https://google.com").status_code == 200


def test_nedbank_id_environment():
    assert requests.get("https://google.com").status_code == 200


def test_ecm_environment():
    assert requests.get("https://google.com").status_code == 200


def test_cde_environment():
    assert requests.get("https://google.com").status_code == 200
