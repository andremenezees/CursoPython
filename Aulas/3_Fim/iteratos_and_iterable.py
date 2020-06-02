"""

Iterator(iterador) -> é um objeto que pode ser iterado. Ou seja um objeto que retorna um dado.
                      é possivel testar se é um iterador através da função next().

Iterable(iteravel) -> é um objeto que retorna um iterator.
                      é  possivel testar se é um iteravel através da função iter().


"""
#Exemplo interavel

nome = 'mapache' #Iteravel
lista = [1, 2,3, 4, 5, 6]# iteravel

# Iterador

for letra in nome:  #nome é iteravel e letra é iterador.
    print(f'{letra}')
print("\n")
"""
Criando um loop

"""

def meu_for(iteravel):
    it = iter(iteravel) #para transformar em um iterador

    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for(lista)

"""
Criando um iterador customizado

"""

#Replica do range
class contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


con = contador(1, 10)

print("\n")
for n in contador(1,10):
    print(n)

"""
Geradores

    - Geradores são iteradores, mas nem todo iterador é um gerador.
    - Geradores podem ser criados por funcoes geradoras, funcoes geradoras usam yield.
    
    Diferenças entre funções e generator functions:
    
    ----------------------------------------------------------------------------------------
    / Funções                                        /   Generator function
    ----------------------------------------------------------------------------------------
    / Utilizam return                                /   Utilizam yield 
    -----------------------------------------------------------------------------------------
    / Retorna uma vez                                /   Podem utilizar yield muitas vezes
    -----------------------------------------------------------------------------------------
    / Quando executada, retorna um valor            / Quando executada, retorna um gerador
    -----------------------------------------------------------------------------------------
    
"""


#Exemplo de generator function (Gastou 449mb)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador #Controla o while, executa o programa até a condição do while parar de ser verdade
        contador = contador + 1

gen = conta_ate(10)
print("\n")

for num in gen:
    print(num)


"""
Teste de memoria com generators.
#Sequecia de fibonacci
1,1,2,3,5,8,13  #1+1 = proximo valor (2)  2+1 = 3  3+2 = prox valor(5) ...

"""

def fib_lista(max):
    nums =[]
    a,b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

#Teste
print(fib_lista(10))

#Função usando geeradores (Gastou 3mb)

def fib_gen(max):
    a,b, contador = 0, 1, 0
    while contador < max:
        a,b = b, a + b
        yield a #Esta imprimindo o a
        contador = contador + 1

#teste
for n in fib_gen(10000):
    print(n)

"""
A quantidade de memoria gasta com o generator é bem menor que com uma função normal.
"""
