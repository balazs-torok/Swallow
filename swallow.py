#!/usr/bin/env python3.6

from argparse import ArgumentParser
from sys import stderr

from scipy.optimize import brentq


def main():
    # argument_parser = ArgumentParser(description='Calculate the swallow\'s rounds.', add_help=False)
    # argument_parser.add_argument('vs', help='The speed of the swallow', type=float)
    # try:
    #     args = argument_parser.parse_args()
    # except Exception as e:
    #     print(e)
    #     argument_parser.print_help(file=stderr)
    #     exit(1)

    result = brentq(f, 21.0, 1000.0)
    print('result={}'.format(result))


def f(vs):
    rounds = 0
    d0 = 72.1 / 2.0
    d = d0
    dn = 0.1 / 2.0
    v = 20.0
    # vs = args.vs
    while (0 < d and rounds < 32):
        d = d * (vs - v) / (vs + v)
        rounds += 1
    print('vs={}, rounds={}, d={}'.format(vs, rounds, d))
    return d - dn


if __name__ == '__main__':
    main()
