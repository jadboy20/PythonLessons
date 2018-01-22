# WhoGoesFirst?
# In this lesson we will learn about order of operations or operation
# precedence.
#
# What is order of operation? If you remember from your math classes
# if given this expression...
# 								1 + 3 * 3
# which operation would you do first?
# Thats right! The multiplication i.e. 3 * 3. This is part of the rules
# that is setup by maths.
# 
# We will go through some expressions and see how order of operations
# can affect our mathematical expressions. 
#
# Lets Go!

def main():
	# This is the order from strongest to weakest operations. 
	# Strongest means you perform them first. Weakest means you perform 
	# them last. 
	#
	# Strongest: Multiplication and Division.
	# Weakest: Addition and Subtraction. 
	#
	# Lets see some examples. 
	# 
	# Example 1:
	answer = 2 + 3 * 5
	print("Example 1:\n============")
	print("2 + 3 * 5 = " + str(answer))
	
	# Example 2: 
	answer = 2 * 10 / 4
	return 0
	
if __name__ == "__main__":
	import sys
	sys.exit()
