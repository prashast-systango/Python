# Set is a collection of non-repetitive elements
# a = {1,2,3,1,1,1,1}
# print(a) >>> {1,2,3}

# Syntax
# a = {} this is not an empty set(this is an empty dictionary)
# a = set() this is an empty set

a = {1,2,3,4,5}
a1 = set()
a2 = set()


# (set.add())
# Syntax : set.add(element)
a2.add(9)
a2.add(21)
a2.add(30)
a2.add(34)
a2.add(35)

# a2.add([1,2,3]) # we cannot add list in a set, because lists are mutable and sets are not
a2.add((1,2,3)) # we can add tuples in a set, as tuples are immutable
# a2.add({2:3}) # we cannot add dictionary in a set, because dictionaries are mutable and sets are not
print(a2)

# (len(set))
#Returns the length
print("length of b2 : ",len(a2)) # 3

# (remove())
# Syntax : (set.remove(element))
# a2.remove(2) # throws error as '2' is not present in the set
a2.remove(21)  # removes '21' from set


# (pop())
# removes and returns any random element from the set
# Syntax : (set.pop())
a2.pop()
print(a2)

# (union())
# 
for i in a2:
    print(i)