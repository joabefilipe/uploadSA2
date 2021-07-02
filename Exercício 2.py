
pegaValor1 = int(input("Digite um valor:"))
pegaValor2 = int(input("Digite um valor:"))
pegaValor3 = int(input("Digite um valor:"))
pegaValor4 = int(input("Digite um valor:"))

total = (pegaValor1+pegaValor2+pegaValor3+pegaValor4)
mediaTotal = total/4

if mediaTotal < 0:
    print("O resultado é negativo: ",  mediaTotal)
elif mediaTotal > 0:
    print("O resultado é positivo: ",  mediaTotal)


####################COM FUNÇÃO#######################
    
    valores = [5.2 , 9.0 , -3.0 , 4.3]

quantidadeNotas = len(valores)
mediaValores = sum(valores)/quantidadeNotas

print(round(mediaValores,2))