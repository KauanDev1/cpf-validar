# cpf-validar

Projeto de **lógica de programação** que usa **lógica matemática** para validar (e gerar) CPFs,
desenvolvido em **Python padrão** — sem bibliotecas externas, sem frameworks, apenas
laços de repetição, condicionais e operações aritméticas.

O objetivo aqui não é entregar uma biblioteca pronta, e sim exercitar o raciocínio:
traduzir uma regra matemática oficial em código do zero.

---

## A lógica matemática por trás do CPF

Um CPF tem 11 dígitos: os **9 primeiros** formam a base e os **2 últimos** são
dígitos verificadores, calculados a partir da base pelo algoritmo do **módulo 11**.

Ou seja, os dois últimos dígitos não são aleatórios — eles são o *resultado de uma conta*
feita em cima dos nove primeiros. Validar um CPF é refazer essa conta e comparar.

### 1º dígito verificador

Multiplica-se cada um dos 9 primeiros dígitos por pesos decrescentes de **10 até 2**,
e soma-se tudo:

```
soma = d1×10 + d2×9 + d3×8 + d4×7 + d5×6 + d6×5 + d7×4 + d8×3 + d9×2
resto = soma % 11
```

A partir do resto:

- se `resto` for **0 ou 1** → o dígito é **0**
- se `resto` for **2 ou mais** → o dígito é **11 − resto**

### 2º dígito verificador

Mesma ideia, mas agora entram **10 dígitos** (os 9 da base + o 1º dígito verificador
recém-calculado), com pesos decrescentes de **11 até 2**:

```
soma = d1×11 + d2×10 + ... + d9×3 + dv1×2
resto = soma % 11
```

E a mesma regra do resto se aplica:

- `resto` 0 ou 1 → dígito **0**
- `resto` ≥ 2 → dígito **11 − resto**

### Validação

Um CPF é válido quando os dois dígitos calculados batem exatamente com os
dois últimos dígitos informados.

---

## Arquivos

| Arquivo | O que faz |
|---|---|
| `cpfValidar.py` | Lê um CPF digitado pelo usuário, recalcula os dois dígitos verificadores e informa se é **VÁLIDO** ou **INVÁLIDO**. |
| `cpfgerar.py` | Sorteia uma base de 9 dígitos, calcula os dois verificadores por essa mesma lógica e imprime um CPF formatado (`XXX.XXX.XXX-YY`). |

Os dois scripts compartilham o mesmo núcleo matemático — um aplica a regra para
**conferir**, o outro aplica para **construir**.

---

## Como executar

Basta ter Python 3 instalado:

```bash
# validar um CPF
python3 cpfValidar.py

# gerar um CPF matematicamente válido
python3 cpfgerar.py
```

O `cpfValidar.py` espera o CPF digitado **apenas com números**, sem pontos ou traço:

```
Digite um cpf pra definir se ele é válido.....: 12345678909
```

---

## Aviso

O CPF gerado pelo `cpfgerar.py` é apenas **matematicamente válido**, ou seja,
passa na regra do módulo 11. Ele **não corresponde a nenhuma pessoa real** e não
tem qualquer vínculo com a Receita Federal. O uso aqui é estritamente
**didático**, para testar a própria lógica de validação.
