

def main():
	#Your code goes here	
		
	firstname = input("What is your name?")
	lastname = input("What is your last name?")
	age = input("What is your age?")
	haircolour = input("What is your haircolour?")
	eyecolour = input("What is your eyecolour?")
	shoes = input("What is the brand of your shoes?")
	dogsname = input ("What is the name of your dog?")
	#This is a bonus one:)
	personality = input ("What is your personality?")

	print(   " Hi my name is " + str(firstname) + " and my last name is " + str(lastname)    )
	print (     " i am " + str(age) + " ,and my haircolour is " + str(haircolour)  )
	print (" ,my eyecolour is " + str(eyecolour) + " ,my brand of shoes are " + str(shoes) )
	print (" ,dog's name is" + str(dogsname) + " and my personality is" + str(personality) ) 
	
	
	
	
	 
	
	
	
	return 0

	
if __name__ == "__main__":
	import sys
	main()
	sys.exit()
