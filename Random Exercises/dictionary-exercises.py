gabarito = {
    1: "D",
    2: "A",
    3: "C",
    4: "B",
    5: "A",
    6: "D",
    7: "C",
    8: "C",
    9: "A",
    10: "B"
}

resposta_certa = []
resposta_errada = []

print("Temos 10 questões na prova, vamos verificar quantas questoes o aluno acertou.(A, B, C ou D)")

for i in range(0, len(gabarito)):
    resposta = input(f"Qual a resposta da {i+1}° questão: ").upper()
    if resposta == gabarito[i+1]:
        print("Resposta Correta - computando...")
        resposta_certa.append(resposta)
    else:
        print("Resposta Errada - computando...")
        resposta_errada.append(resposta)


print("Respostas corretas", resposta_certa)
print("Respostas erradas", resposta_errada)