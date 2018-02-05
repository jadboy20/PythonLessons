# 01_defs.py
# 
# Functions always start with a def. 
# Did you know the main thing you see at the start is a function?
# Notice the def?

def main():


	
	
	return 0
		
def add(a, b):
	return a + b
	
def ph():
	print("Hello")
	
def blahblahblah(first , second):
	return first * second
	
def reply():
	name = input("Whats your name? ")
	print("Hello " + str(name))
	
	
def aboutMe():
	# Your code goes here:
	
	firstname = input("What is your first name? ")
	lastname = input("What is your last name? ")
	age = input("What is your age? ")
	haircolour = input("What is your hair colour? ")
	shoes = input("What is your brand of shoes? ")
	eyecolour = input("What is your eye colour? ")
	dogsname = input("What is your dogs name? ")
	
	print("My name is " + str(firstname) + " " + str(lastname) + " and I am " + str(age) + " years old.")
	print("I have " + str(haircolour) + " hair and have " + str(eyecolour) + " eyes.")
	print("I have " + str(shoes) + " shoes and my dogs name is " + str(dogsname))
	
	
def calculateAreaOfSquare(Width , Length):
	return Width * Length
	
	
if __name__ == "__main__":
	import sys
	main()
	
	sys.exit()

