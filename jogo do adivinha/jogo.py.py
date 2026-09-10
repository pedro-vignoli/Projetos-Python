import random

novamente = "s"

recorde = 1000

while novamente == "s":

    numero = random.randint(1, 100)

    palpite = 0
    tentativa = 0

    while palpite != numero:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativa += 1

        if palpite < 1 or palpite > 100:
            print("Isso aí não conta! Escolhe um número entre 1 e 100.")
        elif numero == palpite:
            print(f"Mandou bem! Você descobriu em {tentativa} rodada(s).")
        elif numero > palpite:
            print("Sobe um pouco mais.")
        else:
            print("Desce um pouco.")

    if tentativa < recorde:
        recorde = tentativa
        print(f"Uau, marca nova! {recorde} rodada(s) e pronto.")
    else:
        print(f"Quase! O melhor resultado até agora segue em {recorde} rodada(s).")

    novamente = input("Bora de novo? (s/n): ")

print("Até a próxima!")
