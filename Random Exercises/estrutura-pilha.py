def main():
    keep = True
    pilha = []

    while keep:
        print("\n--- Bem vindo ao Sistema de Pilha ---\n")
        print("O que você deseja fazer?")
        print("1 - Criar pilha e seus valores")
        print("2 - Consultar valores da pilha")
        print("3 - Alterar valores da pilha")
        print("4 - Excluir valores da pilha")

        try:
            choose = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número.")
            continue

        # Adicionando valores à pilha - Opção 1
        if choose == 1:
            print("--- Adicionando na Pilha ---")
            if pilha:
                print("A pilha já foi criada! Reinicie o programa caso queira outra pilha.")
            else:
                try:
                    length = int(input("Qual o tamanho da pilha: "))
                    if length >= 51:
                        print("O tamanho máximo da Pilha é 50!")
                    else:
                        pilha = list(range(0, length))
                        for i in range(len(pilha)):
                            pilha[i] = input(f"Digite o valor da posição {i + 1}: ")
                except ValueError:
                    print("Tamanho inválido! Digite um número inteiro.")

        # Consultando os valores da pilha - Opção 2
        elif choose == 2:
            print("--- Consulta da Pilha ---")
            if not pilha:
                print("A pilha está vazia!")
            else:
                for index, value in enumerate(pilha):
                    print(f"Valor {index + 1}: {value}")

        # Editando os valores da pilha - Opção 3
        elif choose == 3:
            print("--- Editando a Pilha ---")
            if not pilha:
                print("Primeiro crie uma pilha para poder editá-la!")
            else:
                for i in range(len(pilha)):
                    print(f"Valor atual na posição {i + 1}: {pilha[i]}")
                    edit_choice = input("Você deseja editar esse valor? (s/n): ").lower()

                    if edit_choice == 's':
                        novo_valor = input("Digite o novo valor: ")
                        pilha[i] = novo_valor
                        print(f"Valor na posição {i + 1} atualizado para: {pilha[i]}")
                        break
                    else:
                        print("Valor não alterado.")

        # Deletando valores da pilha - Opção 4
        elif choose == 4:
            print("--- Deletando da Pilha ---")
            if not pilha:
                print("A pilha está vazia! Primeiro crie uma pilha para poder excluí-la.")
            else:
                delete_choice = input("Deseja apagar a pilha inteira? (s/n): ").lower()
                if delete_choice == 's':
                    pilha.clear()
                    print("Pilha deletada com sucesso!")
                else:
                    try:
                        index = int(input("Digite a posição do valor que deseja remover (1 a {}): ".format(len(pilha)))) - 1
                        if 0 <= index < len(pilha):
                            removido = pilha.pop(index)
                            print(f"Valor '{removido}' removido da posição {index + 1}.")
                        else:
                            print("Posição inválida!")
                    except ValueError:
                        print("Entrada inválida! Digite um número.")

        else:
            print("Opção inválida! Tente novamente.")

        # Verificar se o usuário quer continuar no programa
        end = input("Terminar programa? s - sim, n - não:\n").lower()
        if end == "s":
            keep = False

    print("\nAgradecemos o tempo em que esteve com a gente!")

if __name__ == "__main__":
    main()
