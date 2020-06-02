"""
Erros mais comuns em python

1- Syntaxe error -> Ocorre quando  python encontra um erro na sua escrita, ou seja
voce escreveu algo que o python não reconhece como parte da linguagem.

2- NameError -> Ocorre quando uma variável ou função não foi definida. Por exemplo
ao tentar imprimir uma variavel que não existe, ou uma variavel que esta dentro
de uma estrutura porém a condição para acessar essa variavel nunca será satisfeita.

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro
tipo de dado indexado utilizando um indice invalido.

5 - Value Error -> Ocore quando uma função/operação recebe um argumento com tipo
correto mas valor inapropriado.

6 - KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que
não existe.

7 - AttributeError -> Ocorre quando uma variavel não tem um atributo/função. Tentar
usar uma função que só funciona em listas em outra função.
Exemplo:
tupla = (1,545,3,2)
tupla.sort()  # Função sort só funciona em listas.

#TypeError

print('Mapache' + 4)  #print('Mapache' + '4')

#Exemplo indexError(Acesasr um elemento que não existe)

lista = ['asdasda']
print(lista[3])

"""

"""
Levantando os proprios erros com raise.

Raise serve para escrever o proprio erro.

"""


# exemplo raise

def colore(texto, cor):
    cores = ('Verde', 'Azul', 'Branco', 'Preto', 'Vermelho')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor.title() not in cores:
        raise ValueError(f'Precisa escolher uma cor entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor.title()}')


colore('Mapache', 'azul')

"""
try e except

Serve para aparecer uma mensagem de erro escolhida pelo criador do programa ao 
inves dos erros normais do sistema. Utilizado para aplicações, caso o usuario
digite algo errado ao inves de aparecer 'TypeError' e outra error em vermelho
aparecera a mensagem escolhida pelo criador do programa.

Finally -> O finally sempre é executado, é utlizando para enviar uma mensagem
final que sempre ira aparecer, como obrigado.
"""

#Exemplo 1 - tratando um erro generico.

try:
    mapache()
except:
    print("Deu algum erro.")

#Exemplo 2 - Tratando erro especifico. Mais recomendado

try:
    Mapache()
except NameError:
    print('Voce está utilizando uma função inexistente.')

#Exemplo 3

try:
    len(5)
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')

try:
    mapache(5)
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')

mapache = 11
try:
    print('Mapache'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')
finally:
    print('O finally sempre é executado.')

#Exemplo mais complexo

#Mais recomendado

"""
def dividir(a, b):
    try:
        return int(a)/int(b)
    except ValueError:
        return('Valor incorreto, digite um numero inteiro.')
    except ZeroDivisionError:
        return 'Não é possivel realizar divisões por zero.'


num1 = input('Digite o primeiro numero:')
num2 = input('Digite o segundo numero:')

print(dividir(num1, num2))

"""


"""
#Outra forma de tratar os erros de forma mais geral.

def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError, NameError) as err:
        return(f'Ocorreu um erro: {err}')



num1 = input('Digite o primeiro numero:')
num2 = input('Digite o segundo numero:')

print(dividir(num1, num2))
"""

#Debuggando com PDB

#Comandos básicos do PDB.
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)


nome = 'Maicon'
sobrenome = 'Jordan'

import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
profissao = 'Jogador de basquete'
final = nome_completo + ' ' + 'é' + ' ' + profissao
print(final)




