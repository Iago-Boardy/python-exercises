import numpy as np
import random
#Nem precisamos da biblioteca de math, porque podemos usar a de numpy

   #question 1
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

aaa = np.random.choice(lista)
#print(aaa)

   #question 2
randomvalue = random.randrange(100)
#print(randomvalue)

   #question 3
n1 = int(input("Digite um numero para calcular a potencia: "))
n2 = int(input("Digite outro numero para calcular a potencia: "))

potencia = np.pow(n1, n2)
print(potencia)

   #a partir de agora teremos alguns projetos, que irao ser criados em outras pages a principio