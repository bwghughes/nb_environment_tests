""" Name of tests important here. """
import requests
import pytest
from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError

""" Environment tests should be name test_<slug>_environment. This is how we know what to update on the dashboard. """

def test_aem_environment():
    assert False


def test_mdm_environment():
    assert False


def test_nedbank_id_environment():
    assert False
