class New1(object):
    # constructor :will be called at the time of object creation
    def __init__(self):
        print("hello from __init__")

    # instance method
    def newMeth(self):
        print("hello from instance method")

    @classmethod
    def classMethod(cls):
        print("hello from class method")

    @staticmethod
    def staticMeth():
        print("hello from static method")

# object creation (constructor will be called)
obj1 = New1()
obj1.newMeth()  # calling normal method

# class methods and static methods can be called on classname
New1.classMethod()
New1.staticMeth()




# Passing member of one class to another class
class Student:
    def __init__(self, r, n):
        self.roll_no = r
        self.name = n
    def display(abc):
        print("Name :",abc.name)
        print("Roll_no :",abc.roll_no)


class User:
    @staticmethod
    def show(s):
        print("Name :",s.name)
        print("Roll_no :",s.roll_no)
        s.display()
        
stu = Student(10701, "Prashast")
User.show(stu)