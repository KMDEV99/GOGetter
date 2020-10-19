#! /usr/bin/python3

import logging
import host
from re import match, compile


class DataManipulate:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.host_name_pattern = compile(r'\w+\d?\.\w+')

    def is_valid_row(self, hosts, values):
        """
        Checks if given strings match specified criteria (elements amount)
        :param hosts: lists of hosts
        :param values: list of values
        :returns: True if given parameters match criteria else False
        """
        is_valid = hosts and len(hosts) == len(values)
        if is_valid:
            for host in hosts:
                is_valid = self.is_valid_host_name(host)
                if not is_valid:
                    break
        if is_valid:
            for value in values:
                is_valid = self.is_valid_value(value)
                if not is_valid:
                    break
        return is_valid

    def is_valid_host_name(self, host_name):
        """
        Checks if host name matches regex pattern
        :param host_name: (str)host name
        :returns: True if matched else False
        """
        return bool(match(self.host_name_pattern, host_name))

    def is_valid_value(self, value):
        """
        Checks if value is greater than 0
        :param value: float(value)
        :returns: True if greater than 0 else False
        """
        return bool(value)

    def get_valid_row(self):
        """
        Yields valid rows from .csv file
        :returns: (list)hosts, (list)values
        """
        for hosts_to_append, values_to_append in self.file_handler.read_row_from_file():
            if self.is_valid_row(hosts_to_append, values_to_append):
                yield hosts_to_append, values_to_append

    def get_host_dict_from_csv(self):
        """
        Processing .csv data to dictionary with hosts as key
        :returns: (dict) host : host object
        """
        logging.info("Processing file: '%s'" % self.file_handler.input_path)
        res = {}
        for host_to_append, value_to_append in self.get_valid_row():
            for i, host_name in enumerate(host_to_append):
                try:
                    res[host_name].update(value_to_append[i])
                except KeyError:
                    res[host_name] = host.Host(value_to_append[i])
        return res
