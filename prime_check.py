import math
a = int(input("enter a number"))
divide =2
limit = math.sqrt(a)
goal =0

while divide <=limit:
    if a % divide ==0:
        goal +=1
        print(" a = ",a,"is not prime..")
        print(exit())
    else:
        pass
    divide+=1
if goal==0:
    print("a =",a,"is prime number")
