# Iterator 
#
# Syntax : next(iterator[, default])
# (next()) function is used to fetch next item from the collection


# Generator
def mygenerator(n):
    for i in range(n):
        yield i
#n = int(input("Enter number :"))
n = 1000
obj1 = mygenerator(n)
print(next(obj1))
print(next(obj1))
print()


# Itetating in a string

# str = "Prashast"
# str1 = itr(str)
str1 = iter("Prashast") # creating a iterator
print(next(str1))
print(next(str1))
print(next(str1))
print(next(str1))
print(next(str1))
