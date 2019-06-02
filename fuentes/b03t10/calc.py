#!/usr/bin/env python3

import argparse

def _add(a):
    _add.description = 'Summation of {} is {}'
    return sum(a)

def _avg(a):
    _avg.description = 'The average of {} is {}'
    return sum(a)/len(a)

def _build_parser():
    parser = argparse.ArgumentParser(
        description='Make operations with numbers.')

    # positional arguments
    parser.add_argument('numbers', nargs='*', metavar='N', type=int)

    # options
    parser.add_argument(
        '--sum', action='store_true',
        help='calculate the summation of numbers')
    parser.add_argument('--avg', action='store_true',
        help='calculate the average of numbers')
    parser.add_argument('-v', '--verbose', action='count', default=0,
        help='increase output verbosity')

    return parser

if __name__ == '__main__':
    parser = _build_parser()
    args = parser.parse_args()

    numbers = args.numbers
    if args.verbose >= 2:
        print('calc in verbose mode.')

    if args.sum:
        result = _add(numbers)
        if args.verbose >= 1:
            print(_add.description.format(numbers, result))
        else:
            print(result)

    if args.avg:
        result = _avg(numbers)
        if args.verbose >= 1:
            print(_avg.description.format(numbers, result))
        else:
            print(result)
