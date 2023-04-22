x=[1,2,4,3,6,7,9,45,78,-1,-3,-6,-9,-45]
def positive1(x):
    return x>0
y=list(filter(positive1,x))
print(y)