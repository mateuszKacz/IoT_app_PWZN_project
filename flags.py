import argparse
from os.path import isfile
from sys import exit


def read_flags():
    """Function takes string of parameters and returns dictionary of parameters"""

    parser = argparse.ArgumentParser(description="Parse input params")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-n', metavar='n', type=int, help='Input how many mock devices to create at startup')
    group.add_argument('-f', metavar='f', type=str, help='Path to file with devices to create')

    try:
        args = parser.parse_args()
    except argparse.ArgumentError as exc:
        print('To many params')
        raise exc

    if args.n is not None:
        if args.n > 16:
            print('-n parameter to big, making max 16 devices')
            return {'n': 16}
        elif args.n <= 0:
            raise ValueError('Wrong -n parameter value')
        else:
            return {'n': args.n}

    elif args.f is not None:
        if isfile(args.f):
            return {'f': args.f}
        else:
            print('-f parameter is not file')
            raise NotADirectoryError

    else:
        return {}

