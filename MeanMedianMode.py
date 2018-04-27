# This program is to calculate the mean median and mode of sample population.
# Program takes input n as the number of element in data sample and an array of n element of data sample.

from collections import Counter
from itertools import groupby
n = int(input())
arr = list(map(int,input().split()))

mean = sum(arr)/n
mid = n//2
arr = sorted(arr)
median = 0.0
if n % 2 == 0:
    median = (arr[mid-1]+arr[mid])/2
else:
    median = arr[mid]
mode = 0
arr_f = Counter(arr).most_common()
arr_f = [list(g) for k,g in groupby(arr_f,key=lambda x:x[1])]
arr_f = sorted(arr_f[0],key= lambda x:x[0])

mode = arr_f[0][0]
print('%.1f\n%.1f\n%d'%(mean,median,mode))
