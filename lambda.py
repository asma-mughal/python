#hellow this is lambda functions


def square(x):
    return x * x

print(square(8))

#name = lambda parameter(s): expression

square1 = lambda x: x * x
print(square1(8))

double_multiply = lambda x , y: 2 * x * y
def name_and_alias(name, alias):
    return name.title() + ':' + alias.title()

name_and_alias1 = lambda name, alias : name.title() + ':' + alias.title()
print(name_and_alias1("Fareeha", "Tosif"))
monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
monty_python.sort(key = lambda name : name.split(' ')) 
print(monty_python)
def func(n):
    return lambda a : a * n

doubler = func(2)
print(doubler(5))
def price_calc(start, hourly_rate):
    return lambda hours : start+ hourly_rate * hours
walking_cost = price_calc(4,6)
print(walking_cost(10)) 
print((price_calc(3,4)(1)))
print((lambda a,b,c: a+b+c)(2,3,4))

sum_lambda = lambda x : x + 5
print(sum_lambda(2))

strip_spaces = lambda str: ''.join(str.split(' '))
print(strip_spaces('Monty Pythons Flying Circus')) 

join_list_no_duplicates = lambda list_a, list_b : list(set(list_a + list_b))
list_a = [1,2,3,4]
list_b = [3,4,5,6,7]
print(join_list_no_duplicates(list_a,list_b))

def quad_function(a,b,c):
    return lambda x : a * (x *x) + (b * x) + c
g = (quad_function(2, 5, 6))
print(g(2))



signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups, key = lambda id :int(id[3:])))

class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

print(sorted(player_list, key = lambda player: player.score))
print([player.name for player in player_list])