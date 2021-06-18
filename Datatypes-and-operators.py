a= 299
b= 29.5
c= "Prashast"
d= 'PRASHAST'
e= ''' 'p'r'a's'h'a's't' '''
f= None
g= (1>100)
h= (100>1)

# printing variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(g)

# printing their types
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

# logical operators
print((g and h))
print((g or h))
print((not h))

# typecasting
A= "1999"
print(type(A))
A=int(A) #typecasting string to integer
print(type(A))
print(A+1)
A=str(A) # string to integer
print(type(A))