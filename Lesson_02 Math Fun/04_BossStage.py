def main():
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
	
	return 0
	
	
if __name__ == "__main__":
	import sys
	main()
	sys.exit()

