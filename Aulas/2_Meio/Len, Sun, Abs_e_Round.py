"""
Len, Abs, Sum, Round

#Len

len() -> Retorna o tamanho (ou seja, o numero de itens) de um iteravel.

abs() -> Retorna o valor absoluto de um numero inteiro ou real. Ou seja o modulo
somente o numero independente do sinal.

sum() -> Retornar a soma dos valores. É possivel receber um valor inicial com sum.

round() -> Retorna um numero arrendondado para n digito de precisão apos a casa
decimal, se a precisão não for informada retorna o inteiro mais proximo da entrada.

"""
#Exemplo len():
print(len(range(0,9)))

#Exemplo Abs():
print(abs(-5))
print(abs(5))
print(abs(-5.3232323))

#Exemplo sum():
print(sum([1, 2.22, 3, 4, 5]))
print(sum([1, 2.22, 3, 4, 5], 5))

#Exemplo round:
print(round(10.2))
print(f'Para o numero 10.51 arendonda-se para cima:{round(10.55)}')
print(f'Para o numero 10.49 arendonda-se para baixo:{round(10.49)}')

print(f'Para o numero 10.5123 podemos escolher para ter precisão de 2 casas:{round(10.5123, 2)}')
print(f'Para o numero 10.512312313131 podemos escolher para ter precisão de 5 casas:{round(10.512312313131, 5)}')

