class Carros:
    def __init__(self, pess: int = 0, gas: int = 0, km: int = 0):
        self.pess = pess
        self.gas = gas
        self.km = km

    def __str__(self):
        return f"pass: {self.pess}, gas: {self.gas}, km: {self.km}"

    def maxPess(self):
        if self.pess < 2:
            self.pess += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.pess == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.pess -= 1

    def gaxMax(self, increment: int):
        self.gas += increment
        if self.gas > 100:
            self.gas = 100

    def drive(self, distance: int):
        if self.pess == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print("fail: tanque vazio")
        else:
            if distance > self.gas:
                print(f"fail: tanque vazio apos andar {self.gas} km")

                self.km += self.gas
                self.gas = 0
            else:
                self.km += distance
                self.gas -= distance

def main():
    carro = Carros()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "enter":
            carro.maxPess()
        elif args[0] == "show":
            print(carro)
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            increment = int(args[1])
            carro.gaxMax(increment)
        elif args[0] == "drive":
            increment = int(args[1])
            carro.drive(increment)

main()






