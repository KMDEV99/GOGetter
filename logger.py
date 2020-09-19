#! /usr/bin/python3

import logging


def init_logger():
    FORMAT = '%(asctime)s %(levelname)s:%(message)s'
    logging.basicConfig(format=FORMAT, filename='host.log', level=logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger().addHandler(console)
