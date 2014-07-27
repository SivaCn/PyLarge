#!/usr/bin/python


## ------------ Imports ----------- ##
## ------------ Imports ----------- ##


class Reader(object):
    def get_header(self, _file):
        fp = open(_file, 'r')
        _header = fp.readline()
        fp.close()
        return _header

class BulkReader(Reader):
    def read(self, _file):
        with open(_file, 'r') as fp:
            _data = fp.readlines()
        return _data[1:]

class SequenceReader(Reader):
    def read(self, _file):
        fp = open(_file, 'r')
        _header = fp.readline()
        _line = fp.readline()

        while _line:
            yield _line
            _line = fp.readline()

        fp.close()
