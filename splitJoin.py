# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# #CONVERT STRING -> LIST (SPLIT)
# print(msg.split())
# print(csv.split(','))
# #CONVERT LIST -> STRING (JOIN)
# print(','.join(friends_list + csv.split(',')))
# print(' '.join(msg.split(' ')))

# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = ['Exercise: fill me with names']
# new_string = (''.join( friends_list))
# print(new_string)
# print(new_string.split(','))
# print(','.join(','.join(csv.split(';')).split(':')))
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# new_list = []
# coordinates = []  # Initialize an empty list to store coordinates
# for x in range(x+ 1):
#      for y in range(y + 1):
#           for z in range(z + 1):
#             coordinate = [x, y, z]  # Create a tuple (x, y, z)
#             if(x + y + z != n):
#                 coordinates.append((coordinate))  # Append the tuple to the list
# print(coordinates)
new_list = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        new_list.append(name, score)
