from unittest import TestCase
from data_manipulate import DataManipulate
from file_handler import FileHandler
from host import Host


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
        input_hosts = ['host1.bom', 'host2.com']
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

    def test_get_host_dict_from_csv(self):
        expected_value = {
            "host1.com": self.prepare_host([3063.33, 9618.39, 19707.9, 3]),
            "host2.com": self.prepare_host([1301.62, 1301.62, 1301.62, 1]),
            "host4.com": self.prepare_host([6647.35, 9203.05, 24547.58, 3]),
            "host5.com": self.prepare_host([1812.97, 1812.97, 1812.97, 1]),
            "host7.com": self.prepare_host([1, 1, 1.0, 1]),
        }

        fh = FileHandler(input_path="testInput.csv", output_path="")
        dm = DataManipulate(fh)
        dict_res = dm.get_host_dict_from_csv()
        for key in dict_res.keys():
            self.assertEqual(dict_res[key], expected_value[key], msg="%s %s == %s" % (key, dict_res[key], expected_value[key]))
        self.assertFalse("host6.com" in dict_res.keys())

    def prepare_host(self, params):
        host = Host(1)
        host.hMin = params[0]
        host.hMax = params[1]
        host.hSum = params[2]
        host.hCount = params[3]
        return host
