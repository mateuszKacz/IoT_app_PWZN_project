import sys
import getopt
import os


def read_flags():
    """Function takes string of parameters and returns dictionary of parameters"""

    possible_flags = ['n', 'f']
    params = {}
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'n:f:')

    except getopt.GetoptError:
        print(f'Wrong flag! Accepted flags: {possible_flags}')
        sys.exit()

    for opt, arg in opts:
        if opt == '-n':
            if int(arg) > 0:
                params['n'] = int(arg)
            else:
                print('Wrong flag value!')
                sys.exit()
        elif opt == '-f':
            if os.path.isfile(arg):
                params['f'] = arg
            else:
                print('Parameter is not a directory or file does not exist!')
                sys.exit()
        else:
            print('Unknown parameter!')

    return params



