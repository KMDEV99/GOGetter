from unittest import TestCase
from data_manipulate import DataManipulate
from file_handler import FileHandler


class TestDataManipulate(TestCase):
    def setUp(self):
        self.dm = DataManipulate(FileHandler("testInput", "testOutput"))

    def test_is_valid_row_not_diff_len(self):
        input_hosts = ['host1.bom', 'host2']
        input_values = [1123]
        self.assertFalse(self.dm.is_valid_row(input_hosts, input_values))

    def test_is_valid_row_not_diff_len2(self):
        input_hosts = ['host1.bom']
        input_values = [1123, 444545]
        self.assertFalse(self.dm.is_valid_row(input_hosts, input_values))

    def test_is_valid_row_not_both_empty(self):
        input_hosts = []
        input_values = []
        self.assertFalse(self.dm.is_valid_row(input_hosts, input_values))

    def test_is_valid_row_valid(self):
        input_hosts = ['host1.bom', 'host2']
        input_values = [1123, 444545]
        self.assertTrue(self.dm.is_valid_row(input_hosts, input_values))

    def test_is_valid_row_not_hosts_empty(self):
        input_hosts = []
        input_values = [1]
        self.assertFalse(self.dm.is_valid_row(input_hosts, input_values))

    def test_is_valid_row_not_values_empty(self):
        input_hosts = ["test"]
        input_values = []
        self.assertFalse(self.dm.is_valid_row(input_hosts, input_values))

    def test_is_valid_host_name_valid(self):
        host_name = "host2.pl"
        self.assertTrue(self.dm.is_valid_host_name(host_name))

    def test_is_valid_host_name_not_double_dot(self):
        host_name = "host..pl"
        self.assertFalse(self.dm.is_valid_host_name(host_name))

    def test_is_valid_host_name_not_no_dot(self):
        host_name = "hostpl"
        self.assertFalse(self.dm.is_valid_host_name(host_name))
