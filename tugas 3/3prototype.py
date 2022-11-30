from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    def __init__(self):
        self.hp = None
        self.attack = None
        self.defense = None

    @abstractmethod
    def clone(self):
        pass

class Shopkeeper(Prototype):
    def __init__(self, hp, defense, attack):
        super().__init__()

        self.hp = hp
        self.defense = defense
        self.attack = attack

        self.charisma = 30

    def __str__(self):
        return f"This shopkeeper stats are \nHP = {self.hp}\nDEF = {self.defense}\nATK = {self.attack}\nCHR = {self.charisma}"

    def clone(self):
        return copy.deepcopy(self)

if __name__ == '__main__':
    sk = Shopkeeper(100, 20, 20)
    print(sk)