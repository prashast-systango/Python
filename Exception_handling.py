print("Division")
a = int(input("Enter a number :"))
b = int(input("Enter another number :"))

try:
    print(a/b)
except ZeroDivisionError as e1:
    print(e1)    
except Exception as e:  # e is an object
    print(e)    # prints the object of Exception
except: # This can be used when the exception is not known
    print("only except")
else:  # This will be executed whenever except will not be executed
    print("Else: this will be executed, whenever except will not be executed")
finally:  # This will be executed everytime
    print("This is finally, and will be executed everytime")
print("Rest of the code")