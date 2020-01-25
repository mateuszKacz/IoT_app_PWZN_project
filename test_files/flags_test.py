from flags import read_flags
import sys
from unittest.mock import patch
import pytest


@pytest.mark.parametrize('args, comment, expected',
                         [[['main.py', '-n', '4'], 'Simple run with -n parameter', {'n': 4}],
                          [['main.py', '-f', 'test_iot_dev.txt'], 'Simple run with -f parameter.', {'f': 'test_iot_dev.txt'}],
                          [['main.py'], 'No parameters run.', {}],
                          [['main.py', '-n', '20'], '-n to big', {'n': 16}]
                          ])
def test_read_flags_normal(args, comment, expected):
    """testing read_flags() function"""

    with patch.object(sys, 'argv', args):
        print(comment)
        assert read_flags() == expected


def test_n_to_big():
    """Testing with -n param with to big parameter >16"""

    with patch.object(sys, 'argv', ['main.py', '-n', '20']):
        print('Testing with -n param negative')
        assert read_flags() == {'n': 16}


def test_n_negative():
    """Testing with -n param negative"""

    with patch.object(sys, 'argv', ['main.py', '-n', '-1']):
        print('Testing with -n param negative')
        try:
            read_flags()
        except Exception as err:
            assert isinstance(err, ValueError)


def test_f_not_exists():
    """Tests parsing with not existing path"""
    with patch.object(sys, 'argv', ['main.py', '-f', 'tes']):
        print('Tests parsing with not existing path')
        try:
            read_flags()
        except Exception as err:
            assert isinstance(err, NotADirectoryError)