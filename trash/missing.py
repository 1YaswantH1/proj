nums=[4,3,2,7,8,2,3,1]
x=[i for i in range(len(nums))]
print(list(set(x).difference(nums)))