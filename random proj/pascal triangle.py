def factorial(num):
    fact=1
    for k in range(1,num+1):
        fact=fact*k
    return fact
def pascal_triangle(rows):
    ans=[]
    for i in range(rows+1):
        ref_list=factorial(rows)//((factorial(rows-i))*(factorial(i)))
        ans.append(ref_list)
    return ans
if __name__=="__main__":
    x=int(input())
    for l in range(x):
        print(pascal_triangle(l))
    
