a = 8
b = 9
print(a == b)
print(a!=b)
print(a < b)
print(a > b)
print ('o' in 'John')
a = [1,23,4]
b = [1,23,4]
print( a == b) # here numbers are being checked
print(a is b ) # here ids are being checked 
print (id(a), id(b)) ## memory of 2 of them are same in computer that's why they are same.
print(42 + False) #automatic conversion
print(42 + True)  #automatic conversion
is_raining = False
is_cold=True
print("Bad Morning")
if is_raining and is_cold:
    print("Bring umbrella or jacket or both")
elif is_raining and not(is_cold): #if  raning but not cold
    print("Bring Umbrella")
elif not(is_raining) and (is_cold): #if  raning but not cold
    print("Bring Jacket")   
else:
    print("Shirt is Fine")

amount = 10
if amount<=50:
    print("Purchase approved")
else:
    print("Please enter your pin")

print("Welcome to Calculator")
def calculator_excercise(op, num1, num2):
 result = 0
 if(op == '+'):
    return num1+num2
 elif(op == '-'):
     return num1 - num2
 elif(op == '*'):
     return num1 * num2
 elif(op == '/'):
     return num1 / num2
 elif(op == 'f'):
     result = (num1*9/5) + 32
     return result
 else:
     return "Input error"


# a = float(input("Please enter First Number: "))
# b = float(input("Please enter Another Number: "))
# c = input("Enter operation (+  , - , * , /): ")
# print("Your result is:" , calculator_excercise(c, a, b))
     
def num_days(month):
    days = 31
    if month == 'feb':
       days = 28
    elif month == 'apr' or month == 'jun' or month == 'sep'or month == 'nov':
        days = 30
    print(f"The number of days in {month} is {days}")

num_days('nov')
print((2**2) == 4)
number = 10
if number > 11:
    print (0)
elif number!=10:
    print(1)
elif number >=20 or number <12:
    print(2)
else:
    print(3)
print(9999+8888)
print(100 *100)
def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = filesize % block_size
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    else:
        return block_size * full_blocks
print(calculate_storage(1)) #should be equal to 4096
print(calculate_storage(4096))#should be equal to 4096

print(calculate_storage(4097))#should be equal to 8192

print(calculate_storage(6000))#should be equal to 8192
