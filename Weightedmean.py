
# This program takes the three lines of input. First line  has the number of element in data sample.
# Second line take the n data values and third line has n number of wights of data sample.


n = int(input())

x = list(map(int,input().split()))
w = list(map(int,input().split()))

xw = list(map(lambda a,b:a*b,x,w))
W = sum(w)

wMean = round(sum(xw)/W,1)
print(wMean)