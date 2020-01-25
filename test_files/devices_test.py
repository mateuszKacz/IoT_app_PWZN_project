from device import Devices
import flags
import pytest
from unittest.mock import patch
import sys


@pytest.mark.parametrize('args, comment, expected',
                         [[['main.py', '-n', '4'], 'Simple run with -n parameter', 4],
                          [['main.py', '-f', 'test_iot_dev.txt'], 'Simple run with -f parameter.', 3],
                          [['main.py'], 'No parameters run.', 1],
                          [['main.py', '-n', '20'], '-n to big', 16]
                          ])
def test_devices_sample_input(args, comment, expected):
    """Tests Devices class object creation with sample -n or -f parameter"""
    with patch.object(sys, 'argv', args):
        print(comment)
        params = flags.read_flags()
        devices = Devices(params)
        assert devices.number_of_devices == expected
