minutosHora = 60
segundosHora = 3600

menu = input("- Para converter hora para minuto digite 1;\n- Para converter minuto para hora digite 2.\n-Para converter horas para segundos digite 3\n")
menu = int(menu)

if menu == 1:
    pegaValor = input("Digite os minutos para converter: ")
    calculo   = float(pegaValor)/minutosHora
    print(pegaValor," equivale à ", round(calculo,2))

elif menu == 2:
    pegaValor = input("Digite as horas para converter: ")
    calculo = float(pegaValor) * minutosHora
    print(pegaValor, " equivale à ", round(calculo,2))

elif menu == 3:
    pegaValor = input("Digite as horas para converter: ")
    calculo = float(pegaValor) * segundosHora
    print(pegaValor, " horas, equivale à ", round(calculo, 2)," segundos")