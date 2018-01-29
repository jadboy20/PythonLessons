# BasicMath
# In this lesson we will learn about some math operations we can do 
# with Python. This is without any imported libraries. Some information
# was taken from:
# - www.tutorialspoint.com/python/python_basic_operators.htm 
# 
# Go to the website if you want to read up more about this. 
#
# As you have learned from school, there are a few operators, but the 
# main ones are:
#
# Operator            | Symbol
# ==============================
# - Addition          |   + 
# - Subtraction       |   -
# - Multiplication    |   *
# - Division          |   /   
# 
# There are some other ones, but we will look at them later on. 
#

def main():
	# Lets go through all the operators mentioned above.
	# We will use the PRINT feature and variables from the previous 
	# lesson to display our answers. Lets start!
	#
	# Addition
	# ====================
	# We can add two numbers together and store them in a variable.
	answer = 1 + 1
	print(answer)
	
	# We can add three numbers together and store them in a variable.
	answer = 1 + 1 + 1
	print(answer)
	
	# Infact we can add as many numbers as we like!!
	answer = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
	print(answer)
	
	# We can do the same with subtraction... 
	answer = 5 - 1 - 1 - 1 - 1 - 1
	print(answer)
	
	# and multiplication...
	answer = 2 * 2 * 2 * 2 * 2
	print(answer)
	
	# and division
	answer = 10 / 5 / 2
	print(answer)
	
	# We can also combine them all!
	answer = 5 + 3 - 3
	print(answer)
	
	# Try make your own ones and print them! VV
	# Write your code under here...:a
	answer = 6 + 5 * 1 - 1 / 5 
	print(answer)
	
	answer = 5 + 5 * 6 / 5 - 2
	print(answer)
	
	answer = 2 ** 5
	print(answer)
	return 0
	
if __name__ == "__main__":
	import sys
	main()
	sys.exit()
