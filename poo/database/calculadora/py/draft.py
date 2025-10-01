from typing import Any


class Calculaltor:
    def __init__(self, batteryMax: int):
        self.display = 0.0
        self.batteryMax = batteryMax
        self.battery = 0

    def __str__(self):
        return f"display = {self.display: .2f}, battery = {self.battery}"

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

    def sum(self, a, b):
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





main()
