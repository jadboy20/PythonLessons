# 02_return_something.py
# 
# Functions sometimes need to return something. If you have a function
# that requires information, then you will need to use arguments. 


def main():
	
	IsThisYourNumber()
	
	# Try making your own function that returns something. 
	return 0

def IsThisYourNumber():
	print("Think of a number between 1 and 10");
	Pause()
	print("Add 4")
	Pause()
	print("Times 8")
	Pause()
	print("Divide by 4")
	Pause()
	print("Subtract the number you started with")
	Pause()
	answer = input("Is your number 2? [Y/N]")
	if(str(answer) == "Y"):
		print("YAY")
	else:
		print("NO!")
	
def Pause():
	input(" ")
if __name__ == "__main__":
	import sys
	main()
	
	sys.exit()


