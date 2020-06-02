nome = 'mapache'

for letra in nome:
    print(letra)

lista = [1,11,3,4,5,6]

#Forma de pegar o indice e o valor
for i in enumerate(lista):
    print(i)

#Função range muito importante para usar no FOR

quant = int(input("Quantidade de numeros somados:"))

soma = 0
for n in range(1,quant+1):
    numeros = int(input("Numero a ser somado:"))
    soma = soma + numeros

print(f'A soma é {soma}')
