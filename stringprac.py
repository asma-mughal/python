msg = "Welcome to learn"
#0123435..
print(msg + " " + msg)
print (msg * 2)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(len(msg))
print(msg.count('a')) #case sensitive method
print(msg[:7])
#slicing the strings
print(msg[7])
print(msg[-1]) #give the last number
test_msg = "Welcome to Python 101: Strings"
result = (test_msg[18] +" " +test_msg[0:7] +" " +test_msg[25:29] +" " + test_msg[8:11] + test_msg[8] + test_msg[12] + test_msg[2] + test_msg[6]+ test_msg[25])
print(result.title())
print(result[::-1])
# another_msg = """Dear Terry,,
# You must cut down the mightiest 
# tree in the forest with…
# a herring"""
# print(another_msg)
print(msg.replace('W', 'MIO'))
print(msg)
#strings are immutable
#memebership
print('welcome' in msg) #case sensitive
print('Failure'not  in msg)
name = "TERRY"
color = "RED"
msg1 = f'{name.capitalize()} loves the color {color.lower()}'
print(msg1)