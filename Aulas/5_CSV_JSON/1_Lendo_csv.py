"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores seperados por virgula

#Seperador por virgula
1, 2, 3, 4, 5, 6

"Geek", "University", "python",  "ciencia", "dados"

#Sepador por ponto e virgula

#Seperador por virgula
1; 2; 3; 4; 5; 6

"Geek"; "University"; "python"; "ciencia"; "dados"

#Site para pegar dados
dados.gov.br/dataset


"""
#Tratar dados em csv

#Reader

from csv import reader

with open('lutadores.csv','r', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) #Serve para pular uma linha
    for linha in leitor_csv:
        print(f"{linha[0]} nasceu em {linha[1]} e mede {linha[2]} cm")


#DictReader (Outra forma de ler arquivo em CSV)

from csv import DictReader

with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
    print('\n')
    arquivo.seek(0)
    leitor_csv = DictReader(arquivo) #Os elementos são acessados conforme o cabeçalho do arquivo
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']} cm")



#DictReader com outro separador

from csv import DictReader

with open('lutadores.csv', 'r', encoding='utf-8') as arquivo:
    print('\n')
    arquivo.seek(0)
    leitor_csv = DictReader(arquivo, delimiter=',') #Especificando , como separador
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']} cm")
