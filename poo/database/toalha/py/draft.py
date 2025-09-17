class Towel: 
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0
    def __str__(self):
        return f"{self.color}:{self.size}:{self.wetness}"


print("Qual a cor da sua toalha e o tamanho?")
color = input()
size = input()
towel: Towel = Towel(color, "P")
print(f"Sua toalha é {towel.color} e {towel.size}")

