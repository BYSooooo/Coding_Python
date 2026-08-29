# Dicts

# Basic Structure
# Dictionary is allow difference type of each value
player = {
    'name' : 'nico', # string
    'age' : 12, # number
    'alive' : True  # boolean
}

# get()
player_age = player.get('age')
print(player_age)

# add list in dict
player2 = {
    'name' : 'nico',
    'age' : 12,
    'alive' : True,
    'fav_food' : [ '🍕', '🍔' ]
}

# Get Value using get()
fav_food_get = player2.get('fav_food')
print(fav_food_get)

# Get Value directly
fav_food_more = player2['fav_food'] 
print(fav_food_more)

# Method - pop
player3 = {
    'name' : 'nico',
    'age' : 12,
    'alive' : True,
    'fav_food' : [ '🍕', '🍔' ]
}
player3.pop('age')
print(player3)

# Add Key-Value
player4 = {
    'name' : 'nico',
    'age' : 12,
    'alive' : True,
    'fav_food' : [ '🍕', '🍔' ]
}

player4['xp'] = 1500
print(player4)

# Add Value in list value in dict
player5 = {
    'name' : 'nico',
    'age' : 12,
    'alive' : True,
    'fav_food' : [ '🍕', '🍔' ]
}

player5['fav_food'].append('🧅')
print(player5['fav_food'])