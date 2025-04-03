hora01 = int(input("Insira a primeira hora: "))
minuto01 = int(input("Insira o segundo minuto: "))
hora02 = int(input("Insira a segunda hora : "))
minuto02 = int(input("Insira o segundo minuto : "))

somaHoras = hora01 + hora02
somaMinutos = minuto01 + minuto02

if somaMinutos >= 60:
    somaMinutos -= 60
    somaHoras += 1

if somaHoras > 12:
    somaHoras -= 12

print(f"O Horario é {somaHoras}:{somaMinutos:02d}")









