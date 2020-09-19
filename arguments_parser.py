#! /usr/bin/python3

import argparse
from file_handler import default_input_path, default_output_path


def __init_parser():
    parser = argparse.ArgumentParser(
        "\nCalculates min value, max value, avg value and sum for hosts and saves results to .csv file\n"
        r"Valid host name should match regex '\w+\d?\.\w+', for example 'testhostname.pl'.")

    parser.add_argument('-i', type=str, default=default_input_path,
                        help='Input file path (Default path: "%s")' % default_input_path)

    parser.add_argument('-o', type=str, default=default_output_path,
                        help='Output file path (Default path: "%s")' % default_output_path)

    return parser


def parse_input(argv):
    h_parser = __init_parser()
    parsed = h_parser.parse_args(argv)
    return parsed.i, parsed.o
