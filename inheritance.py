#Single inheritance.

class Car():
    @staticmethod
    def start():
        print("Car is start")

    @staticmethod
    def stop():
        print("Car is stop")

class Tata(Car):
    def __init__(self, name):
        print("This is my car")

        self.name = name

car1 = Tata("safari")
print(car1.name)
print(car1.start())

#Multi-level inheritance.

class Car():
    @staticmethod
    def start():
        print("Car is start")

    @staticmethod
    def stop():
        print("Car is stop")

class Tata(Car):
    def __init__(self, name):
        print("This is my car")

        self.name = name

class Safari(Tata):
    def __init__(self, brand):
        self.brand = brand

car = Safari("tata")
# print(car.name)
print(car.brand)        
car.start()

#Multiple inheritance.

class A():
    @staticmethod
    def one():
        print("App")

class B():
    def __init__(self, name):
        self.name = name 


class C(A, B):
    def __init__(self, surname):
        self.surname = surname

run = B("Yogesh")
run1 = C("Pisal")
print(run.name)
print(run1.surname)