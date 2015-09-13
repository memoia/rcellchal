#!/usr/bin/env python2.7

import os
import sys
import logging
import argparse
import threading
from time import sleep


logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)


class FileMonitor(threading.Thread):
    def __init__(self, path, interval, stop_event):
        self.path = path
        self.interval = interval
        self.stop_event = stop_event
        self.last_stat = self.stat(self.path)
        self.offset = self.last_stat.st_size
        threading.Thread.__init__(self)

    def stat(self, identifier):
        return (os.fstat(sys.stdin.fileno())
                if identifier == '-'
                else os.stat(identifier))

    def next(self):
        data = None
        if self.path == '-':
            data = sys.stdin.read()
        else:
            if os.path.isfile(self.path):
                fd = open(self.path, 'r')
                fd.seek(self.offset)
                data = fd.read()
                self.offset = fd.tell()
                fd.close()
        return data

    def run(self):
        while not self.stop_event.is_set():
            current_stat = self.stat(self.path)
            if self.last_stat.st_mtime != current_stat.st_mtime:
                LOG.debug('Change to {}'.format(self.path))
                if self.last_stat.st_size < self.offset:
                    self.offset = 0
                buff = self.next()
                if buff:
                    print buff
                self.last_stat = current_stat
            sleep(self.interval)


class MonitorCoordinator(object):
    def __init__(self, args):
        self.args = args
        self.threads = []
        self.stop_event = threading.Event()
        for path in self.args.filepath:
            self.threads.append(FileMonitor(path, self.args.s, self.stop_event))
        self.start()

    def start(self):
        map(lambda t: t.start(), self.threads)
        try:
            while True:
                sleep(self.args.s)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.stop_event.set()
        map(lambda t: t.join(), self.threads)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store_true',
                        help='output appended data as the file grows')
    parser.add_argument('-n', action='store', type=int,
                        default=10,
                        metavar='<lines>',
                        help='output the last K lines')
    parser.add_argument('-s', action='store', type=int,
                        default=1,
                        metavar='<seconds>',
                        help='sleep interval')
    parser.add_argument('filepath', nargs='*',
                        default=['-'], help='file to read')
    args = parser.parse_args()
    if args.f:
        MonitorCoordinator(args)


if __name__ == '__main__':
    main()
