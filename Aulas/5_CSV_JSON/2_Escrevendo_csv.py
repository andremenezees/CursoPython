
# -*- encoding: utf-8 -*-

"""

Escrevendo em CSV

reader() (leitor), writer() (escritor)

writerow()  -> Escreve uma linha

"""

"""
from csv import writer

#Atraveves do writerrow e possivel escrever uma linha
with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Genero', 'Duração'])#Cabeçalho
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duração(em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
"""

#DictWriter (as chaves do cabeçalho devem ser as mesma do titulo.)

from csv import DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Genero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None

    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duracao(em minutos): ')
            escritor_csv.writerow({"Título": filme, "Genero": genero, "Duração": duracao})
