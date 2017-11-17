""" Utils for testing """
import os
import requests
from requests.exceptions import ConnectionError


class ReporterException(BaseException):
    pass


def get_slug_from_test_name(test_name: str):
    """ Figures out slug from test name """
    if isinstance(test_name, str) and test_name.startswith("test_") \
        and test_name.endswith("_environment"):
        return test_name[5:-12].replace('_', '-')
    else:
        raise TypeError(f"{test_name} is not valid name. \
                        I was expecting an environment or application name. \
                        It really should end look like test_something_environment.")


def get_proper_name_from_slug(name: str) -> str:
    return name.replace("-", " ").capitalize()


def update_or_create_environment(name: str, result):
    """ Function to post update to dashboard, check if eists, if not call create then update """
    
    try:
        slug = get_slug_from_test_name(name)
    except TypeError as ex:
        raise ReporterException(ex)

    
    try:
        url = f"{os.getenv('ENVSTATUS_BASE_URL').strip()}/environments/{slug}"
        print(f"Updating dashboard at {url}...")
        response = requests.get(url)
        
        if response.status_code == 404:
            print(f"Not found creating new for {name}...")
            create_url = f"{os.getenv('ENVSTATUS_BASE_URL').strip()}/environments/?name={get_proper_name_from_slug(slug)}"
            response = requests.post(create_url)
        
        # TODO Investigate wierdness - if I post with no value its good, anything
        # else is True.
        if not result:
            result = ""

        url = f"{os.getenv('ENVSTATUS_BASE_URL').strip()}/environments/{slug}?test_result={result}"
        print(f"Updating {slug} with {result}...{type(result)}")
        response = requests.put(url)
    except ReporterException as e:
        raise(e)
    except ConnectionError as e:
        print(e)
        raise