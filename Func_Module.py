#Function and Module.

import random

def cars():
    car_1 = input("Enter The Car Name ('BMW', 'Audi', 'Safari'):- ")
    car_collections = ['BMW', 'Audi', 'Safari']
    d = random.choice(car_collections)
    c = {"big": car_1, "small": d}
    return c

car = cars()
print(car)



def ludo():
    player_choice  = input("Enter Your Number :- ")
    system_choice = ["1","2","3","4","5","6"]
    play = random.choice(system_choice)
    run = {"player_choice" : player_choice, "system_choice" : play}

    return run

d = ludo()
print(d)

#Multiplacation of two numbers using arguments and without arguments.
#With out Arguments.
def multiplication():
    a = int(input("Enter the no :- "))
    b = int(input("Enter the no :- "))
    c = a * b
    return c

sum = multiplication()
print(sum)

#With Arguments.
def multiplication(a,b):

    c = a * b
    return c

sum = multiplication(10,20)
print(sum)


#Greeting to person using this.
def greet(name):
    # return f"Hello, {name}!"
    return name

def welcome():
    message = greet("Yogesh")
    # print(message)
    return message

d = welcome()
print(d)

