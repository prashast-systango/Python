# Decorator
def world(fun):
    print("World")
    def India():
        print("India")
        fun()
        print("Indore")
    India()

def MP():
    print("Madhya Pradesh")

newWorld = world
newWorld(MP)



#1
# can be treated as objects
def shout(text):
	return text.upper()

# print(shout('Prashast'))
yell = shout # now yell will act as shout 
# print(yell('Prashast'))



#2 Functions can be passed as arguments to other functions
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am Prashast.""")
	# print (greeting)

# Passing functions as arguement in another function
greet(shout)
greet(whisper)
print()



#3
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)
add_2000 = create_adder(2000)

# print(add_15(10))
# print(add_2000(21))
