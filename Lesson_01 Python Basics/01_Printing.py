# Printing.py
# This lesson will show you how to print to the standard output.
# Standard output is any output that the program will normally print to.
# In this case, it will be the command window that the program is run 
# from. 
#
# We will use this to write some messages to the standard output.


def main(args):
	# You type first, "print(" and then the message in between. 
	# Make sure that the message is in Quotation marks. 
	print("Hello, world!")
	
	# Now write your own message under here VV
	print("How are you?") 
	
	print("Good,Thanks")
	
 

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
