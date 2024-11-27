
def main():
    lista = []
    for i in range(1, 6):
        valor = int(input(f"Digite o {i}° number: "))
        lista.append(valor)
    lista.reverse()
    print(lista)



if __name__ == "__main__":
    main()
