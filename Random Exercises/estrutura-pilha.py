from contextlib import nullcontext

keep = True

while keep:
    print("--- Bem vindo ao Sistema de Pilha ---")
    print()

    pilha = []

    print("O que voce deseja fazer?")
    print("Adicionar valores de pilha - 1")
    print("Consultar valores de pilha - 2")
    print("Alterar valores de pilha - 3")
    print("Excluir valores de pilha - 4")

    choose = int(input())

    #HERE WE ARE ADDING VALUES TO THE STACK - OPTION 1
    if choose == 1:
        length = int(input("Qual o tamanho da pilha: "))
        pilha = list(range(0, length))
        for i in range(len(pilha)):
            pilha[i] = input(f"Digite o valor da posição {i + 1}: ")


    #HERE WE ARE CONSULTING THE VALUES FROM THE STACK - OPTION 2
    if choose == 2:
        for i in range(0, len(pilha)):
            print(i)
        if not pilha:
            print("A pilha esta vazia!!")

    #Default part in the end of the program to see if we should keep on
    end = input("Terminar programa? s - sim, n - não:\n").lower()

    if end == "s":
        keep = False

print()
print("Agradecemos o tempo em que esteve com a gente!")