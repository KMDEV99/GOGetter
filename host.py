#! /usr/bin/python3


class Host:
    def __init__(self, value):
        self.hMin = value
        self.hMax = value
        self.hSum = value
        self.hCount = 1

    def get_avg(self):
        return self.hSum / self.hCount

    def update(self, new_value):
        self.hCount += 1
        self.hMin = new_value if new_value < self.hMin else self.hMin
        self.hMax = new_value if new_value > self.hMax else self.hMax
        self.hSum += new_value

    def __eq__(self, host2):
        if not isinstance(host2, Host):
            return NotImplemented

        return self.hMin == host2.hMin and self.hMax == host2.hMax and self.hSum == host2.hSum and self.hCount == host2.hCount

    def __str__(self):
        return "hMin: %s, hMax: %s, hSum: %s, hCount: %s" % (self.hMin, self.hMax, self.hSum, self.hCount)
