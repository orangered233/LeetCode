"""
Python bisect module
https://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html

"""
import collections
import bisect

""" The usage of Python bisect module"""


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ktv = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ktv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ktv:
            return ""
        l = self.ktv[key]
        pos = bisect.bisect(l, (timestamp, 'whatever'))
        if pos == 0:
            return ""
        else:
            return l[pos - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
