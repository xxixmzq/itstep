import random

class Cipher:
    def __init__(self, *numbers):
        self.__data = numbers  
        self.__result = self.__encrypt()

    def __encrypt(self):
        operation = random.choice(["+", "-", "*", "/"])
        a, b = random.sample(self.__data, 2)
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        else:
            return a / b if b != 0 else 0

    def __str__(self):
        return f"Результат шифрування: {self.__result}"


cipher = Cipher(10, 5, 3, 8)
print(cipher)