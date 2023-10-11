
list_questions = [
   {"What color does yellow and green make" : "Lime"},
   {"A computer cannot 'boot' if it does not have the": "Operating system"},
   {"Fathometer is used to measure": "Ocean Depth"}
]
print("Hellow and Welcome, This is your general Knowledge Test, Give it a try")
score = 0
for question in list_questions:
    for key, item in question.items():
        print(f"Hellow this is a question:  {key}")
        answere = input()
        if(item.lower() == answere.lower()):
            score = score + 1   
        else:
            print("Sorry the answere was wrong")
if score == 0:
    print("Oops ! Try Again")
else:
    print(f"Well Done you have played well with score: {score}")


