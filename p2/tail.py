#!/usr/bin/env python2.7

import argparse


class TailHandler(object):
    def __init__(self, args):
        self.args = args
        print args


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store_true',
                        help='output appended data as the file grows')
    parser.add_argument('-n', action='store', type=int,
                        default=10,
                        metavar='<lines>',
                        help='output the last K lines')
    parser.add_argument('file', nargs='?', default='-', help='file to read')
    args = parser.parse_args()
    handler = {
        'tail.py': TailHandler,
    }
    handler.get(parser.prog, TailHandler)(args)


if __name__ == '__main__':
    main()
