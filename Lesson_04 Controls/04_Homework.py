
def main():
	if "hello" == "hello":
		print("This is true")
		
	inputpassword = input("Enter your password: ")
	print(str(inputpassword))
	
	inputstuff = input("Enter the word \"Hello\": ")
	
	if str(inputstuff) == "James123":
		print("Good spelling!!!")
	else:
		print("What are you? 3 years old??")
	
	
if __name__ == "__main__":
	import sys 
	main()
	sys.exit()
