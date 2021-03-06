from datetime import date, datetime
from typing import List

import pytest
from openapi_specgen.schema import get_openapi_schema

from .utils import (DataclassNestedObject, DataclassObject,
                    MarshmallowNestedSchema, MarshmallowSchema)


@pytest.mark.parametrize('data_type, openapi_schema', [
    (str, {'type': 'string'}),
    (date, {'type': 'string', 'format': 'date'}),
    (datetime, {'type': 'string', 'format': 'date-time'}),
    (int, {'type': 'integer'}),
    (float, {'type': 'number'}),
    (bool, {'type': 'boolean'}),
    (DataclassObject, {'$ref': '#/components/schemas/DataclassObject'}),
    (List, {'type': 'array', 'items': {}}),
    (
        List[DataclassObject],
        {'type': 'array', 'items': {'$ref': '#/components/schemas/DataclassObject'}}
    ),
    (List[str], {'type': 'array', 'items': {'type': 'string'}}),
    (List[int], {'type': 'array', 'items': {'type': 'integer'}}),
    (List[float], {'type': 'array', 'items': {'type': 'number'}}),
    (List[bool], {'type': 'array', 'items': {'type': 'boolean'}})
])
def test_openapi_schema(data_type, openapi_schema):
    assert openapi_schema == get_openapi_schema(data_type)


def test_dataclass_schema():
    expected_openapi_schema = {
        'DataclassObject': {
            'title': 'DataclassObject',
            'type': 'object',
            'required': ['str_field', 'int_field', 'float_field',
                         'boolean_field', 'list_field', 'date_field', 'datetime_field'],
            'properties': {
                'str_field': {'type': 'string'},
                'int_field': {'type': 'integer'},
                'float_field': {'type': 'number'},
                'boolean_field': {'type': 'boolean'},
                'list_field': {'type': 'array', 'items': {}},
                'date_field': {'type': 'string', 'format': 'date'},
                'datetime_field': {'type': 'string', 'format': 'date-time'},
            }
        }
    }
    assert expected_openapi_schema == get_openapi_schema(DataclassObject, reference=False)


def test_dataclass_nested_objects():
    expected_openapi_schema = {
        'DataclassNestedObject': {
            'title': 'DataclassNestedObject',
            'type': 'object',
            'required':
            [
                'str_field',
                'nested_object'
            ],
            'properties': {
                'str_field': {'type': 'string'},
                'nested_object': {'$ref': '#/components/schemas/DataclassObject'}
            }
        },
        'DataclassObject': {
            'title': 'DataclassObject',
            'required': ['str_field', 'int_field', 'float_field',
                         'boolean_field', 'list_field', 'date_field', 'datetime_field'],
            'type': 'object',
            'properties': {
                'str_field': {'type': 'string'},
                'int_field': {'type': 'integer'},
                'float_field': {'type': 'number'},
                'boolean_field': {'type': 'boolean'},
                'list_field': {'type': 'array', 'items': {}},
                'date_field': {'type': 'string', 'format': 'date'},
                'datetime_field': {'type': 'string', 'format': 'date-time'},
            }
        }
    }
    assert expected_openapi_schema == get_openapi_schema(DataclassNestedObject, reference=False)


def test_marshmallow_schema():
    expected_openapi_schema = {
        'Marshmallow': {
            'title': 'Marshmallow',
            'type': 'object',
            'required':
            [
                'str_field'
            ],
            'properties': {
                'str_field': {'type': 'string'},
                'int_field': {'type': 'integer'},
                'float_field': {'type': 'number'},
                'boolean_field': {'type': 'boolean'},
                'list_field': {'type': 'array', 'items': {'type': 'string'}},
                'date_field': {'type': 'string', 'format': 'date'},
                'datetime_field': {'type': 'string', 'format': 'date-time'},
            }
        }
    }
    assert expected_openapi_schema == get_openapi_schema(MarshmallowSchema, reference=False)


def test_marshmallow_nested_schema():
    expected_openapi_schema = {
        'Marshmallow': {
            'title': 'Marshmallow',
            'type': 'object',
            'required':
            [
                'str_field'
            ],
            'properties': {
                'str_field': {'type': 'string'},
                'int_field': {'type': 'integer'},
                'float_field': {'type': 'number'},
                'boolean_field': {'type': 'boolean'},
                'list_field': {'type': 'array', 'items': {'type': 'string'}},
                'date_field': {'type': 'string', 'format': 'date'},
                'datetime_field': {'type': 'string', 'format': 'date-time'},
            }
        },
        'MarshmallowNested': {
            'title': 'MarshmallowNested',
            'type': 'object',
            'required':
            [
                'str_field'
            ],
            'properties': {
                'str_field': {'type': 'string'},
                'int_field': {'type': 'integer'},
                'float_field': {'type': 'number'},
                'boolean_field': {'type': 'boolean'},
                'list_field': {'type': 'array', 'items': {'type': 'string'}},
                'nested_schema': {'$ref': '#/components/schemas/Marshmallow'},
                'self_reference': {'$ref': '#/components/schemas/MarshmallowNested'}
            }
        }
    }
    assert expected_openapi_schema == get_openapi_schema(MarshmallowNestedSchema, reference=False)
