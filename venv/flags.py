import sys
import getopt

def read_flags():
    """Function takes string of parameters and returns dictionary of parameters"""

    possible_flags = ['n', 'f']
    params = {}
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'nf')

    except getopt.GetoptError:
        print(f'Wrong flag! Accepted flags: {possible_flags}')
        sys.exit()

    for opt, arg in opts:
        if opt == '-n':
            print('N')
            print(arg)
            params['n'] = arg
        elif opt == 'f':
            params['path'] = arg
        else:
            print('Unknown parameter!')

    return params



