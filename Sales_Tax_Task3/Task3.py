# Importing the input file module-
from Input import InputClass
#
import re
# Regex for int/float value 
intFloatRegex = '(\d+(\.\d+)?)'

# Regex for string value
stringRegex =  '[a-zA-Z\s]+$'

content_list = InputClass.input_data.split("\n")
# Output File Content will be stored in this list
output_list = ['Product-Name,Product-CostPrice,Product-SalesTax,Product-FinalPrice,Country']
# 
class Main(object):
    # Input File validation function
    def inputFormatValidation(self):
        for i in range(len(content_list)):
            
            if i != 0:
                self.temp_list1 = content_list[i].split(",")
                # Input file format validation
                if len(self.temp_list1) < 4:
                    raise Exception('''Invalid Input, one or more fields empty''')
                elif len(self.temp_list1) > 4:
                    raise Exception('''Invalid Input, there should only be 4 fields of input''')
                
                # Product-name validation
                if (re.fullmatch(stringRegex, self.temp_list1[0])):
                    pass
                else:
                    raise Exception("Invalid Input, Not a String, in 'Product-name' in row ",i+1)
                
                # Country validation
                if (re.fullmatch(stringRegex, self.temp_list1[3])):
                    pass
                else:
                    raise Exception("Invalid Input, Not a String, in 'Country' in row ",i+1)
                
                # Sales tax validation 
                if (re.fullmatch(intFloatRegex, self.temp_list1[2])):
                    pass
                else:
                    raise Exception("Invalid Input, Not a Number, in 'Sales Tax Percentage'in row ",i+1)
                
                # Cost price validation 
                if (re.fullmatch(intFloatRegex, self.temp_list1[1])):
                    pass
                else:
                    raise Exception("Invalid Input, Not a Number, in 'Cost Prize' in row ",i+1)


    
    def generateOutput(self):
        for i in range(len(content_list)):
            # print(i)
            if i != 0:
                # This takes each row from input file one by one
                # The list contains each field of a row as elements
                self.temp_list = content_list[i].split(",")
                self.current_sales_tax_Percentage = int(self.temp_list[2])
                self.sales_tax_amount = (self.current_sales_tax_Percentage/100) * int(self.temp_list[1])
                self.final_price = self.sales_tax_amount + int(self.temp_list[1])
                # The string takes values for each row one by one, in specified output format
                self.output_string = (f"\n{self.temp_list[0]},{self.temp_list[1]},{self.current_sales_tax_Percentage},{self.final_price},{self.temp_list[3]}")
                # Appending the string in output list
                output_list.append(self.output_string)

obj = Main()
obj.inputFormatValidation()
obj.generateOutput()

file_output = open('Output3.csv',mode='w')
file_output.writelines(output_list)
print("Output Generated !!!")
file_output.close()