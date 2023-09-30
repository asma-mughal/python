# while condition:
#     code
# #     iterator
# Loops question :
# 1. What do I want to repeat?
# 2. What do I want to change each time?
# 3. How long should we repeat
i =0
while(i<5):
    print(f"{i}."+ "*" *i + "Loops are awesome" + "*" * i)
    i = i + 1
j=0
actual_number = 10
while(j<3):
    number = int(input(f"Guess {j} number "))
    if(number != actual_number):
        if(number <=10 or number >=30):
            print("Just near the actual number")
        elif(number <=30 or number>=50):
            print("Oh No! You are guessing so high")
    if(actual_number == number):
        print("Congrats you won the Game!")
        break
    
    j = j + 1
if(number !=actual_number):
    print("You lost the game")