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