# creating a list
# List can store multiple datatypes together
a= [99, "Prashast", True, "Potter", 1.55, "False"]
print(a)
for i in a:
    print(i)

# editing the list
a[0]= "Dash"
a[1]= "Harry"
# a[5]= "Bill" we cannot add elements like this (gives error: index out of range)
print(a)

# List Slicing
print(a[0:])
print(a[-3:])
print(a[-3:4])
print(a[0:-2])
print(a[-4:4])

# List Methods
l1 =[9 ,96 ,8 ,44 ,569 , 20]
l2=[9,8,7,6]
l3=[44,55,66,77]
print(l1)
print(sum(l1)) # sums all the elements of list

l1.sort() # sorts the list
print(l1)
l1.reverse() # reverses
print(l1)
l1.append(l2)# adds at the end of list, when list in arguement (List is added within the list)
print(l1) # [569, 96, 44, 20, 9, 8, [9, 8, 7, 6]]
l3.extend(l2)# adds at the end of list, when list in arguement (elements of list are added within the list)
print(l3) # [44, 55, 66, 77, 9, 8, 7, 6]

print(l1)
l1.insert(2,12) # inserts 12 at 2nd index
print(l1)
popped_val= l1.pop(2) # removes and returns the value at passed index
print(popped_val)
print(l1)
#l1.remove(149) # removes the passed value from the list, if present
# Gives error if the value passed is not in the list
# l1.remove(11111) (ValueError: list.remove(x): x not in list)
print(l1)


# Tuples(can have homogenous as well as heterogeneous data)
t = (1, 3, 1, 5, 7, 9, 1)
t1 = ()   # empty tuple
# t2 =(1)   wrong way to declare tuple with 1 element
t2 = (1,)   # tuple with one value
# t(0)= 9   tuples are immutable, cannot edit

# Tuples Methods
print(t.count(1)) # returns number of occurrences of value passed
print(t.index(5)) # Return first index of value. Raises ValueError if the value is not present.
