
####  @Copyright  Atul Kumar  ############
############################# Pearson correlation coefficient #############################
###################################### SAMPLE INPUT  ####################
###################    15  12  8   8   7   7   7   6   5   3
###################    10  25  17  11  13  17  20  13  9   15
#############################OUTPUT= 0.145 ############
############## -1 <= r <= 1 , It has a value between +1 and −1, where 1 is total positive linear correlation,
###########  0 is no linear correlation, and −1 is total negative linear correlation.


X = list(map(float, input().split()))
Y = list(map(float, input().split()))
#print(phy,his)

x_mean = sum(X)/len(X)
y_mean = sum(Y)/len(Y)

x_y = list(map(lambda x, y: (x-x_mean) * (y-y_mean), X, Y))
x_x = list(map(lambda x: (x-x_mean)*(x-x_mean), X))
y_y = list(map(lambda y: (y-y_mean)*(y-y_mean), Y))

numerator = sum(x_y)
denum     = pow(sum(x_x), 0.5) * pow(sum(y_y), 0.5)

r = round(numerator/denum, 3)

print(r)