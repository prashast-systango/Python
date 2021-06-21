# Dictionary Syntax
myDictionary = {
    "Name" : "Prashast",
    "City" :"Indore",
    "Age" : 52,
    }
# print(myDictionary) # {'Name': 'Prashast', 'City': 'Indore', 'Age': 52}


# Indexed : Values can be accessed with keys
print('''Values can be accessed with keys :
myDictionary["City"]''')
#print(myDictionary["City"])
print()

# Dictionary is Mutable
print('''Dictionary is Mutable
myDictionary["Age"] = 22 ''')
myDictionary["Age"] = 22    
#print(myDictionary) # {'Name': 'Prashast', 'City': 'Indore', 'Age': 22}
print()

# Nested : Dictionary can have another dictionary in it
# Here 'myDictionary1' is outer dictionary, 'Native' is the inner one
myDictionary1 ={
    "Name" : "Prashast",
    "Native" : {"City" : "Ujjain", 
                "State" : "M.P."}
}

# Accessing inner dictionary
print('''Accessing inner dictionary
print(myDictionary1["Native"])
>>>''')
print(myDictionary1["Native"]) # 'City': 'Indore', 'State': 'M.P.'}
print()

print('''print(myDictionary1["Native"]["City"])
>>>''')
print(myDictionary1["Native"]["City"]) # Indore
print()


### Methods

#1 (keys)
# Syntax : Dictionary.keys()
# print(myDictionary.keys()) # prints the keys of dictionary (default type : class)

#2 (values)
# Syntax : Dictionary.values
# print(myDictionary.values()) # prints the keys of dictionary

# typecasting
# print(list(myDictionary.keys())) # prints the list of keys of dictionary 

#3 (items)
# Syntax : Dictionary.items()
# "myDictionary.items()" returns the (key,value) pair in list form (Iterable : can be helpfull while using loops)
# print(myDictionary.items())

#4 (update) 
# Syntax : Dictionary.update(Dictionary2)
myDictionary.update(myDictionary1) # updates the dictionary, adds the values of 'myDictionary1' to 'myDictionary' 
print(myDictionary)
# it adds the (key,value) pair to the dictionary
# it can also update the value for a key


#5 (get)
# Syntax : Dictionary.get(key)
# returns the value associated with the passed key, only if the key is present in dictionary
print(myDictionary.get("City")) # Indore


#6 (pop)
# Syntax : Dictionary.pop(key)
# Removes the (key,value) pair for the key passed
# And Returns the value for the key
# x = myDictionary.pop("Age") 
# print(x)                       # 22
# print(myDictionary)      #{'Name': 'Prashast', 'City': 'Indore','Native': {'City': 'Ujjain', 'State': 'M.P.'}}



## Dictionary.get(key)  vs  Dictionary[key]
# we passed a key 'name20', which is not present in the Dictionary
print(myDictionary.get("Name20")) # Returns None (No error)
# print(myDictionary["Name20"]) # Throws an error

myDictionary2 = {
    "A" : 1,
    "B" : 2,
    "c" : 3,
    "D" : 4
}
for i in myDictionary2.values():
    # x = myDictionary2.(i)
#     x = i+5
#     myDictionary2[i]= x
# print(myDictionary2)    
    print(i)

val =myDictionary2.values()
print(sum(val))