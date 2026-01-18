from typing import List
from queue import Queue
from collections import deque 
import bisect
from math import gcd
import heapq
from sortedcontainers import SortedList

arr = [(1, "value")]
print(bisect.bisect_right(arr, 1, 0, len(arr), key=lambda x: x[0]))

arr = [1]
print(bisect.bisect_right(arr, 1, 0, len(arr)))

arr = [1, 2]
print("".join([str(i) for i in arr]))

dic ={1: 2, 3: 4}
print(list(dic.keys()))

print([1, 2].sort())

print(-10%11)

# sorted list
# https://grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedcontainers.SortedList.bisect_right
sortedList = SortedList(key = lambda x: -x) # optional key which tells sortedList how to compare its elements
sortedList.add(1)
sortedList.add(2)
sortedList.add(2)
sortedList.bisect_left(2) # Just like normal bisect_left  => return first index >= val
sortedList.bisect_right(2) # Returns first index > val
sortedList.pop(0) # Removes value at given index
sortedList.remove(1) # Removes a certain value
sortedList.index(2) # Gets the index of certain value, has optional start, stop optional parameters