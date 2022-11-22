import math

count=int(input("enter a number of calculations: "))
for i in range(count):
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))

    result=math.gcd(num1,num2)
    print("result is : ",result)
print("finish!")