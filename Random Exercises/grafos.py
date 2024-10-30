def main():
    end = True
    while end:
        print("--- Bem-vindo ao Sistema de Grafo ---")
        word = input("Diga a palavra que usaremos para comparar: ")
        userInput = []
        rightW = []
        wrongW = []

        for j in range(len(word)):
            user_letter = input(f"{j + 1}ª letra: ")
            userInput.append(user_letter)
            if user_letter == word[j]:
                rightW.append(user_letter)
            else:
                wrongW.append(user_letter)

        print("Letras corretas:", rightW)
        print("Letras incorretas:", wrongW)
        print(f"Você digitou: {userInput} e a palavra certa era '{word}'.")

        end = input("Deseja continuar? (s/n): ").strip().lower() == 's'


if __name__ == "__main__":
    main()
