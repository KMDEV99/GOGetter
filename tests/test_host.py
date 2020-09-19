from unittest import TestCase
from host import Host


class TestHost(TestCase):
    def setUp(self):
        self.val1 = 1000.1
        self.val2 = 1000.2
        self.val3 = 255
        self.host1 = Host(self.val1)
        self.host1.update(self.val2)
        self.host1.update(self.val3)

    def test_update_avg(self):
        output_avg = (self.val1 + self.val2 + self.val3) / 3
        self.assertEqual(self.host1.get_avg(), output_avg)

    def test_update_sum(self):
        output_sum = self.val1 + self.val2 + self.val3
        self.assertEqual(self.host1.hSum, output_sum)

    def test_update_count(self):
        output_count = 3
        self.assertEqual(self.host1.hCount, output_count)

    def test_update_min(self):
        output_min = self.val3
        self.assertEqual(self.host1.hMin, output_min)

    def test_update_max(self):
        output_max = self.val2
        self.assertEqual(self.host1.hMax, output_max)
