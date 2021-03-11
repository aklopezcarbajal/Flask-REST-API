import requests


BASE = "http://127.0.0.1:5000/"

hopper = {'name': 'Hopper', 'species': 'penguin', 'personality': 'Cranky', 'quote': "Always have a comeback."}

#Add new villager
#response = requests.put(BASE + "villager/" + 'Hopper', hopper)
#print(response.json())
#input()

#get a specific element
response = requests.get(BASE + "villager/Hopper")
print(response.json())

#modify an element
response = requests.patch(BASE + "villager/Hopper", {'quote': "Hopper's new quote!"})
print(response.json())