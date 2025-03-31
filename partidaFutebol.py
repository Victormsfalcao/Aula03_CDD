mandante = input("Insira o mandante: ")
visitante = input("Insira o visitante: ")

golsMandante = int(input("Insira a quantidade de gols do mandante: "))
golsVisitante = int(input("Insira a quantidade de gols do visitante: "))

if golsMandante > golsVisitante:
    print(f"O Vencedor é : {mandante} pelo placar de {golsMandante} x {golsVisitante} contra o {visitante}")

else:
     if golsVisitante > golsMandante:
       print(f"O Vencedor é : {visitante} pelo placar de {golsVisitante} x {golsMandante} contra o {mandante} !")

     else:
       print(f"Empate! o placar foi de {golsMandante} x {golsVisitante}!  ")

