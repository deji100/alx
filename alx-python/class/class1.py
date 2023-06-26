import random
import math

class Warrior:

    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)

        return attkAmt
    
    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt

class Battle:

    def startFight(self, warrior1, warrior2):

        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over.":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over.":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttackAmt = warriorA.attack() 

        warriorBBlookAmt = warriorB.block()

        damageToWarrorB = math.ceil(warriorAAttackAmt - warriorBBlookAmt)

        warriorB.health = warriorB.health - damageToWarrorB

        print("{} attacks {} and deals {} damages".format(warriorA.name, warriorB.name, damageToWarrorB))

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} is victorious and {} is dead".format(warriorA.name, warriorB.name))
            return "Game Over."
        else:
            return "Fight Again."
        
def main():

    maximus = Warrior("Maximus", 50, 20, 10)

    deji = Warrior("Deji", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, deji)

main()
