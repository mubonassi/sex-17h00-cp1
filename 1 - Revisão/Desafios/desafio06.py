import math

print("| AREA, CIRCUNFERENCIA E DIAMETRO DE UM CIRCULO |")

raio = float(input("Digite o raio do circulo: "))

area = math.pi * raio**2
circunferencia = 2 * math.pi * raio
diametro = 2 * raio

print(f"Area: {area:.2f}")
print(f"Circunferencia: {circunferencia:.2f}")
print(f"Diametro: {diametro:.2f}")