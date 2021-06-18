name= "prashast"
print(name)
length= len(name) # 8
print(name.count("s")) # 2
print(name.capitalize()) # Prashast
print(name.find("rash")) # if present, returns the index of first element(r)= 2
print(name.find("dash"),"\n") # returns -1

# Escape sequences
print("Prashast\tSitani\n")
print("Prashast\\Sitani")
print("Prashast\Sitani")
print("Prashast\'s")

# slicing
print(name[0],name[-6],name[-7],name[-1],name[4],"\n")
print(name[0:])
print(name[::-1])
print(name[0::1])
print(name[0::2])
print(name[0::3])