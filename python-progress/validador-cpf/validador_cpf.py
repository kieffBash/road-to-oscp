# cpf usuário
cpf = "096.927.000-38"
pega_numeros_1 = cpf[0:11].split(".")

# gera uma lista com contagem regressiva de 10 a 2
contagem_regressiva_1 = []
for n in range(10, 1, -1):
    contagem_regressiva_1.append(n)

# gera uma lista com cada número do cpf separados por .
numeros_inteiros_1 = []
for conjunto in pega_numeros_1:
    for numeros in conjunto:
        numeros_inteiros_1.append(int(numeros))

# gera uma lista com os números multiplicados
numeros_multiplicados_1 = []
for i in range(0, 9):
    numeros_multiplicados_1.append(contagem_regressiva_1[i] * numeros_inteiros_1[i])

# soma todos os números
soma_multiplicados_1 = 0
for numero in numeros_multiplicados_1:
    soma_multiplicados_1 += numero

verifica_resto_1 = (soma_multiplicados_1 * 10) % 11
primeiro_digito = 0 if verifica_resto_1 >= 10 else verifica_resto_1


# pega os números para o segundo digito
pega_numeros_2 = cpf[0:11].split(".")
pega_numeros_2.append(str(primeiro_digito))

# faz a contagem regressiva para o segundo digito
contagem_regressiva_2 = []
for contagem_2 in range(11, 1, -1):
    contagem_regressiva_2.append(contagem_2)

# pega os números inteiros contando com o digito um para o segundo digito
numeros_inteiros_2 = numeros_inteiros_1.copy()
numeros_inteiros_2.append(primeiro_digito)

# gera uma lista com os números multiplicados para o digito 2
numeros_multiplicados_2 = []
for i in range(0, 10):
    numeros_multiplicados_2.append(contagem_regressiva_2[i] * numeros_inteiros_2[i])

# soma todos os números para o digito 2
soma_multiplicados_2 = 0
for numero in numeros_multiplicados_2:
    soma_multiplicados_2 += numero

verifica_resto_2 = (soma_multiplicados_2 * 10) % 11
segundo_digito = 0 if verifica_resto_2 >= 10 else verifica_resto_2

print("Dígitos verificadores:", primeiro_digito, segundo_digito)
print("CPF completo:", cpf[:12] + f"{primeiro_digito}{segundo_digito}")
