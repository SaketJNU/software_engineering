"""
A function is a block of organized, reusable code that is used to perform a single, related action.
Functions provide better modularity for your application and a high degree of code reusing.
--Types of Function ---
1->Function with no argument and no Return value
2->Function with no argument and with Return value
3->Function with argument and No Return value
4->Function with argument and Return value
"""

# Keyword Arguments 

def addition(firstNum,secondNum,thirdNum):
    sum = firstNum+secondNum+thirdNum
    return (sum)

firstNum = 40
secondNum = 50 
thirdNum = 10
sum = addition (firstNum, secondNum , thirdNum)
print("Sum in keyword argument = {}".format(sum))


# Default Arguments

def addition1(a1,b1,c1=10):
    sum1 = a1+b1+c1
    return sum1

a1 = 40 
b1 = 50
c1 = 10
result = addition1(40,50)
print("Sum in default arguments = {}".format(result))



def addition2(a,b,c):
    print("a = {},b={},c{}".format(a,b,c))
    return a+b+c

x = 40 
y = 50
z = 10 
sum2 = addition2(x,y,z) # we can also do as -> sum = addition(a = x,b = y,c = z)
print("Sum is :",sum2)