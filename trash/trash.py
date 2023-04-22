nums1 =[1,2]
nums2 =[3,4]
n=nums1+nums2
if len(n)%2!=0:
        median=n[(len(n)+1)//2]
else:
    print(n[len(n)//2]-1)
    print(n[(len(n)//2)])
    median=(n[len(n)//2-1]+n[(len(n)//2)])/2
print(median)

