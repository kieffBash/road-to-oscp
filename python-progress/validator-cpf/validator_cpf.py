"""
Sobre a parte mais hardcode em get_numbers_1:
    O professor tinha dito para não utilizarmos os CPFs com '.' e '-' de primeira.
    Porém, se quisessemos, poderíamos tentar criar dessa forma. Olhando depois percebi
    que poderia ter utilizado o método .replace() o que tornaria bem mais fácil, porém,
    preferi deixar dessa forma mais bruta, acredito mostrar mais da minha evolução
    conforme o tempo for passando
"""

# cpf usuário
cpf = "096.927.000-38"
get_numbers_1 = cpf[0:11].split(".")

# gera uma lista com contagem regressiva de 10 a 2
countdown_1 = []
for n in range(10, 1, -1):
    countdown_1.append(n)

# gera uma lista com cada número do cpf separados por .
int_numbers_1 = []
for s in get_numbers_1:
    for n in s:
        int_numbers_1.append(int(n))

# gera uma lista com os números multiplicados
multiplied_numbers_1 = []
for i in range(0, 9):
    multiplied_numbers_1.append(countdown_1[i] * int_numbers_1[i])

# soma todos os números
multiplied_sum_1 = 0
for n in multiplied_numbers_1:
    multiplied_sum_1 += n

check_remainder_1 = (multiplied_sum_1 * 10) % 11
first_digit = 0 if check_remainder_1 >= 10 else check_remainder_1


# pega os números para o segundo digito
get_numbers_2 = cpf[0:11].split(".")
get_numbers_2.append(str(first_digit))

# faz a contagem regressiva para o segundo digito
countdown_2 = []
for n in range(11, 1, -1):
    countdown_2.append(n)

# pega os números inteiros contando com o digito um para o segundo digito
int_numbers_2 = int_numbers_1.copy()
int_numbers_2.append(first_digit)

# gera uma lista com os números multiplicados para o digito 2
multiplied_numbers_2 = []
for i in range(0, 10):
    multiplied_numbers_2.append(countdown_2[i] * int_numbers_2[i])

# soma todos os números para o digito 2
multiplied_sum_2 = 0
for n in multiplied_numbers_2:
    multiplied_sum_2 += n

check_remainder_2 = (multiplied_sum_2 * 10) % 11
second_digit = 0 if check_remainder_2 >= 10 else check_remainder_2

formated_cpf = f"{cpf[0:11]}-{first_digit}{second_digit}"

if formated_cpf == cpf:
    print("Seu CPF é válido.")
else:
    print("Seu CPF é inválido.")
