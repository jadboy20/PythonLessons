# 03_Conditions.py
# 
# You remember how we used TRUE and FALSE? These are just TWO types of 
# MANY conditions we can use. 
#
# With an IF statement condition, as long as the condition you have provided
# is TRUE, then the code in the IF statement will run. Then we can 
# use the ELSE for anything else.
#
# This technique is used for:
# - Checking passwords are correct
# - Checking if your character has hit the ground in a game.
# - Use in your controllers for Minecraft to see if you are walking forward
#   , backward, left, right or anything else. 
# 


def main():
	
	# To make the statement,we will need these comparison operators:
	# == : Equals
	# != : Not Equals
	# >  : Greater than
	# <  : Less Than
	# >= : Greater than or equal to.
	# <= : Less than or equal to 
	# 
	# Lets try the equals one with something we know is true.
	
	if 1==1: 
		print("This is true")
	else:
		print("This is false")
		
	# Lets try something that we know is false. 
	
	if 1 == 2:
		print("This is true")
	else:
		print("This is false")
		
	# What is going to print?
	
	# Lets try a greater than one.
	
	if 2 > 1:
		print("This is true")
	else:
		print("This is false")
	
	# Try your own below. 
	
	# Try write a function that simplifies the above stuff...
	# Call the function "TrueOrFalse()" where the argument is the 
	# Condition...
	
	
if __name__ == "__main__":
	import sys
	main()
	
	sys.exit()
