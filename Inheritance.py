# class Parent_name:
#     parent body
# class Child(Parent_name):
#     child body    

# Parent-class
class Father:
    money = 10000

    def __init__(self):
        print("Parent-class constructor")

    def show(self):
        print("Parent-class instance method")

    @classmethod
    def showMoney(cls):
        print("Parent-class class method")
    
    @staticmethod
    def stat():
        print("Parent-class static method")

# Child-class
class Son(Father):
    # def __init__(self):
    #     print("Child-class constructor")

    def disp(self):
        print("Child-class instance method")



s = Son() # Parent class constructor will be called automatically, if child class constructor is not present
s.disp()
# we can call parent class methods on child class object
s.show()
s.showMoney()
s.stat()

# we cannot call child class method on parent object
# f = Father()
# f.disp()  # AttributeError