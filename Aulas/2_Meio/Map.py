"""
Map
com o map, fazemos mapeamento de valores para função.

"""

import math


def area(r):
    # Calcula a area de um circulo de raio r
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

#Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

#Forma com MAP (Map recebe dois parametros, primeiro a função depois um iteravel)

areas = map(area, raios)
print(list(areas))

#Forma mais utilizada, com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

#No map o dado é utilizado apenas uma vez. Apos ser utilizado a memoria é limpa.

#Outro exemplo(Transformar as temperaturas em Celcius para Fahrenheit

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19),
           ('Los Angeles', 26), ('Tokio', 26), ('Nova York', 28)]

print(cidades)

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))

