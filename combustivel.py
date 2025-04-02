tipoCombustivel = input("Insira o tipo de combustível: ")
numLitros = float(input("Insira a quantidade de litros que você quer abastecer: "))

gasolina = 5.80
etanol = 4.90


if tipoCombustivel == "G":

    valorGasolina = numLitros * gasolina
    print(f"Você abasteceu {numLitros} litros de Gasolina voce pagou R${valorGasolina}. ")

else:
    if tipoCombustivel == "E":
            valorEtanol = numLitros * etanol

            print(f"Você abasteceu {numLitros} litros de Etanol voce pagou R${valorEtanol}. ")

    else:
        print("Tipo de combustivel invalido.")