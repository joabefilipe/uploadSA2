notas = [200, 100, 50, 20, 10, 5, 2]
notas_utili = [0, 0, 0, 0, 0, 0, 0]
moedas = [1, 0.50, 0.25, 0.10, 0.5, 0.1]
moedas_utili = [0, 0, 0, 0, 0, 0]
valor_compra = float(input ('Informe o valor da sua compra.'))
valor_recebimento = float(input ('Informe o valor recebido.'))

while valor_compra>valor_recebimento:
    print ('Valor não de Compra não pode ser maior que o dinheiro recebido.')
    valor_compra = float(input ('Informe o valor da sua compra.'))
    valor_recebimento = float(input ('Informe o valor recebido.'))


troco = valor_recebimento - valor_compra
troco_temp = 0.0
i=0
for i in range(len(notas)):
    quant_ced = 0
    while (notas [i] + troco_temp) <= troco:
        troco_temp = troco_temp + notas[i]
        quant_ced += 1
    notas_utili [i] = quant_ced
i=0
print (troco_temp)
for i in range(len(moedas)):
    quant_ced = 0
    while (moedas [i] + troco_temp) <= troco:
        troco_temp = troco_temp + moedas[i]
        quant_ced += 1
    moedas_utili [i] = quant_ced
    
i=0
for i in range(len(moedas)):
    if moedas_utili [i] != 0:
        print (str(moedas_utili [i]) + ' Moedas: ' + str(moedas [i]))
i=0
for i in range(len(notas)):
    if notas_utili [i] != 0:
        print (str(notas_utili[i]) + ' Notas: ' + str(notas[i]))
