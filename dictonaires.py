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
python = {'John':35,
          'Eric':36,
          'Michael':35,
          'Terry':38,
          'Graham':37,
          'TerryG':34}
holy_grail = {'Arthur':40,
              'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

#memeberShip test
print('arthur' in holy_grail)
#concatate Dict together
people = {}
people1 = {}
people2 = {}
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
#method 2 comprehension
for groups in (python, holy_grail):
    people1.update(groups)
print(sorted(people1.items()))
#method 3 unpacking
people2 = {**python, **holy_grail}
print(sorted(people2.items()))
print('The sum of the ages', sum(people.values()))

freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}
cart ={}
purse=1000
for shop in freelancers, antiques:
    buy_items = input(f"Welcome to shop {shop['name']} Enter the thing you want to buy, type(exit to exit store):")
    if buy_items=="exit":
        continue
    if buy_items not in shop:
        continue
    else:
        cart.update({buy_items: shop.pop(buy_items)})
total_cost = sum(cart.values())
print(f"You Total is : {total_cost} and your change is {purse -total_cost }")
