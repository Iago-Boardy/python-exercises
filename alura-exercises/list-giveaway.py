import numpy as np

def main():
    frutas = ["maçã", "banana", "uva", "pêra",
              "manga", "coco", "melancia", "mamão",
              "laranja", "abacaxi", "kiwi", "ameixa"]

    salada_frutas = np.random.choice(frutas, 3)
    print("Salada de frutas surpresa!")
    input("Aperte enter para saber sua salada de frutas...")

    print(salada_frutas)


if __name__ == "__main__":
    main()