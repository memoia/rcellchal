#!opt/bin/python

import logging
import argparse
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)


class FileModifiedHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print 'yep'


class ObserverCoordinator(object):
    def __init__(self, args):
        self.args = args
        self.observers = []
        event = FileModifiedHandler()
        for path in self.args.filepath:
            obs = Observer(timeout=self.args.s)
            obs.schedule(event, path, recursive=False)
            self.observers.append(obs)
        self.start()

    def start(self):
        map(lambda o: o.start(), self.observers)
        try:
            while True:
                sleep(self.args.s)
        except KeyboardInterrupt:
            map(lambda o: o.stop(), self.observers)
            map(lambda o: o.join(), self.observers)


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
    observers = ObserverCoordinator(args)


if __name__ == '__main__':
    main()
