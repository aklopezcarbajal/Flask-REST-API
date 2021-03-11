import requests

BASE = "http://127.0.0.1:5000/"

data = [
	{'name': 'Muffy', 'species': 'Sheep', 'personality': 'Sisterly', 'quote': "There's a black sheep in every family."},
	{'name': 'Rocket', 'species': 'Gorilla', 'personality': 'Sisterly', 'quote': "Art feeds the soul. So does pizza."},
	{'name': 'Bud', 'species': 'Lion', 'personality': 'Jock', 'quote': "You're not living unless you're sweating!"},
	{'name': 'Jitters', 'species': 'Bird', 'personality': 'Jock', 'quote': "When you're a team of one, you're always captain!"},
	{'name': 'Lucha', 'species': 'Bird', 'personality': 'Smug', 'quote': "Birds of a feather, et cetera, et cetera..."},
	{'name': 'Raymond', 'species': 'Cat', 'personality': 'Smug', 'quote': "Stay on brand!"},
	{'name': 'Molly', 'species': 'Duck', 'personality': 'Normal', 'quote': "Like water off a duck's back."},
	{'name': 'Lily', 'species': 'Frog', 'personality': 'Normal', 'quote': "Don't jump to conclusions!"},
	{'name': 'Peanut', 'species': 'Squirrel', 'personality': 'Peppy', 'quote': "Never take a nibble when you can take a bite."},
	{'name': 'Sprinkle', 'species': 'Penguin', 'personality': 'Peppy', 'quote': "Frosting is just the icing on the cake."}
]

#add elements to the database
for i in range(len(data)):
	response = requests.put(BASE + "villager/" + data[i]['name'], data[i])
	print(response.json())