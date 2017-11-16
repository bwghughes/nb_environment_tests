"""conftest module provides config to pytest to push results to server."""
import os

from _pytest.runner import runtestprotocol

from utils import update_or_create_environment

BASE_URL = os.getenv("ENVSTATUS_BASE_URL")


def pytest_runtest_protocol(item, nextitem):
    """ After each test, report result to """
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'call':
            if item.name.startswith("test_") and item.name.endswith("_environment"):
                print(f"{item.name} is {report.passed}")
                update_or_create_environment(item.name, report.passed)
    return True
