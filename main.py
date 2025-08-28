altura = []
genero = []
contador = 0
for i in range(15):
    alt = float(input("Digite sua altura: "))
    altura.append(alt)
    while True:
        gen = str(input("Digite seu gênero [ M / F ]: ")).upper()[0]

        if gen == 'M':
            genero.append("Masculino")
            break
        elif gen == "F":
            genero.append("Feminino")
            contador += 1
            break
        else:
            print("Erro!Digite Novamente")

maior = max(altura)
menor = min(altura)

alturas_masculinas = [altura for i, altura in enumerate(altura) if genero[i]== "Masculino"]
media_masculina = sum(alturas_masculinas) / len(alturas_masculinas)

print(f"A maior altura do grupo foi de {maior:.2f} e a menor altura foi de {menor:.2f}")
print(f"A Média da altura Masculina do grupo é de {media_masculina:.2f}")
print(f"O número de pessoas do gênero feminino são de {contador}")