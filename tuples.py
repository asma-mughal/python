#tuples are list but could be modified and more faster than  Lists
# friends = ['John', 'Michael', 'Terry']
# friends_tuple = ('John', 'Michael', 'Terry')
# friends_set= {'John', 'Michael', 'Terry', "Eric", "John"}
# second_friends_set = {"Crazy", "DUO","David", "Eric"}

# print(friends_set)
# #built in methods
# print(friends_set.intersection(second_friends_set))

# print(friends_set.union(second_friends_set))
# print(friends_set.difference(second_friends_set))

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
print("Eric" and "John" in friends)
print(friends.union(my_friends))
print(friends.intersection(my_friends))
print(friends.difference(my_friends))
new_cars = list(set(cars))
print(new_cars)