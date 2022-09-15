from enum import Enum
import sys


class ArgNumber(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    STOP = 999


def main(argv):
    for arg in (data for data in argv):
        ArgNumber(arg)


if __name__ == '__main__':
    main(sys.argv)
