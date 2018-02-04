# 02_return_something.py
# 
# Functions sometimes need to return something. If you have a function
# that requires information, then you will need to use arguments. 


def main():
	
	# The print function needs an argument. THe argument is the string
	# you put in it.
	print("I am an argument")
	
	# This function returns stuff!
	a = subtract(10, 2)
	print(a)
	
	# Try making your own function that returns something. 
	return 0

def subtract(a, b):
	return a - b
if __name__ == "__main__":
	import sys
	main()
	
	sys.exit()


