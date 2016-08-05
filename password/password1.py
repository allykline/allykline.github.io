from hashlib import *

login_dict = {}

#pseudocode create an empty dictionary to become the place where passwords are stored. 
#create kind of a homepage, where a user can create an account, log in, or leave the program
#need three methods, one to create an account, one to log into account, and one for the homepage
#for the homepage, have user input options for creating/logging in/leaving then call the methods for the first to, quit for the third
# for the method to make a hash, have user input a username and password; then encode and hash the password-- then save the user name as a dictionary key, and the hashed password as its value, then return to homepage
#for the method to log in, also make inputs for a username and a password, then hash the password using the same process as the account creation method
#make the computer check if the username is in the dictionary, and then check if the password matches the value of the username key
#if they both match, print a welcome message, if the username is in the dictionary, but the hashed password doesn't match, print an error message. If neither of the items match, prompt user to make account

def new_account():
	username = input("Enter a username: ")
	password = input("Enter a password: ")
	hash_password = make_hash(password)
	login_dict[username] = hash_password



def make_hash(password):
	return sha256(password.encode('utf-8')).hexdigest()
	

	
def login():
	username = input("Enter your username: ")
	password = input("Enter your password: ")
	password = make_hash(password)
	if username in login_dict and login_dict[username] == make_hash(password):
		print("Welcome, " + username + "!")
	elif username not in login_dict:
		create_user = input("This user isn't in our database. Would you like to create an account? (Enter 'yes' or 'no'): ")
		if create_user == "yes":
				new_account()
		elif create_user == "no":
			print("Okay. We won't create an account for you.")
	elif login_dict[username] != password:
		print("Sorry, that isn't your password! Please try again.")
		x = 2
		for i in range(3):
		 print("You have " + str(x + 1) + " attempt(s) left.")
		 password = input("Enter your password: ")
		 if password == make_hash(password):
		 	print("Welcome, " + username + "!")
		 	break
		 elif password != make_hash(password):
		 	x = x-1


		print("Get out of " + username +"'s account!")
		
def prompt():
	start_up = "3"
	while start_up != "0":	
		start_up = input("Hi! Press 1 to log in, 2 to create a new account, or 0 to exit the program: ")
		if start_up == "1":
			login()
		elif start_up == "2":
			new_account()
		elif start_up == "0":
			quit()

prompt()

