import bisect


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