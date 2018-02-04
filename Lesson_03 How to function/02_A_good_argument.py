# 02_A_good_argument.py
# 
# Functions need arguments sometimes. Arguments are things you can pass
# to function for it to use inside it. 

def main():
	
	# The print function needs an argument. THe argument is the string
	# you put in it.
	print("I am an argument")
	
	# Here is an argument that needs two arguments.
	a = subtract(10, 2)
	print(a)
	
	# Try making your own function with an argument or so.
	return 0

def subtract(a, b):
	return a - b
if __name__ == "__main__":
	import sys
	main()
	
	sys.exit()


