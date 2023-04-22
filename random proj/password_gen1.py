# password generater till 26 digits--->
def pass_gen(a):
    password=""
    ref=0
    for i in x:
            ref+=1
            password=i+password
            if ref==digits:
                 break
    print(password)
if __name__=="__main__":
    x = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',   's', 't','u', 'v', 'w', 'x', 'y', 'z'}
    digits=int(input())
    password=""
    ref=1
    pass_gen(digits)

    


