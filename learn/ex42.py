## animal is-a object (yes, sort of confusting) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## self has-a name
        self.name = name

##cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##self has-a name
        self.name = name

##person is-a object
class Person(object):

    def __init__(self, name):
        ##hasa
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

##isa
class Employee(Person):

    def __init__(self, name, salary):
        ##super has a employee and self and isa __init__that has a name
        super(Employee, self).__init__(name)
        ##
        self.salary = salary

##
class Fish(object):
    pass

##
class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

##
satan = Cat("Satan")

##
mary = Person("Mary")

##
frank = Employee("Frank", 120000)

##
frank.pet = rover

##
flipper = Fish()

##
crouse = Salmon()

##
harry = Halibut()
