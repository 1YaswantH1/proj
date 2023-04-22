# nums ={1,2,4,5,6,7,8,54}
# print(type(nums))
# # del nums
# # print(nums)
# print(sorted(nums))
# print(nums)
# nums={1:"one"}

# print(nums.pop(1))
# print(type(nums))
# print(nums)
nums= [4,3,2,7,8,2,3,1]
x=[i for i in range(1,len(nums))]
y=set(x)
z=set(nums)
ans=y.intersection(z)
print(list(ans))