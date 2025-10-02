from typing import Any


class Calculator:
    def __init__(self, batteryMax: int):
        self.display = 0.0
        self.batteryMax = batteryMax
        self.battery = 0

    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.battery}"

    def charge(self, increment: int):
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def useBattery(self):
        if self.battery > 0:
            self.battery -= 1
            return True
        else:
            print("fail: bateria insuficiente")
            return False

    def sum(self, a:float, b: float):
        if self.useBattery() == False:
            return
        self.display = a + b

    def division(self, a, b):
        if self.useBattery() == False:
            return
        if b == 0:
            print("fail: divisao por zero")
            return
        self.display = a / b

def main():

    calculator = None
    while True:

        line: str = input()
        if line == "":
                continue
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax: int = int(args[1])
            calculator = Calculator(batteryMax)
        elif args[0] == "show":
            print(calculator)
        elif args[0] == "charge":
            increment: int = int(args[1])
            calculator.charge(increment)
        elif args[0] == "sum":
            a: float = float(args[1])
            b: float = float(args[2])
            calculator.sum(a,b)
        elif args[0] == "div":
            a: float = float(args[1])
            b: float = float(args[2])
            calculator.division(a, b)

main()
