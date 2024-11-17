from typing import List
from queue import Queue
from collections import deque 
import bisect
from math import gcd
import heapq

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
heapq.heapify() # inplace heapifies the array.
heapq.heappush(h, (1, 2)) # push a tuple, list to the heap
val = heapq.heappop() 
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
for i in dic: print(i) # gets the keys in dic

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

# math
print(gcd(4,2))
