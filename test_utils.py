import os
import pytest
from utils import get_slug_from_test_name, update_or_create_environment, \
                  ReporterException
from unittest.mock import MagicMock, patch, Mock
from utils import requests

BASE_URL = os.environ["ENVSTATUS_BASE_URL"] = "http://localhost:1234"

def test_get_slug_from_test_name_ok():
    assert get_slug_from_test_name("test_some_app_environment") == "some-app"


def test_get_slug_from_test_name_error():
    with pytest.raises(TypeError):
        get_slug_from_test_name(None)


def test_get_slug_from_test_name_not_ok_number():
    with pytest.raises(TypeError):
        get_slug_from_test_name(1)

def test_get_slug_from_test_name_not_ok_too_short():
    with pytest.raises(TypeError):
        get_slug_from_test_name("")


def test_update_or_create_environment_post_called_if_get_is_404():
    mock_response = Mock()
    mock_response.status_code = 404
    with patch('requests.put') as mock_put:
        with patch('requests.post') as mock_post:
            with patch('requests.get') as mock_get:
                mock_get.return_value = mock_response
                update_or_create_environment('test_sys_called_environment', Mock())
                assert mock_get.called
                assert mock_post.called
                assert mock_put.called

def test_update_or_create_environment_post_called_if_get_is_broken_at_all():
    with pytest.raises(ReporterException) as e:
        with patch('requests.get') as mock_get:
            mock_get.side_effect = ReporterException
            update_or_create_environment('test_sys_called_environment', Mock())


def test_update_or_create_environment_blows_up_if_dodgy_name():
    with pytest.raises(TypeError) as e:
        with patch('utils.get_slug_from_test_name') as mock_slugger:
            mock_slugger.side_effect = TypeError
            update_or_create_environment('test_sys_called_environment', Mock())

    