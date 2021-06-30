class InputClass:
    # Input File Should be in format
    # Product-Name(eg:Notebook), Product-CostPrice(100), Product-SalesTax-Percentage(20), Country(India)
    file_input = open('Input3.csv',mode='r')
    # Input File Content
    input_data = file_input.read()
    file_input.close()