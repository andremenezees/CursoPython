"""
Sistema de arquivos e navegação.

para fazer uso de manipulação de arquivos do sistema operacional, precisamos
importar e fazer uso do modulo os.

os -> Operation System - Sistema Operacional.

"""

#fazer o import

import os

#getcwd() -> Pega o current work directory. Diretorio de trabalho corrente
#Retorna o path (caminho) absoluto

print(os.getcwd())

#para mudar o diretorio, podemos utilizar o chdir(), chdir(..) volta um diretorio.

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())





#Podemos checar se um diretorio é absoluto ou relativo.

#No windows
print(os.path.isabs( 'C:\\Users\\sistema_de_arquivos_navegacao.py '))

#Podemos identificar o sistema operacional com o modulo OS.
print(os.name)     #posix = linux ou Mac    nt = Windows

#Podemos ter mais detalhes do sistema operacional
#print(os.uname())  #Para aparecer mais detalhes no POSIX

import sys
print(sys.platform)

import os

#Criando um arquivo através do python

print(os.getcwd())  #Printa o diretorio atual

#Serve para juntar dois diretorios, ou seja avança para o diretorio escolhido caso ele esteja no diretorio atual
res = os.path.join(os.getcwd(), 'TesteParaPython')
os.chdir(res)
print(os.getcwd())

#Podemos listar os arquivos e diretórios com o listdir()
os.chdir('..')
print(os.getcwd())  #Printa o diretorio atual em q o OS se encontra
print(' ')
test1 = os.listdir()
print(f'Arquivos do diretorio C:\ Users\ andre : {test1}') #Lista os arquivos que estão no diretorio em q o OS se encontra
print(' ')

#Ver quantos arquivos tem no diretorio raiz do seu OS

test = os.listdir('C:\\')
print(f'Arquivos do diretorio raiz: {test}')
print(' ')

#Podemos listar arquivos e diretorios com mais detalhes com scandir()
scanner = os.scandir('C:\\')
arquivos = list(scanner) #Escaneia os arquivos de um diretorio escolhido
print(arquivos)
print(' ')

print(f'Dir aqui: {dir(arquivos[0])}')
print(' ')

print(arquivos[0].inode()) #??
print(arquivos[0].is_dir()) # É um diretorio? True
print(arquivos[0].is_file()) # É um arquivo? False
print(arquivos[0].is_symlink()) # É um link simbolico? False
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) #Caminho até o arquivo
print(arquivos[0].stat()) #Estatisticas do arquivo

#Quando utilizamos a funcao scandir() nós precisamos fechar

scanner.close()