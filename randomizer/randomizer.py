import random 
#band name pseudocode:
#make three lists: one of articles, one of adjectives, and one of nouns
#from each of these lists, pick a random integer
#take the integer and match its value to an item on the list
#print the list items as one string 

article_list = ['The ', 'Some ', 'Very ', 'Those ', ' ']
adjective_list = ['Acidic ', 'Agonizing ', 'Angelic ', 'Anxious ', 'Basic ', 'Burning ', 'Bitter ', 'Black ', 'Bold ', 'Beautiful ', 'Calm ', 'Chubby ', 'Colorful ', 'Dark ', 'Deep ', 'Delicious ', 'Devious ', 'Elderly ','Luminous ',]
noun_list = ['Dancers', 'Cheetas', 'Ladies', 'Men', 'Bikers', 'Trees', 'Cacti', 'Pineapples', 'Grasshoppers', 'Apples', 'Doggos', 'Computers', 'Stars']

article=random.randint(0, len(article_list)-1)
adjective=random.randint(0, len(adjective_list)-1)
noun = random.randint(0, len(noun_list)-1)

def band_name():
	print(article_list[article] + adjective_list[adjective] + noun_list[noun])


#menu pseudocode:
#make four lists: two for adjectives, one for food items, and one empty one that will become the menu itself
#from each of the first three lists, pick a random integer
#take the integer and match its value to an item on the list 
#create a string of said items, and append them to the empty menu list; repeat 10 times
#print list, numbering it 

menu_adj = ['Spicy ', 'Delicious ', 'Sweet ', 'Tasty ', 'Cold ', 'Fragrant ']
menu_adj2 = ['Chinese ', 'Orange ', 'Jasmine ', 'Filipino ', 'Cheesy ']
menu_food = ['Rice', 'Steak', 'Chicken', 'Salad' ]
menu_item = []

for i in range(10):
	adj1 = random.randint(0, len(menu_adj)-1)
	adj2 = random.randint(0, len(menu_adj2)-1)
	food = random.randint(0, len(menu_food)-1)
	menu_item.append(menu_adj[adj1] + menu_adj2[adj2] + menu_food[food])

def menu():
	for number, letter in enumerate(menu_item):
		print(number + 1, letter)	

#haiku pseudocode:
#make two lists: one for 5 syllable phrases, the other for 7 syllable phrases
#pick a random integer from both lists, but randomize the first one twice
#print each line of the haiku, matching the value of the integer to its equivalent in the list
#repeat last two steps 3 times with a loop

haiku5 = ['petals slowly fall', 'the blue river flows', 'trees are mostly green', 'small budding flowers', 'the colorful dreams', "dew drops form on grass"]
haiku7 = ["don't you love the smell of grass?", "a breeze carries a fresh scent", "the frog hops off of his rock", "falling softly from the tree",]

def haiku():
	for i in range(3):
		line1 = random.randint(0, len(haiku5) - 1)
		line2 = random.randint(0, len(haiku7) - 1)
		line3 = random.randint(0, len(haiku5) - 1)
	
		print(haiku5[line1])
		print(haiku7[line2])
		print(haiku5[line3])
		print("")
	

print("Band Name:")	
band_name()
print(" ")
print("Menu:")
menu()
print(" ")
print("Haiku:")
haiku()

