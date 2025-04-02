hora01 = float(input("Insira a primeira hora: "))
minuto01 = float(input("Insira o segundo minuto: "))
hora02 = float(input("Insira a segunda hora : "))
minuto02 = float(input("Insira o segundo minuto : "))

entrada01 = hora01 + minuto01
entrada02 = hora02 + minuto02

somasHoras = hora01 + hora02
somaMinutos = (minuto01 + minuto02) - 59

converteHoras = somasHoras * 60

reConversao = (converteHoras + somaMinutos ) /

print(reConversao)



#