from abc import ABC
class Area(ABC):
    
    def area(self,msg,area):
        
        self.area1 = str(area)
        self.msg1 = msg
        
        print(self.msg1 + self.area1)
        