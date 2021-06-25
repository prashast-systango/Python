from abc import ABC,abstractmethod
class Calculator(ABC):
    @abstractmethod
    def calculate(self):
        pass

class Multiply(Calculator):
    def calculate(self,num1,num2):
        print("Result :",num1*num2)
class Add(Calculator):
    def calculate(self,num1,num2):
        print("Result :",num1+num2)
class Substract(Calculator):
    def calculate(self,num1,num2):
        print("Result :",num1-num2)
class Divide(Calculator):
    def calculate(self,num1,num2):
        print("Result :",num1/num2)

obj = Multiply()
obj.calculate(2,3)

obj1 = Add()
obj1.calculate(1999,1)

obj2 = Substract()
obj2.calculate(2000,1)

obj3 = Divide()
obj3.calculate(15,3)
