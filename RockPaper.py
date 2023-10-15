import random
user_score =0
comp_score = 0
options = ["Rock", "Paper", "Scissors"]
while True:
    user_input = input("Input for Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == 'q':
        break
    random_number = random.randint(0,2)
    print(random_number)
    #rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print(f"Computer Picks: {computer_pick}")
    if user_input == "rock" and computer_pick == "scissors":
        user_score= user_score + 1
        print("You won")
        continue
    elif user_input == "paper" and computer_pick == "paper":
        print("Tie Match")
    elif user_input == "scissor" and computer_pick == "scissor":
        print("Tie Match")
    elif user_input == "rock" and computer_pick == "rock":
        print("Tie Match")
    else:
        print("Computer Won")
        comp_score = comp_score + 1
        continue

print(f"Computer score is {comp_score} and Your Score is {user_score}")







