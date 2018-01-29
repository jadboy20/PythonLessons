def main():
	# Your code goes here:
	
	print("This program can add two numbers toether")
	# To get user input you use the function "input("Question")"
	number1 = input("Whats your first number? ")
	number2 = input("Whats your second number? ")
	
	answer = float(number1) + float(number2)
	print("The answer is: " + str(answer))
	
	
	return 0
	
	
if __name__ == "__main__":
	import sys
	main()
	sys.exit()

