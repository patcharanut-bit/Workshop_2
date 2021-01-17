# Loop Dictionary items
# EX 1
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key in thisdict:
    print(key)

#Output
# brand
# model
# year

# EX 2
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key in thisdict:
    print(thisdict[key]) # Ford \n Mustang \n 1964

# EX 3
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key in thisdict.keys():
    print(key) # brand \n model \n year

# EX 4
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for value in thisdict.values():
    print(value) # Ford \n Mustang \n 1964

# EX 5
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key, value in thisdict.items():
    print(key, value) # brand Ford \n model Mustang \n year 1964