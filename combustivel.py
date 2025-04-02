tipoCombustivel = input("Insira o tipo de combustível:")
numLitros = float(input("Insira a quantidade de litros que você quer abastecer: "))

gasolina = 5.80
etanol = 4.90

valorGasolina = numLitros * gasolina
valorEtanol = numLitros * etanol

if tipoCombustivel == "G":
    print(f"Você abasteceu {numLitros} litros de Gasolina voce pagou R${valorGasolina}. ")

else:
    print(f"Você abasteceu {numLitros} litros de Etanol voce pagou R${valorEtanol}. ")
