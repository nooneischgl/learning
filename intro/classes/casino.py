#!usr/bin/env python3
import random


class Greeter(object):

    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello " + self.name.title())

    def goodbye(self):
        print("Goodbye " + self.name.title())

g = Greeter('scott')
g.hello()
g.goodbye()

g2 = Greeter('jessica')
g2.hello()
g2.goodbye()

class Die(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

d = Die(6)
print(d.roll())
print(d.roll())
print(d.roll())
print()
d2 = Die(20)
print(d2.roll())
print(d2.roll())
print(d2.roll())