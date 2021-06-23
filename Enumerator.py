# enumerate function
fruits = ["banana","apple","mango","kiwi"]

# using normal For loop
for items in fruits:
    print(items)
print()

# here 'items' stores indexes and elements in the list
for items in enumerate(fruits):
    print(items)
print()

#   
for index,items in enumerate(fruits):
    print(index)
    print(items)        
print()

# indexes,elements        (list_name,index)
for index,items in enumerate(fruits,100):
    print(index," : ",items)    