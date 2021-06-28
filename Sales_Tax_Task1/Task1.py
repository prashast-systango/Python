# import csv
file_input = open('Input1.csv',mode='r')
input_data = file_input.read()
# print(input_data)
content_list = input_data.split("\n")
# print(content_list)
output_list = ['Product-Name,Product-CostPrice,Product-SalesTax,Product-SalesTaxAmount,Product-FinalPrice,Country']

# Dictionary includes (country : sales tax)
Tax_Dict ={
    'India': 15,
    'America': 30,
    'Australia': 25,
    'Bhutan': 25,
    'Nepal': 20,
    'China': 80,
    'Dubai': 20,
}
i = 1
for i in range(len(content_list)):
    # print(i)
    if i != 0:
        temp_list = content_list[i].split(",")
        current_sales_tax = Tax_Dict[temp_list[2]]
        sales_tax_amount = (current_sales_tax/100)*int(temp_list[1])
        final_price = sales_tax_amount + int(temp_list[1])
        output_string = (f"\n{temp_list[0]},{temp_list[1]},{current_sales_tax},{final_price},{temp_list[2]}")
        output_list.append(output_string)

print(output_list)
file_output = open('Output1.csv',mode='w')
file_output.writelines(output_list)