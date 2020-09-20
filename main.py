#! /usr/bin/python3

import data_manipulate
import arguments_parser
import sys
import file_handler
import logging
import logger


def main(argv):
    logger.init_logger()
    logging.info('Welcome to GOGetter 3000 :) \nType -h for help')

    input_path, output_path = arguments_parser.parse_input(argv)

    fh = file_handler.FileHandler(input_path, output_path)
    dm = data_manipulate.DataManipulate(fh)

    res = dm.get_host_dict_from_csv()
    if res:
        fh.save_to_csv(res)


if __name__ == "__main__":
    main(sys.argv[1:])
