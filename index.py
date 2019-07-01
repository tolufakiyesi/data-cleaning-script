import sys
import re


if len(sys.argv) < 2:
    print('Error! polarity is required as command a line argument')
    exit()

polarity = sys.argv[1]


if __name__ == '__main__':
    for line in sys.stdin:
        if line.strip()[-2:] == '\\\"':
            print('__label__{0} {1}"'.format(polarity, line.strip()[:-2]))
        elif line.strip()[-1:] == '\\':
            print('__label__{0} {1}'.format(polarity,line.strip()[:-1]))
