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

def multiplication_table(number):
    multiplier = 1
    while multiplier <=25:
        result =  number * multiplier
        if result > 25:
            break
        print(str(number) + "x"+ str(multiplier)+ "=" + str(result))

        multiplier = multiplier + 1
multiplication_table(3)
    