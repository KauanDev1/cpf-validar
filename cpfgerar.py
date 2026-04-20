import random

multiplicador = 10
multiplicador2 = 11
soma = 0
soma2 = 0
resultado = 0

for i in range(1):
    numero = random.randint(100000000, 999999999)

for digito in str(numero):
    resultado = int(digito) * multiplicador
    soma += resultado
    multiplicador -= 1

resto = soma % 11
if resto == 0 and 1:
    digitoValidoUm = 0

elif resto >= 2:
    digitoValidoUm = 11 - resto

for digito in str(numero):
    resultado = int(digito) * multiplicador2
    soma2 += resultado
    multiplicador2 -= 1

soma3 = soma2 + (digitoValidoUm * 2)
soma4 = soma3 % 11

if soma4 == 0 and 1:
    digitoValidoDois = soma4

elif soma4 >= 2:
    digitoValidoDois = 11 - soma4

cpf1 = digitoValidoUm
cpf2 = digitoValidoDois

numero_str = str(numero)

print(" ")
print(f"{numero_str[:3]}.{numero_str[3:6]}.{numero_str[6:]}-{cpf1}{cpf2}")
print(" ")











