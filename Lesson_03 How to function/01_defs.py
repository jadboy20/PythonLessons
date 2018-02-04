# 01_defs.py
# 
# Functions always start with a def. 
# Did you know the main thing you see at the start is a function?
# Notice the def?

def main():
	
	# Did you know "print" is a function.
	print("I am a function!")
	
	# "Input" is a function too!
	i = input("I'm a function?")
	
	# You can make youre own functions. 
	result = add(2,3)
	print(result)
	
	# You use functions to perform tasks that you will use many times. 
	# For instance, maybe you want to print "Hello" 20 times. 
	# Instead of writing print("hello") print("hello").... you could make a function
	# called ph() which prints hello. Lets have a look!
	ph()
	ph()
	ph()
	ph()
	ph()
	ph()
	ph()
	ph()
	ph()
	ph()
	
	# See how much writing we saved??
	
	# Try your own function below. 
	
	return 0
		
def add(a, b):
	return a + b
	
def ph():
	print("Hello")
	
if __name__ == "__main__":
	import sys
	main()
	
	sys.exit()

