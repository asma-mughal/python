# def greeting(name, age=12):
#     print(f'hellow friend {name} you are {age} !')
 
# user_name = input("enter your name ")
# greeting(user_name)

# def greeting(name, age=28, color="red"):
#     new_age = int(age) + 1
#     print('Hello '  +  name + ', you will be ' + str(new_age) + ' old next birthday !')
#     print(f'Hello {name}, you will be {new_age} old next birthday !')
#     print(f'We hear you like the color {color}')

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# fav_color = input("Enter your favourite color: ")
# greeting(name, age, fav_color)
def value_added_tax(amount):
    tax = (amount * 0.25)
    total_amount = amount * 1.25
    return f" {tax}, {total_amount}, {amount}"
return_value = value_added_tax(100)
print(return_value)
