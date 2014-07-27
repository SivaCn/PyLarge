#!/usr/bin/python


## ------------ Imports ----------- ##
from utilities import ConfigHelper
from utilities import InvalidOptionToSet
## ------------ Imports ----------- ##

__all__ = ['ConfigSetups']


class ConfigSetups(ConfigHelper):
    def __update_config(self, _datadict, section):
        if not isinstance(_datadict, dict):
            _msg = "Argument '_datadict' must be a Dictionary, but not {0}"
            raise TypeError(_msg.format(type(_datadict)))

        _options_available = self.get_options(section)

        for option in _datadict:
            if option not in _options_available:
                _msg = "UnIdentifiable Option '{0}' under '{1}'"
                raise InvalidOptionToSet(_msg.format(option, section))
            self.set_value(_section, option, _dataset[option])

    def hdfsfiles(self, _datadict):
        section = 'hdfsfiles'
        self.__update_config(_datadict, section)

    def mongodb(self, _datadict):
        section = 'mongodb'
        self.__update_config(_datadict, section)

    def filesystem(self, _datadict):
        section = 'filesystem'
        self.__update_config(_datadict, section)
