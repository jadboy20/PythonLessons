# Variables.py
# In this lesson we will be learning about Variables. 
#
# Variables in programming are objects that you can store information 
# in. They can be called in the program and have information put in 
# them or read from them. Think of them like a container. You can put 
# something in the container. You can also open the container and see
# whats inside it. You can transfer the contents of the container to 
# another container. 
# 
# Variables are one of the main building blocks of 
# programming. Lets try to use them. 

def main():
	# Lets make a variable that contains the message "I am a variable."
	# We can call the variable whatever we want for now. 
	var = "I am a variable."
	
	# Now we can do things with this variable. Lets try print it. 
	# To print the variable, we just simply type "print" and then put
	# the variable inside the print function. 
	print(var)
	
	# Now lets put another message in the variable. Lets see what
	# happens.
	var = "I am a different message"
	print(var)
	
	# Notice how the variable contents changed? This means that all the 
	# contents were replaced with the new message. 
	
	# You can also store numbers in the variables. Not just messages. 
	newvar = 10
	print(newvar)
	
	newvar = 10.5
	print(newvar)
	
	# You can also copy the contents of a variable to another variable.
	original = 5
	varcopy = original
	original = 3
	varcopy = original
	print(original)
	print(varcopy)
	
	# Variables naming must follow rules. The rules are:
	# - Do not start with a number: 01variable
	# - Make sure that variable names relate to what is storing. If you 
	#   are storing temperature readings in the variable call it names 
	#   like:
	#	o temperature
	#   o temp
	#   o tempReading
	#  
	#   NOT 
	#   x atuhaeu
	#   x eeeeeee
	
	return 0
	
if __name__ == "__main__":
	import sys
	main()
	sys.exit()
