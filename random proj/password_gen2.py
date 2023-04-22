import random
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',   's', 't','u', 'v', 'w', 'x', 'y', 'z']
digits=int(input())
y=""
for i in range(digits):
    y+=x[random.randrange(26)]
print(y)

