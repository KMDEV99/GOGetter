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
