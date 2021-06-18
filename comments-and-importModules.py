# single line comment
'''multi
line
comment'''

# importing modules
import os
import random

# (os.listdir) returns a list containing the names of the entries in the directory given by path
print(os.listdir('/home//ubox13//Desktop//Python//Python'))
# (random.choice) returns any random element from the list 
fruits= ["apple","mango","banana","grapes","kiwi"]
fruit= random.choice(fruits)
print(fruit)