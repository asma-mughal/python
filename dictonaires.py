# movie ={
#     'title':'Life of Brain',
#     'year': 9988,
#     'cast': ['Terry', 'Eric', "Georage"]

# }
# print(movie['title'])
# print(movie.get('title'))
# print(movie.get('budget', 'Not found'))
# movie['title'] = "The Holy Grail"
# print(movie)
# movie['budget'] = "New budget"
# print(movie)
# movie.update({
#     'ratings': 8,
#     'Famous':True

# })
# print(movie)
# #del movie['year']
# year = movie.pop('year')
# print(movie)
# print(len(movie))
# print(movie.keys())
# print(movie.values())
# print(movie.items())
# for key, value in movie.items():
#     print(key, value)
# python = {'John':35,
#           'Eric':36,
#           'Michael':35,
#           'Terry':38,
#           'Graham':37,
#           'TerryG':34}
# holy_grail = {'Arthur':40,
#               'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
# life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

# #memeberShip test
# print('arthur' in holy_grail)
# #concatate Dict together
# people = {}
# people1 = {}
# people2 = {}
# people.update(python)
# people.update(holy_grail)
# people.update(life_of_brian)
# #method 2 comprehension
# for groups in (python, holy_grail):
#     people1.update(groups)
# print(sorted(people1.items()))
# #method 3 unpacking
# people2 = {**python, **holy_grail}
# print(sorted(people2.items()))
# print('The sum of the ages', sum(people.values()))

# freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
# antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
# pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}
# cart ={}
# purse=1000
# for shop in freelancers, antiques:
#     buy_items = input(f"Welcome to shop {shop['name']} Enter the thing you want to buy, type(exit to exit store):")
#     if buy_items=="exit":
#         continue
#     if buy_items not in shop:
#         continue
#     else:
#         cart.update({buy_items: shop.pop(buy_items)})
# total_cost = sum(cart.values())
# print(f"You Total is : {total_cost} and your change is {purse -total_cost }")
# def email_list(domains):
#     emails=[]
#     for key, items in domains.items():
#         for item in items:
#             string_append = f"{item}@{key}"
#             emails.append(string_append)
#     print(emails)
    


# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	# Go through group_dictionary
# 	for key, items in group_dictionary.items():
# 		for item in items:
# 			if item in user_groups:
# 				user_groups[item].append(key)
# 			else:
# 				user_groups[item] = [key]
# 	return(user_groups)


# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))


# wardrobe= {'shirt': ['red', 'blue', 'white'], 'jeans':['blue', 'black']}
# new_items= {'jeans':['white'], 'scarf': ['yellow'],'socks':['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)
# def add_prices(basket):
# 	total = 0
# 	for key, values in basket.items():
# 		total += values
# 	# Limit the return value to 2 decimal places
# 	return round(total, 2)  

# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
# 	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

# print(add_prices(groceries)) # Should print 28.44

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):
    print((c*thickness).ljust(thickness*2)+(c*thickness).rjust(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness*2)+(c*thickness).ljust(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).center(thickness*6))