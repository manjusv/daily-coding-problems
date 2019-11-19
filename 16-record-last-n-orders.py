# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


class Log(object):
    def __init__(self, n):
        self.n = n
        self.cur = 0
        self.arr = []

    def record(self, order_id):
        if len(self.arr) == self.n:
            self.arr[self.cur] = order_id
        else:
            self.arr.append(order_id)
        self.cur = (self.cur + 1) % self.n

    def get_last(self, i):
        return self.arr[self.cur - i]
