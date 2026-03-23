# EXERCICIO NÚMERO 1
ano = int(input("Insira o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")

# EXERCICIO NÚMERO 2
peso = float(input("Insira o seu peso: "))
altura = float(input("Insira sua altura: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f"Está abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Peso ideal")
elif imc >= 25 and imc <= 29.9:
    print(f"Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print(f"Obesidade")
elif imc >= 35 and imc <= 39.9:
    print(f"Obesidade Mórbida")
elif imc >= 40:
    print(f"Obsidade Mórbida Severa")
else:
    print(f"IMC não calculado, insira novamente por gentileza")

# EXERCICIO NÚMERO 3
quantidade = int(input("Insira a quantidade de produtos adquiridos: "))
valor = int(input("Insira o valor do produto: "))
if quantidade > 100:
    desconto = 0.10
else:
    desconto = 0.05

desconto_unidade = valor * desconto
unidade_desconto = valor - desconto_unidade
total = quantidade * unidade_desconto
print(f"O valor inicial do produto R${valor}")
print(f"A quantidade inicial do produto foi: {quantidade}")
print(f"O valor com desconto por unidade foi de R$ {unidade_desconto}")
print(f"O valor final foi: {total}")


# EXERCICIO NÚMERO 4
idade = int(input("Digite sua idade: "))
if idade >= 18 and idade <= 65:
    print(f"Voto obrigatório")
elif idade > 16 and idade <= 18:
        print(f"Voto facultativo")
else:
        print(f"Não eleitor")

# EXERCICIO NÚMERO 5
idade1 = int(input("Digite a idade da primeira pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))
idade3 = int(input("Digite a idade da terceira pessoa: "))

maior = idade1
if (idade2 > maior):
    maior = idade2
if (idade3 > maior):
    maior = idade3

menor = idade1
if (idade2 < menor):
    menor = idade2
if (idade3 < menor):
    menor = idade3
print(f"A maior idade é {maior} e o menor idade é {menor}")

# EXERCICIO NÚMERO 6
hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

if (0 <= hora <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59):
    situacao = "A hora inserida é válida"
    print(f"A hora é: {hora}:{minutos}:{segundos}")
    print (situacao)
else:
    situacao = "A hora inserida é inválida"
    print(situacao)

# EXERCICIO NÚMERO 7
nota = float(input("insira a nota: "))
if nota >= 9 and nota <= 10:
    nota = "A"
elif nota >= 7 and nota < 9:
    nota = "B"
elif nota >= 5 and nota < 7:
    nota = "C"
elif nota >= 3 and nota < 5:
    nota = "D"
elif nota >= 0 and nota < 3:
    nota = "E"
else:
    nota = "A nota é inválida"
print(f"A nota é: {nota}")

# EXERCICIO NÚMERO 8
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
lado4 = float(input("Digite o quarto lado: "))

if lado1 == lado2 == lado3 == lado4:
    forma = "A forma geométrica é um quadrado"
elif ((lado1 == lado2 and lado3 == lado4) or
      (lado1 == lado3 and lado2 == lado4) or
      (lado1 == lado4 and lado2 == lado3)):
    forma = "A forma geométrica é um retângulo"
else:
    forma = "A forma geométrica não é nem quadrado e nem retângulo"
print(f"A forma é: {forma}")

#EXERCICIO 9
n1 = float(input("Insira um número: "))
n2 = float(input("Insira o segundo número: "))
match(input("Escolha a operação: +, -, * ou /")):
    case "+":
        print(n1 + n2)
    case "-":
        print(n1 - n2)
    case "*":
        print(n1 * n2)
    case "/":
        if n2 == 0:
            print("Não é possivel realizar a operação por 0")
            pass
        else:
            print(n1 / n2)
    case _:
        print("Operação inválida, tente novamente")

EXERCICIO 10
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
notas = [nota1, nota2, nota3]
menor_nota = min(notas)
notas.remove(menor_nota)
media = sum(notas) / len(notas)
print(f"A média final (sem a menor nota) é: {media}")

# # #EXERCICIO 11
# ---------------------------
# |Linhas Codigo    | a | b |
# ---------------------------
# | 1 |             | 8 |   |
# ---------------------------
# | 2 |             | 8 | 3 |
# ---------------------------
# | 4 |             | 6 | 3 |
# ---------------------------
# | 5 |             | 6 | 9 |
# ---------------------------
# | 6 |             | 6 | 9 |
# ---------------------------


# EXERCICIO 12
# ----------------------------------
# | Linhas Codigo   | x  | y  | z  |
# ----------------------------------
# | 1 |             | 12 |    |    |
# ----------------------------------
# | 2 |             | 12 | 5  |    |
# ----------------------------------
# | 3 |             | 12 | 5  | 3  |
# ----------------------------------
# | 6 |             | 12 | 5  | 15 |
# ----------------------------------
# | 7 |             | 12 | 10 | 15 |
# ----------------------------------
# | 9  |            | 8  | 10 | 15 |
# ----------------------------------

# EXERCICIO 13 -  DESAFIO
import random
sorteio = random.randint(1, 10)
tentativa = int(input("Insira um número de 1 a 10: "))

if tentativa == sorteio:
    print("Acertou de primeira tentativa!")
else:
    print("Você infelizmente errou!")
    if tentativa > sorteio:
        print("O número sorteado é menor que o inserido.")
    else:
        print("O número sorteado é maior que o inserido.")
tentativa2 = int(input("Tente novamente, insira um número: "))
if tentativa2 == sorteio:
    print("Você acertou na segunda tentativa!")
else:
    print(f"O número era {sorteio}")

