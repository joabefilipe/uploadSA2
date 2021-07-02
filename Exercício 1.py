L = [5, 7, 2, 9, 4, 1, 3]
print(L)
# A
tamanhoL = len(L)
print(tamanhoL)

# B
maiorValor = max(L)
print(maiorValor)

# C
menorValor = min(L)
print(menorValor)

# D
somaElementos = 0       # Declaro o inicio
for L in L:             # condição
    somaElementos += L  # Repetição
print(somaElementos)

# E
L = [5, 7, 2, 9, 4, 1, 3]
L.sort()
print(L)

# D
L.sort(reverse = True)
print(L)