#! /usr/bin/python3

import logging
from ast import literal_eval
from csv import reader, writer

default_input_path = "input.csv"
default_output_path = "output.csv"


class FileHandler:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def read_row_from_csv(self):
        """
        Yields rows (host, value) one by one from .csv file if they meet specified conditions (syntax, value).
        :returns: (str)host, (str)value
        """
        try:
            with open(self.input_path, "r", newline='') as csv_file:
                csv_reader = reader(csv_file)
                header = next(csv_reader)
                for hosts, values in csv_reader:
                    try:
                        hosts_to_append = literal_eval(hosts)
                        values_to_append = literal_eval(values)
                    except (SyntaxError, ValueError):
                        continue
                    yield hosts_to_append, values_to_append
        except (FileNotFoundError, IOError, ValueError) as err:
            logging.error(err)

    def save_to_csv(self, hosts_dict):
        """
        Saves min, max, avg, sum for each host in specified .csv file.
        :param hosts_dict: Dictionary with hosts and values
        """
        logging.debug("Saving csv to %s (%s rows)" % (self.output_path, len(hosts_dict)))
        try:
            with open(self.output_path, 'w', newline='') as file:
                output = writer(file)
                output.writerow(['host', 'min', 'max', 'avg', 'sum'])
                sorted_keys = sorted(hosts_dict.keys())
                for key in sorted_keys:
                    output.writerow(
                        [key, hosts_dict[key].hMin, hosts_dict[key].hMax, hosts_dict[key].get_avg(),
                         hosts_dict[key].hSum])
            logging.info("Successfully saved csv file: '%s'" % self.output_path)
        except (FileNotFoundError, IOError) as err:
            logging.error(err)
