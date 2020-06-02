"""
Sistema de arquivos - Manipulação

"""

import os
import stat

# Descobrindo se um arquivo ou diretorio existe.

#Paths relativos
print(os.path.exists('arquivo.txt'))
print(os.path.exists('frutas.txt'))
print(os.path.exists('Meio do curso'))

#Paths absolutos
print(os.path.exists('C:\\Users\\andre\PycharmProjects\CursoPython\Aulas'))

#Criando arquivos

"""
os.mknod('arquivo4.txt')
"""

#Cria um diretorio
"""
os.mkdir('templates')
"""

#Criar varios diretorios de uma vez (se já tiverem todos os diretorios criados da erro)

#Esse exist é para não aparecer erro caso ja tenha criado os diretorios

"""
os.makedirs('templates/teste/outroteste', exist_ok=True)
"""

#Renomear um diretorio

"""
os.rename('templates', 'templates2')
"""

#Renomear arquivo é a mesma coisa

"""
os.rename('frutas.txt', 'cesta_de_frutas.txt')
"""

#Removendo um arquivo (o arquivo deletado some, NÃO vai para a lixeira)

"""
os.remove('novo.txt')
"""

#Removendo diretorios

"""
os.rmdir('templates')
"""

#Remover varios arquivos de uma vez
"""
for arquivo in os.scandir('templates2'):
    if arquivo.is_file():
        os.remove(arquivo.path)
"""

#Removendo varios diretorios VAZIOS de uma vez

"""
os.removedirs('templates2/teste/outroteste')
"""

#Enviando arquivos/diretorios para a lixeira

from send2trash import send2trash

"""
send2trash('teste_lixeira.txt')
"""

#Utilizando arquivos e diretorios temporarios

import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretorio temprario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Mapache god\n')
    #input()  #input para manter o codigo parado dentro do with, apos sair do with o arquivo e deletado


#criando um arquivo temporario

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')  #Tem q ser escrito em bits (binario)
    tmp.seek(0)
    print(tmp.name)
    #input()
#Em arquivos temporarios so conseguimos escrever bits. Por isso, utilizamos b


"""
https://docs.python.org/3/library/os.html
"""


