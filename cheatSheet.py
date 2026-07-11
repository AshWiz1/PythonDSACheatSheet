from typing import List
from queue import Queue
from collections import deque 
import bisect
from math import gcd
import heapq
from sortedcontainers import SortedList, SortedSet, SortedDict

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

sortedSet = SortedSet()
sortedDict = SortedDict()

# list
arr = list()
arr.append(1)
arr.pop()
print(len(arr))

# queue
q = Queue()
q.put(1)
print(q.get()) # pops from front
print(q.qsize())

# deque
dq = deque()
dq.append(9)
dq.popleft()
dq.appendleft(1)
dq.pop()
len(dq)

# heap
h = []
heapq.heapify(h) # inplace heapifies the array.
heapq.heappush(h, (1, 2)) # push a tuple, list to the heap
val = heapq.heappop(h) 
len(h)

# initialize multi dimensional array
vis =[[False for i in range(3)] for i in range(3)]

# Set
sett = set()
sett.add(1)
sett.remove(1)
len(sett)
print( 1 in sett)
for i in sett: print(i)

# dictionary
dic = {}
print(1 in dic)
dic[1] = 3
dic.get(5, 1) # gets the value at key 1, if it does not exist it returns 0
dic.pop(1) # removes the entry from dictionary
len(dic)
for i in dic: print(i) # iterate through the keys in dic. Gets exception when dic is modified within the loop
for i in list(dic): print(i) # iterate through the key of the dic. No exception when dic is modified within the loop

# array
arr = [1, 2]
arr.remove(1) # remove given element from list => throws error if its not there
print(arr.index(2)) # gets the index of the element => throws error if its not there
print(1 in arr)

# sort
arr = [2, 1] 
arr.sort() # in-place sort
arr2 = [(1, 2), (2, 1)]
arr2.sort(key = lambda x: (x[0], x[1])) # print with a comparator
arr.sort(reverse = True) # sort in reverse order

# array/string refering
arr[-1] # last elements
arr[0: len(arr)] # sub-array from 0 to len(arr)-1 inclusive
print(arr[::-1]) # reverse an array. not in-place
temp = arr[:] # copy of array

# string
strr = 'asdfa asd'
print(ord(strr[0])) # get ascii for character
print(chr(ord(strr[0]))) # convert ascii to string
print(".".join(["Hello", "Word"])) # join string
print(strr.split(" ")) # split a string
print(strr.find("asd")) # returns index of found string
print(strr.rfind("asd")) # returns index of found string from end
print(strr.upper()) # upper case => not in-place
print(strr.lower()) # lower case
num = "121"
print(str(num)) # converts num to string  

# binary search
arr = [1,3]
print(bisect.bisect_left(arr, 2, 0, len(arr))) # gets the first index of element greater than equal to value 
print(bisect.bisect_right(arr, 2, 0, len(arr))) # gets the first index of element just greater than value

tupleArr = [(1, "value"), (2, "value")]
bisect.bisect_right(tupleArr, 1, 0, len(tupleArr), key=lambda x: x[0]) # pass the "key" as custom comparator function

# math
print(gcd(4,2))
print("22".isdigit()) # Check if a given string is number
print("A".isalpha()) # Check if a given string is alphabet
