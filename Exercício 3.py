n = int(input("Digite o tamanho da lista que deseja: "))
lista = [0] * n
i = 0
total = 0

for i in range(len(lista)):
    lista[i] = input("Digite um valor")
    total += int(lista[i])
print(lista)

mediaLista = total/n
print(mediaLista)

maiorValor = max(lista)
print("Maior Valor: " + maiorValor)

menorValor = min(lista)
print("menor valor: " + menorValor)