from datetime import date

# Creating class
class Vehicle:
    
    # Constructor
    def __init__(self, brand, model, type):
        # Instance attributes
        self.brand = brand
        self.type = type
        self.model = model
        self.fuel_cap = 11
        self.fuel = 0
    # Method
    def fuel_up(self):
        self.fuel = self.fuel_cap    
        print("Tank Full :",self.fuel) 

    # Method
    def vehicle_detail(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Type :", self.type)
        print("Fuel tank capacity :", self.fuel_cap)
        print("Date :",date)
        # print("Brand", self.brand)

    # Class Method
    @classmethod
    def buyerDetails(cls,Name,Address):
        cls.Name = Name
        cls.Address = Address
        print("Buyer :",cls.Name)
        print("Assress :",cls.Address)

    # Static Method
    @staticmethod
    def currentDate():
        return date.today()
    
    

date = Vehicle.currentDate() # calling static method
print(date)
Vehicle.buyerDetails("Prashast","Indore")

veh = Vehicle("TVS","Apache","Bike") # object creation
veh.vehicle_detail() # calling method with object
print("Accessing attributes :",veh.__dict__) # Accessing attributes using object
print()


veh1 = Vehicle("Hyundai","Verna","Car") # object creation
veh1.fuel_cap = 22 # changing attribute value using object
veh1.vehicle_detail()
print()
veh1.fuel_up()
# print(date.today())