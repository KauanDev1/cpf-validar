
cpfValor = input("Digite um cpf pra definir se ele é válido.....: ")
print(" ")
multiplicador = 10
multiplicador2 = 11
soma = 0
soma2 = 0
soma3 = 0
digitoValidoUm = 0
digitoValidoDois = 0

base = cpfValor[:9]

ultimo2 = cpfValor[-1]
ultimo1 = cpfValor[-2]

for digito in base:
    resultado = int(digito) * multiplicador
    soma += resultado
    multiplicador -= 1

resto = soma % 11
if resto == 0 and 1:
    digitoValidoUm = 0

elif resto >= 2:
    digitoValidoUm = 11 - resto


for digito in base:
    resultado = int(digito) * multiplicador2
    soma2 += resultado
    multiplicador2 -= 1\

soma3 = soma2 + (digitoValidoUm * 2)
soma4 = soma3 % 11

if soma4 == 0 and 1:
    digitoValidoDois = 0

elif soma4 >= 2:
    digitoValidoDois = 11 - soma4

cpf1 = digitoValidoUm
cpf2 = digitoValidoDois


if cpf1 == int(ultimo1) and cpf2 == int(ultimo2):
    print(f"Seu cpf é VALIDO! {cpfValor}")
else:
    print(f"O CPF {cpfValor} é INVÁLIDO!")











