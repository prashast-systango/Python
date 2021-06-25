# Method overloading
def add(datatype, *args):

	if datatype =='int':
		answer = 0
		
	if datatype =='str':
		answer =''

	for x in args:        		
		answer = answer + x  # operator overloading

	print(answer)

# Integer will get added
add('int', 1999, 1)

# String will get concatenated
add('str', 'Hi ', 'this ','is ','Prashast.','''\n
Nice
to
meet
you !!''')