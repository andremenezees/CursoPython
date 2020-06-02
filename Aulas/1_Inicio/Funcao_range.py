
#forma 1, o valor num é o contador, se não especificar o range inicial é 0.

"""
for num in range(11):
    print(num)
"""

#Forma 2 , é especificado o valor de inicio e o valor de parada
"""
for num in range(1,10):
    print (num)
"""

#Forma 3, é especificado o valor de inicio, fim e o passo.
"""
for num in range(1,10,2):
    print(num)
"""
#Forma 4, é especificado o inicio, fim e o passo. Porem neste caso o passo é negativo
"""
for num in range(100,10,-2):
    print(num)
"""
#Para criar uma lista com range
lista = list(range(1,10))
print(lista)
