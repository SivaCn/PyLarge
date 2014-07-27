#!/usr/bin/python


## ------------ Imports ----------- ##
from ConfigParser import SafeConfigParser
## ------------ Imports ----------- ##


class BaseException(Exception):
    def __repr__(self, msg=''):
        return msg

class NoValidHeader(BaseException):
    def __repr__(self, msg=''):
        return msg

class InvalidOptionToSet(BaseException):
    def __repr__(self, msg=''):
        return msg

class ConfigHelper(object):
    def __init__(self, config_file='config.ini'):
        self.config = SafeConfigParser()
        self.config.read(config_file)

    def get_value(self, section, option):
        return self.config.get(section, option)

    def set_value(self, section, option, value):
        # Avoid writing to config file, if the config has the same value
        # as the new requested value.
        if value == self.get_value(section, option):
            return
        self.config.set(section, option, value)
        self.config.write()

    def get_sections(self):
        return self.config.sections()

    def get_options(self, section):
        return self.config.options(section)
