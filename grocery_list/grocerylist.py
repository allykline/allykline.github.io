#pseudocode
#make a grocery list dictionary
#set the grocery list name via input
#make a menu page, where you can add, delete, or update the items, or finish the program
#make a while loop 
print("Hi! Make a list!")
grocery_list = {}
done = False

def name_list():
	list_name = input("Enter the name of your list here: ")
	#return(list_name)
	#grocery_list["name"] = list_name

def add_item():
	add = input("What item would you like to add? ")
	grocery_list[add] = 1

def delete_item():
	delete = input("What item would you like to delete? " )
	del grocery_list[delete]

def update_item():
	update = input("What item would you like to change? ")
	update_val = input("What value do you want to change it to? ")
	grocery_list[update] = int(update_val)

def print_list():
	#print(list_name)
	print(grocery_list)

name_list()

options = ""
done = False
while not done:
	options = input("Would you like to add, delete, or update an item, or finish? ") 
	if options == "add":
		add_item()
	elif options == "delete":
		delete_item()
	elif options == "update":
		update_item()
	elif options == "finish":
		print_list()
		done = True
	else:
		print("Error! Try Again")

print("You're done with the program!")

