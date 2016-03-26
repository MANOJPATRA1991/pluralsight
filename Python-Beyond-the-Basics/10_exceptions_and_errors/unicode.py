#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)
        print("encoding: {}".format(e.encoding))
        print("reason: {}".format(e.reason))
        print("object: {}".format(e.object))
        print("start: {}".format(e.start))
        print("end: {}".format(e.end))

if __name__ == '__main__':
    main()
