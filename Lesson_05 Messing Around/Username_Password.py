
# I am a global variable. 

# These usernames are going to be Global Variables. 
# They are the ones we are comparing to these passwords. 
USERNAME = "Jadboy20"
PASSWORD = "SillyMan"

def main():
	# THis program I am going to ask the user to input their password and username.
	# They must get BOTH correct to go on. 
	
	input_username = input("Enter your username: ")

	
	if str(input_username) == USERNAME:
		print("User name is correct!!")
		
		# I put user pass word here!
		input_password = input("Enter your password: ")
		
		if str(input_password) == PASSWORD:
			print("Password is correct!!")
			print("Welcome Jadboy20!")
		else:
			print("Password is incorrect!")
	else:
		print("User name does not exist!")
	
	input("Press enter to exit...")


	
	
if __name__ == "__main__":
	import sys
	main()
	sys.exit()
	print(variable)
	
