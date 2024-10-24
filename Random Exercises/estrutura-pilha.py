from contextlib import nullcontext

keep = True
pilha = []

while keep:
    print("--- Bem vindo ao Sistema de Pilha ---")
    print()

    print("O que voce deseja fazer?")
    print("Criar pilha e seus valores - 1")
    print("Consultar valores de pilha - 2")
    print("Alterar valores de pilha - 3")
    print("Excluir valores de pilha - 4")

    choose = int(input())

    #HERE WE ARE ADDING VALUES TO THE STACK - OPTION 1
    if choose == 1:
        print("--- Adicionando na Pilha ---")
        if pilha:
            print("A pilha ja foi criada! Recomece o programa caso queira outra pilha.")
        else:
            length = int(input("Qual o tamanho da pilha: "))
            if length >= 51:
                print("O tamanho maximo da Pilha e 50!")
            else:
                pilha = list(range(0, length))
                for i in range(len(pilha)):
                    pilha[i] = input(f"Digite o valor da posição {i + 1}: ")


    #HERE WE ARE CONSULTING THE VALUES FROM THE STACK - OPTION 2
    if choose == 2:
        print("--- Consulta da Pilha ---")
        for index, value in enumerate(pilha):  # Use enumerate para obter o índice e o valor
            print(f"Valor {index + 1}: {value}")
        if not pilha:
            print("A pilha esta vazia!!")

    #Default part in the end of the program to see if we should keep on
    end = input("Terminar programa? s - sim, n - não:\n").lower()

    if end == "s":
        keep = False

print()
print("Agradecemos o tempo em que esteve com a gente!")