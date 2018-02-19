def main():
	# Your code goes here:
	inputpassword = input("Enter your password:")
	
	
	
	
	if str(inputpassword) == "Laugh@Life":
		print("Access Succesful")
	
	else:
		print("Incorrect Password")		
		
	# Add a blocking function. 
	input("Press enter to exit...")
	
if __name__ == "__main__":
	import sys
	main()
	sys.exit()
