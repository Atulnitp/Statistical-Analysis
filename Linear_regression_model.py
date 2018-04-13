
### @Copyright Atul Kumar
####### Linear regression is a way to model the relationship between two variables.
####### like y =  b0 + b1x
#
#
##############################################################

print("independent variable list")
x = list(map(float, input().split()))
print("Dependent variable list")
y = list(map(float, input().split()))
n = len(x)
if len(x) != len(y):
    print("input data length mismatch")

#Calculate intermediate parameter
SigmaX = sum(x)
SigmaY = sum(y)
SigmaX2 = sum([i*i for i in x])
SigmaY2 = sum([i*i for i in y])
SigmaXY = sum(list(map(lambda i, j: i*j, x, y)))

A = ((SigmaY*SigmaX2) - (SigmaX * SigmaXY))/((n*SigmaX2) - (SigmaX*SigmaX))
A = round(A,6)
B = ((n*SigmaXY) -(SigmaX*SigmaY))/((n*SigmaX2) - (SigmaX*SigmaX))
B = round(B,6)
print(A, B)

print("Input value for x to predict")
x1 = float(input())
y1 = round((A + B*x1), 6)
print("Predixted value of y : ", str(y1))