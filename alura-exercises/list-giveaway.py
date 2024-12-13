import numpy as np

def main():
    print("Sistema de Jardinagem")
    raio = float(input("Qual o raio da area circular: "))
    pi = np.pi

    area = pi * pow(raio, 2)
    valor = area * 25.00

    print(f"O valor final que deve ser pago para uma area de {round(area, 2)}, e de R${round(valor, 2)}.")
if __name__ == "__main__":
    main()