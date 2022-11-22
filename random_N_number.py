import random

b=[]
c=[]

n=int(input("enter the number of inputs: "))
for i in range(n):
    b.append(random.randint(1,n))
    c=list(set(b))

print("radom list number is:",c)
