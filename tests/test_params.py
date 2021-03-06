from typing import List

import pytest

from openapi_specgen import OpenApiParam

from .utils import DataclassObject


@pytest.mark.parametrize('location', [
    ('query'),
    ('path'),
    ('header'),
    ('cookie')
])
def test_param_location(location):
    expected_param_dict = {
        'required': True,
        'schema': {
            'title': 'Test_Param',
            'type': 'string'
        },
        'name': 'test_param',
        'in': location
    }
    openapi_param = OpenApiParam('test_param', location, str)
    assert expected_param_dict == openapi_param.as_dict()


def test_param_optinal():
    expected_param_dict = {
        'required': False,
        'schema': {
            'title': 'Test_Param',
            'type': 'string'
        },
        'name': 'test_param',
        'in': 'path'
    }
    openapi_param = OpenApiParam('test_param', 'path', str, required=False)
    assert expected_param_dict == openapi_param.as_dict()


def test_param_default():
    expected_param_dict = {
        'required': True,
        'schema': {
            'title': 'Test_Param',
            'type': 'string',
            'default': 'default_value'
        },
        'name': 'test_param',
        'in': 'path'
    }
    openapi_param = OpenApiParam('test_param', 'path', str, 'default_value')
    assert expected_param_dict == openapi_param.as_dict()


def test_param_any_type():
    expected_param_dict = {
        'required': True,
        'schema': {
            'title': 'Test_Param'
        },
        'name': 'test_param',
        'in': 'path'
    }
    openapi_param = OpenApiParam('test_param', 'path')
    assert expected_param_dict == openapi_param.as_dict()


@pytest.mark.skip('WIP')
def test_param_enum():
    pass


@pytest.mark.skip('WIP')
def test_param_examples():
    pass


@pytest.mark.skip('WIP')
def test_param_empty_value():
    pass


@pytest.mark.skip('WIP')
def test_param_nullable():
    pass


@pytest.mark.skip('WIP')
def test_param_deprecated():
    pass
