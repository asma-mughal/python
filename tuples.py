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

# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}
# cars =['900','420','V70','911','996','V90','911','911','S','328','900']
# print("Eric" and "John" in friends)
# print(friends.union(my_friends))
# print(friends.intersection(my_friends))
# print(friends.difference(my_friends))
# new_cars = list(set(cars))
# # print(new_cars)
# def group_list(group, users):
#   members =  ", ".join(map(str, users))
#   return f"{group}: {members}"

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"
# def guest_list(guests):
# 	for guest in guests:
# 		name, age , occupation = guest
# 		print(f"{name} is {age} years old and works as a {occupation}")

# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])


# eng_students = int(input())
# eng_roll_numbers = set(map(int, input().split()))
# fren_students = int(input())
# fren_roll_numbers = set(map(int, input().split()))
# union_of_roll_numbers = eng_roll_numbers.intersection(fren_roll_numbers)
# print(len(union_of_roll_numbers))
N = int(input())
space_integers = list(map(int, input().split()))
print(space_integers)
if(all(space_integers) and any(space_integers)):
    print("True")
