nome = input("Insira o seu nome: ")
idade = int(input("Insira sua idade: "))
salario = float(input("Insira seu salario: "))
percentual = int(input("Insira o percentual de aumento:" ))

aumento = (salario /100) * percentual
novoSalario = aumento + salario
print(f"Seu nome é {nome}, voce tem {idade} anos e seu salario anterior era de R$ {salario}, com o aumento de {percentual}% (em reais {aumento}) seu salario atual é de {novoSalario}")