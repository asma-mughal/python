# while condition:
#     code
# #     iterator
# Loops question :
# 1. What do I want to repeat?
# 2. What do I want to change each time?
# 3. How long should we repeat
# i =0
# while(i<5):
#     print(f"{i}."+ "*" *i + "Loops are awesome" + "*" * i)
#     i = i + 1
# j=0
# actual_number = 10
# while(j<3):
#     number = int(input(f"Guess {j} number "))
#     if(number != actual_number):
#         if(number <=10 or number >=30):
#             print("Just near the actual number")
#         elif(number <=30 or number>=50):
#             print("Oh No! You are guessing so high")
#     if(actual_number == number):
#         print("Congrats you won the Game!")
#         break
    
#     j = j + 1
# if(number !=actual_number):
#     print("You lost the game")


# def is_power_of_two(number):
#     while number % 2 ==0:
#         number = number /2
#         break
#     if(number ==1 ):
#         return True
#     return False
# print(is_power_of_two(0))
# print(is_power_of_two(1))
# print(is_power_of_two(8))
# print(is_power_of_two(9))

# def sum_divisor(number):
#     divisor = 2
#     total =0
#     if(number <1):
#         return 0
#     while divisor <= number :
#         if number % divisor==0 //2 :
#             total+=divisor
#         divisor = divisor + 1
#     return total
# print(sum_divisor(0))
# print(sum_divisor(3))
# print(sum_divisor(36))

# def multiplication_table(number):
#     multiplier = 1
#     while multiplier <=25:
#         result =  number * multiplier
#         if result > 25:
#             break
#         print(str(number) + "x"+ str(multiplier)+ "=" + str(result))

#         multiplier = multiplier + 1
# multiplication_table(3)
    
# for item in range(1,10,8):
#     print('Current Letter:',item)
# for item in range(1,10):
#     print('Current Letter:',item)
# for item in range(10):
#     print('Current Letter:',item)
# for letter in 'Norwegian blue':
#     print(letter)

# for name in ['Depressed', "Sad", "Failure", "Dissapointed"]:
#     print(name)

# work = ['Mask on', 'Watch Draama', 'Pushups', 'Gym']
# for todo in work:
#     print(todo)
# for todo in range(len(work)):
#     print(work[todo])

# friends = ['John','Terry','Eric','Michael','George']
# for friend in friends:
#     if friend == 'Eric':
#         print('Found' , friend , '!')
#         continue
#     print(friend)

# friends = ['John','Terry','Eric']
# for friend in friends:
#     for number in [1,2,3]:
#         print(friend, number)
#     print(friend)
# names= ["A", "B", "C"]
# name1 = ["D", "E", "F"]
# msg = 'you are invited to the party on Saturday'
# names.extend(name1)
# for index in range(2):
#     names.append(input("Enter another name"))
# # print(names)
# for n in range(6,18+1,3):
#     print(n*2)
# for n in range(19):
#     if n % 2==0:
#         print(n)
# for n in range(18+1):
#     print(n**2)
# for n in range(0,18+1, 2):
#     print(n*2)

# for index in range(1,11):
#     print(index**3)
# for index in range(0,100,7):
#     if index % 7!=0:
#         continue
#     else:
#         print(index)

# def sum_positive(n):
#     sum =0
#     for index in range(0,n+1):
#         sum = sum + index
#     return sum
# print(sum_positive(3))

# def sum_positive(n):
#     if n ==0:
#         return 0
#     else:
#         return n+ sum_positive(n-1)c;lkb c cvd     vhjiop;"{}?. #         return n+ sum_positive(n-1)c;lkb c cvd    
# print(sum_positive(5))

# def is_power_of(number, base):
#     if(base <=1 and number <=0):
#         return False
#     elif number %base == 0:
#         return is_power_of()
#     else:
#         return True
    

# print(is_power_of(8,2))
        

# n = int(input("Enter a number"))
# for i in range(n):
#     print(i*i)

# def is_leap(year):
#     leap = False
#     if( year % 4 ==0 and year % 100 != 0) or (year % 400 ==0):
#         leap = True
#     return leap

# year = int(input())
# print(is_leap(year))

# N = int(input("Enter number of commands: "))
# new_list = []
# for i in range(N):
#     command = input().split()  # Read the command as a list of words
#     if command[0] == "insert":
#         position = int(command[1])
#         element = int(command[2])
#         new_list.insert(position, element)
#     if command[0]=="print":
#         print(new_list)
#     if command[0] == "remove":
#         position = int(command[1])
#         new_list.remove(position)
#     if command[0] == "append":
#         element =int( command[1])
#         new_list.append(element)
#     if command[0] == "sort":
#         new_list.sort()
#     if command[0]== "pop":
#         new_list.pop()
#     if command[0] == "reverse":
#         new_list.reverse()

n = int(input())
arr = map(int, input().split())
new_set = set(arr)
sorted_arr = sorted(new_set)
print(sorted_arr[-2])

