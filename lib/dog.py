#!/usr/bin/env python3
from lib.person import Person

class Dog:
    # Class body goes here
    def __init__(self):
        pass

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.") 
    def walk(self):
        print("The person is walking.")  
    def talk(self):
        print("Hello World!") 



fido = Dog()
fido.bark()
fido.sit()

snoopy = Dog()
snoopy.bark()

person = Person()
person.walk()
person.talk()

