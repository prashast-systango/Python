# Default parameter value(It executes when no parameter is passed while calling a parametrized function)
def greet(name="Stranger"):
    return print("Hello,",name)

greet("Prashast")
greet()


# factorial
def factorial(num):
    ans=1
    for i in range(num):
        ans= ans *(i+1)
    return ans

# f =int(input("Enter the number: "))
# printFact= factorial(f)
# print("Factorial of",f,"is",printFact)



# factorial using recursion
def factorial_recursive(num):
    if (num == 0 or num == 1):
        return 1
    else:    
        product = num * factorial_recursive(num-1)
    return product

# enteredNum =int(input("Enter number :"))
# s = factorial_recursive(enteredNum)
# print(s)


# max of 3 numbers
def maximum(num1, num2, num3):
    if(num1 > num2):
        if(num1 >num3):
            return num1
        else:
            return num3
    else:
        if(num2 > num3):
            return num2
        else:
            return num3

# print("Enter three numbers you want to compare :")
# numbers =[int(input()),int(input()),int(input())]
# max = maximum(numbers[0],numbers[1],numbers[2])
# print("Maximum number is :",max)


# print function
print("Hello")
print("my")
print("name")
print("is")
print("Prashast")

print()

print("Hello", end="")
print("my", end="")
print("name", end="")
print("is", end="")
print("Prashast")

print()

print("Hello", end=" ")
print("my", end=" ")
print("name", end=" ")
print("is", end=" ")
print("Prashast")

# pattern
n= 9
for i in range(n):
    print("*" * (n-i))

for i in range(n):
    print("*" * (i+1))

# anonymous or lambda function
'''def minus(a,b):
    return x-y'''
# below code is same as the above one    
minus =lambda a,b :a-b
print(minus(9,2))

# even = lambda list1: