# input function always stores the value as a string

#name= input("Enter your name: ")
# print(name)
# print(type(name))
#age= input("Enter your age: ")
# print(type(age))
# age= int(age)
# print(type(age))
name= input("Enter your name: ")
yearBorn= input("Enter your year of birth: ")
presentYear= input("Enter the current year: ")
yearBorn= int(yearBorn)
presentYear= int(presentYear)
age= (presentYear-yearBorn)

yearBorn= str(yearBorn)
presentYear= str(presentYear)
age= str(age)
#print("your age is",age)
message='''\nHello NAME,
you are AGE years old,
Have a great YEAR ahead !!!'''

message= message.replace("NAME", name)
message= message.replace("AGE", age)
message= message.replace("YEAR", presentYear)
print(message)