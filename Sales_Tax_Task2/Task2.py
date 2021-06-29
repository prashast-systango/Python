# Input File
file_input = open('Input2.csv',mode='r')
# Input File Content
input_data = file_input.read()
content_list = input_data.split("\n")
file_input.close()

# Output File Content will be stored in this list
output_list = ['Product-Name,Product-CostPrice,Product-SalesTax,Product-FinalPrice,Country']
# 
class Main(object):
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
obj.generateOutput()

file_output = open('Output2.csv',mode='w')
file_output.writelines(output_list)
print("Output Generated !!!")
file_output.close()