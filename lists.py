# #All built-In Functions of List
# friends = ["Michael", "John", "Terry", "eric", 1, True]
# print(friends[2:4])
# print(len(friends))
# print(friends.index(True))
# print(friends.count('Eric'))
# #you cannot sort different datatypes
# life = ["Failure", "Short", "Tuff", "Depressed"]
# another_life = ["Sedness", "Alone"]
# # (life.sort())
# # print(life)
# # print(life.sort(reverse=True))
# # print(life)
# print(life.reverse())

# print(life)
# print(max(life))
# #Modifying Lists
# life.append("Patience")
# print(life)
# life.insert(2, "ANGER")
# print(life)
# life[3]= "Most Tuff"
# print(life)
# life.extend(another_life)

# print(life)
# #remove, pop, delete
# life.pop(-1)
# print(life)

# life.clear()
# print(life)
# del life #I AM DED

# #Copying lists
# # new_life = friends[:]
# # print(new_life)
# # new_friends = list(friends)
# # number_of_sold_week1 = [12, 34, 67,89]
# # number_of_sold_week2 = [14,5,1,2,9]
# # sales =[]
# # another_day = int(input("Enter sales for another day: "))
# # number_of_sold_week2.append(another_day)
# # print(number_of_sold_week2)
# # sales.extend(number_of_sold_week1)
# # sales.extend(number_of_sold_week2)
# # print("Worst Day: " ,min(sales))
# # print("Best Day: ", max(sales))
# print("Total: " ,sum(sales))
# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# new_filenames=[]
# count = 0
# for file in filenames:
#     if ".hpp" in file:
#         new_string = file.replace('.hpp', '.h')
#         new_filenames.append(new_string)
        
#     else:
#         new_filenames.append(file)
    
# print(new_filenames)
# animals = ["lion", "zebra", "dolphin"]
# for index, animal in enumerate(animals):
#     for index2, chars in enumerate(animal):
#         print(index2, chars)
# def pig_latin(text):
#   say = "ay"
#   words = text.split() 
#   new_word_list = []
#   for word in words:
#     new_word = word[1:] + word[0] +say
#     new_word_list.append(new_word)
#   result = " ".join(new_word_list)
#   return result
		
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
my_2D_list= []
another_list = []
unique_grade = set()
name_list = []
N = int(input("Enter a number: "))
for item in range(N):
        name = input()
        score = float(input())
        student_data = [name, score]   
        my_2D_list.append(student_data)
for row in my_2D_list:
    for element in row:
         if not isinstance(element, str):
            another_list.append(element)
         else:
              name_list.append(element)
              