import pytest
import requests
from unittest.mock import Mock

import pytest
import requests
from unittest.mock import Mock


@pytest.fixture
def mock_get(mocker):
    mock = Mock()
    mocker.patch('requests.get', return_value=mock)
    return mock


def test_get_request(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'key': 'value'}
    response = requests.get('http://example.com')
    assert response.status_code == 200
    assert response.json() == {'key': 'value'}
