import random

class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.health = 100

    def attack(self, other):
        damage = random.randint(5, self.power)
        other.health -= damage
        print(f"{self.name} атакує {other.name} на {damage} одиниць!")

    def is_alive(self):
        return self.health > 0


class Battle:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2

    def start(self):
        print("Починається битва!")
        while self.robot1.is_alive() and self.robot2.is_alive():
            self.robot1.attack(self.robot2)
            if not self.robot2.is_alive():
                break
            self.robot2.attack(self.robot1)
        winner = self.robot1 if self.robot1.is_alive() else self.robot2
        print(f"Переміг {winner.name} з {winner.health} HP!")


r1 = Robot("Робот1", 25)
r2 = Robot("Робот2", 20)
battle = Battle(r1, r2)
battle.start()
