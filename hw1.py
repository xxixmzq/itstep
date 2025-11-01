class Student:
    def __init__(self, name):
        self.name = name
        self.money = 50
        self.knowledge = 0
        self.energy = 50
        self.day = 0
    def study(self):
        print(f"{self.name} вчиться")
        self.knowledge += 10
        self.energy -= 10
        self.money -= 5
        if self.money < 0:
            self.money = 0
    def work(self):
        print(f"{self.name} працює")
        self.money += 20
        self.energy -= 15
    def rest(self):
        print(f"{self.name} відпочиває")
        self.energy += 20
        self.money -= 10
        if self.money < 0:
            self.money = 0
    def live_day(self):
        self.day += 1
        print(f"{self.day}: гроші={self.money}, знання={self.knowledge}, енергія={self.energy}")

        if self.money < 15:
            self.work()
        elif self.energy < 20:
            self.rest()
        elif self.knowledge < 100:
            self.study()
        else:
            self.rest()

        if self.energy > 100:
            self.energy = 100
        if self.knowledge > 100:
            self.knoledge = 100

    def live_year(self):
        print("Початок року!")
        for i in range(1, 365):
            self.live_day()
        print(f"Рік закінчився! Результати {self.name}:")
        print(f"Гроші={self.money}, Знання={self.knowledge}, Енергія={self.energy}")
if __name__ == '__main__':
    student = Student("Софія")
    student.live_year()