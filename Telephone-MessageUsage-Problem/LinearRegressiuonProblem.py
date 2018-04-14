import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(pd.__version__)
print(np.__version__)

df = pd.read_csv('telephone_message.csv')
'''print(df)
print(df.head())
print(df.head(6))
print(df.shape)'''
#print(df.describe())


## convert pandas dataframe to ndarray
arr = np.array(df.values, np.float)

#  Data visualization using matplotlib
plt.plot(arr[:, 0], arr[:, 1])
plt.plot(arr[:, 0], arr[: ,1] ,'ro')
plt.xlabel('time (in minutes)')
plt.ylabel('messages')
plt.title('Telephone time-message data')
plt.axis([0, 300, 0, 1000])
plt.show()

### generating linear regression model for the problem
#####print sum of x
print(sum(arr[:,0]))
X = sum(arr[:,0])
#####print sum of y
print(sum(arr[:,1]))
Y = sum(arr[:,1])
#####print sum of x-square
print(sum(np.square(arr[:,0])))
X2 = sum(np.square(arr[:,0]))
#####print sum of y-square
print(sum(np.square(arr[:,1])))
Y2 = sum(np.square(arr[:,1]))

print(sum(np.multiply(arr[:,0],arr[:,1])))
XY = sum(np.multiply(arr[:,0],arr[:,1]))
N = len(arr[:,0])
#calulate value of a and b
A = (Y*X2 -X*XY)/((N*X2)-X*X)
B = ((N*XY)-(X*Y))/((N*X2)-X*X)
A = round(A, 4)
B = round(B, 4)
print("Linear equation for data set : y = ", A, " ", B, "x")
print("Enter value for x :")
inX = float(input())
outY = int(A + B * inX)
print("Output Y = ", outY)

'''x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
print(x1,x2)
print(np.multiply(x1, x2))'''
