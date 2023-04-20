# E22MCAG0008
# Divik Arora
from Duck import Duck
from fly_with_wings import FlyWithWings
from Quack import Quack

class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("I'M Mallard Duck")
