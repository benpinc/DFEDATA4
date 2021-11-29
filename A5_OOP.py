###############################################################
#                             QA  
# Inheritance, polymorphism, abstraction, encapsulation       #
###############################################################

from abc import ABC, abstractmethod

#superclass
class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

#subclass - defines a class within the superclass, inheriting the attributes and changing where needed
class Owl(Bird):
    def reproduce(self):
        self.babies += 6

    def eat(self):
        return "Peck peck"

#mysubclass
class EurasianJay(Bird):
    def eat(self):
        return "worms"

ej = EurasianJay.eat

print(EurasianJay)
print(ej)


# class Dodo(Bird):
#     Fly = False
#     extinct = True

#     def eat(self):
#         return "Nom nom"

#     def reproduce(self):
#         if not self.extinct:
#             self.babies += 1

# DodoA = Dodo.eat
# print(DodoA.eat)     