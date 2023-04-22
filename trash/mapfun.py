# x=["1","2","3","4","5"]
# print(type(x[1]))

# y=list(map(int,x))

# print(type(y[1]))
# # map function takes two arguments for 1 it uses function and other iteratables like list val ect

def fun(x):
    return x*x
x=[1,2]
y=list(map(fun,x))
print(y)
