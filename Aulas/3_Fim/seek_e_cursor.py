"""
A função seek serve para movimentar o cursor pelo arquivo.

"""

arquivo = open('texto.txt')

print(arquivo.read())

print(f'a:{arquivo.read()}')

#movimentando o cursor pelo arquivo com a função seek().
#A função seek() recebe um parametro para informar a posição do cursor.

#Estamos lendo apartir do caracter 14.

arquivo.seek(14)
print(f'b:{arquivo.read()}')

#ReadLine() -> Função que le o arquivo linha a linha.
arquivo.seek(0) #Faz o cursor ir para 0
print(f'c:{arquivo.readline().split()}')  #Primeira linha, pois o cursor esta em 0
print(f'c:{arquivo.readline()}') #Segunda linha.

#Para ler a quantidade de linhas
arquivo = open('texto.txt')


#Readlines le todas as linhas
linhas = arquivo.readlines()
print(linhas)
print(len(linhas))


#Para escolher uma certa quantidade de caracteres para serem lidos.
arquivo.seek(0)
print(arquivo.read(15)) #Lendo os 15 primeiros caracteres.

"""
Quando é aberto um arquivo com open() é criada uma conexão entre o arquivo
e o programa. Essa conexão é chamada streaming, portanto ao finalizar os 
trabalhos é necessario fechar essa conexão, através do close().

Passos para trabalhar com arquivo.
1 - Abrir o arquivo. open()
2 - Utilizar o arquivo.
3 - Fechar o arquivo. close()

"""

arquivo.close()


"""
Bloco With:

    O bloco with é utilizado para criar um contexto de trabalho onde os
recursos utilizados são fechados após o bloco with.

"""

#Utilizando block with
#O bloco with abre e fecha o nosso arquivo, portanto é a forma mais utilizada.
#Apos sair do bloco with o arquivo será fechado, então para utiliza-lo novamente tera q ser reaberto.


with open('texto.txt', 'r') as arquivo:
    print(arquivo.readlines())

"""
Escrevendo em um arquivo, para abrir um arquivo de escrita precisa deixa-lo
em modo 'w'.

#Ao abrir um arquivo com 'w' se o arquivo não existir será criado, se já existe
será apagada o existente e criado um novo.

"""

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrevendo dados em um novo arquivo.\n')
    arquivo.write('Proxima linha do novo arquivo')
    arquivo.write('  Escrevendo na mesma linha.\n')
    arquivo.write('Ultima linha')

"""
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = str(input("Informe uma fruta ou digite sair:"))
        if fruta == 'sair':
            break
        else:
            arquivo.write(fruta)
            arquivo.write('\n')

"""


"""
Modos de abertura de Arquivos.

r -> Abre para leitura - padrão
w -> Abre para escrita, caso exista ja um abri ele sobreescreve.
x -> Abre para escrita somente se o arquivo não existir.
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualizaçãom leitura e escrita.
Por comando não é possivel adicionar no topo.

"""

#Exemplo com x

try:
    with open('testandoarquivos.txt', 'x') as arquivo:
        arquivo.write('Testando arquivo x\n')
except FileExistsError:
    print('Arquivo já existe')

#Exemplo com A (sempre é adiconado no final do arquivo)
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = str(input("Informe uma fruta ou digite sair:"))
        if fruta == 'sair':
            break
        else:
            arquivo.write(fruta)
            arquivo.write('\n')

"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional
o software precisa ter permissão:
    - Permissão de leitura -> Para ler o arquivo.
    - Permissão de escrita -> Para escrever o arquivo.
    
StringIO -> Utilizado para ler e criar arquivos em memória.

"""

#Primeiro fazemos o import

from io import StringIO

mensagem = 'Esta é apenas uma string normal\n'

arquivo = StringIO(mensagem) #Serve para criar um arquivo temporario.

print(arquivo.read())


arquivo.write('Testando stringIO\n')
arquivo.seek(0)
print(arquivo.read())
