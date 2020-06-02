"""
1) Escreva um programa que:
a) Crie/abra um arquivo texto de nome "arq.txt".
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que
o usuario entre com o caractere '0'.
c) Feche o arquivo.
d) Abra e leia o arquivo caractere por caractere, e escreva na tela todos
os caracteres armazenados
"""

"""
with open("arq.txt", 'w') as arquivo:
    while True:
        caract = str(input(("Digite o caractere:")))
        if caract == '0':
            break
        else:
            arquivo.write(caract)
            arquivo.write('\n')



with open("arq.txt", 'r') as arq:

    lendo = arq.read()
    print(lendo)
"""


"""
2) Faça um programa que receba do usuario um arquivo texto e mostre na
tela quantas linhas esse arquivo possui.

"""
"""
with open("Seção13-questao2.txt", 'w') as arquivo:
    while True:
        caract = str(input(("Digite o texto e 0 para sair:")))
        if caract == '0':
            break
        else:
            arquivo.write(caract)
            arquivo.write('\n')

with open("questao2.txt", 'r') as arquivo:
    linhas = arquivo.readlines()
    print(f'Numero de linhas: {len(linhas)}')

"""

"""
3) Faça um programa que receba do usuario um arquivo texto e mostre na
tela quantas letras são vogais e quantas são consoantes.

"""

"""
with open("Seção13-questao3.txt", 'w') as arquivo:
    while True:
        caract = str(input(("Digite o texto e 0 para sair:")))
        if caract == '0':
            break
        else:
            arquivo.write(caract)


with open("Seção13-questao3.txt", 'r') as arquivo:
    contador = 0
    contador2 = 0
    arq = arquivo.read()
    for cont in range(0, len(arq)):
        if arq[cont] == 'a' or arq[cont] == 'e' or arq[cont] == 'i' or arq[cont] == 'o' or arq[cont] == 'u':
            contador = contador + 1
        else:
            contador2 = contador2 + 1
            
    print(f'Numero de vogais:{contador}')
    print(f'Numero de consoantes:{contador2}')
    
"""

"""
11) Faça um programa no qual o usuario informa o nome do arquivo e uma
palavra, e retorne o numero de vezes que aquela palavra aparece no arquivo.

"""

"""
inform = str(input("Digite o arquivo a ser aberto com .txt:"))
palavra = str(input("Digite a palavra a ser procurada:"))

with open(inform, 'r') as arq:
    cont = 0
    for i in arq.read().split():
        if str(i) == palavra:
            cont = cont + 1
    print(f'O numero de vezes que a palavra "{palavra}" aparece no texto é de {cont}')

"""


"""
14) Dado um arquivo contendo um conjunto de nome e data de nascimento(DD MM AAAA,
isto é, 3 inteiros em sequencia) faça um programa que leia o nome do arquivo
e a data de hoje e construa outro arquivo contendo o nome e a idade de cada
pessoa do primeiro arquivo.

"""


"""
total = str(input("Digite o dia de hoje com espaço(ex: 10 05 1996):"))
ano = total.split()

with open('datas_de_nascimento.txt', 'r') as aniv:
    anivlist = list(aniv)
    newarq = open('new_datas_de_nascimento.txt', 'w')
    for i in range(len(anivlist)):
        n = anivlist[i].split()
        

        if ano[1] >= n[2]:
            idade = int(ano[2]) - int(n[3])

        if ano[1] < n[2]:
            idade = (int(ano[2]) - int(n[3])) - 1

        idadestr = str(idade)

        newarq.write(f"nome:{n[0]} idade:{idadestr}")
        newarq.write('\n')

    newarq.close()

"""


"""
15) Faça um programa que receba como entrada o ano corrente e o nome de dois
arquivos: um de entrada e outro de saida. Cada linha do arquivo de entrada
contém o nome de uma pessoa( ocupando 40 caract) e o seu ano de nascimento.
O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde
aparece o nome da pessoa seguida por uma string que representa a sua idade.
    - Se a idade for menor que 18 anos, escreva "menor de idade".
    - Se a idade for maior que 18 anos, escreva "maior de idade".
    - Se a idade for igual a 18 anos, escreva "entrando na maioridade".
"""

"""
total = str(input("Digite o dia de hoje com espaço(ex: DD MM AAAA):"))
entrada = str(input('Digite o arquivo de entrada:'))
saida = str(input('Digite o arquivo de saida:'))
ano = total.split()


with open(entrada, 'r') as arqentrada:
    arqlist = list(arqentrada)
    newarq = open(saida, 'w')
    for i in range(len(arqlist)):
        n = arqlist[i].split()

        if ano[1] >= n[2]:
            idade = int(ano[2]) - int(n[3])

        if ano[1] < n[2]:
            idade = (int(ano[2]) - int(n[3])) - 1

        idadestr = str(idade)

        if idade < 18:
            newarq.write(f"Nome: {n[0]} e menor de idade pois sua idade e :{idadestr}")
            newarq.write('\n')

        if idade > 18:
            newarq.write(f"Nome: {n[0]} e maior de idade pois sua idade e :{idadestr}")
            newarq.write('\n')

        if idade == 18:
            newarq.write(f"Nome: {n[0]} esta entrando na maioridade pois sua idade e :{idadestr}")
            newarq.write('\n')


   newarq.close()

"""


"""
18) Faça um programa que leia um arquivo contendo o nome e o preço de
diversos produtos (separados por linha), e calcule o total da compra.

"""

"""
with open('arquivo_questao_18.txt', 'r') as arq_18:

    listarq = list(arq_18)
    total = 0
    for i in range(len(listarq)):
        n = listarq[i].split(':')
        preco = n[1].split()

        #prec = x[0]
        for i, x in enumerate(preco):

            if i % 2 != 0:
                print(x)
                total = total + float(x)
    print(total)

"""

"""
25) Faça um programa gerenciar uma agenda de contatos. Para cada contato armazene
o nome, o telefone e o aniversário (dia e mes). O programa deve permitir:

a) Inserir contato.
b) Remover contato.
c) Pesquisar um contato pelo nome.
d) Listar todos os contatos.
e) Listar os contatos cujo nome inicia com uma dada letra.
f) Imprimir os aniversariantes do mes.

Sempre que o programa for encerrado, os contatos devem ser armazenados em um
arquivo binário. Quando o programa iniciar, os contatos devem ser inicializados
com os dados contidos neste arquivo binário.

"""
inicio = int(input("Para inserir um novo contato digite: 1.\n"
                   "Para remover digite : 2 \n "
                   "Para pesquisar um contato pelo nome digite: 3. \n"
                   "Para listar todos os contatos digite: 4. \n"
                   "Para listar os contatos a partir da letra inicial digite: 5. \n"
                   "Para listar os aniversariantes do mes digite: 6 \n"
                   "Digite aqui:"))

if inicio == 1:

    #Inserir contato
    with open('agenda_quest_25.txt', 'r') as agend:
        linhas = agend.readlines()

    with open('agenda_quest_25.txt', 'a') as agend:
        print("Voce escolheu a opção 1, inserir contato.\n")

        inserir = str(input('Para inserir contato digite o nome, telefone e aniversario:'))
        print('\n')
        cont = 0
        ins = inserir.split()
        for i, n in enumerate(ins):
            nome = ins[0]
            tel = ins[1]
            aniv = ins[2]

        for linha in linhas:
            palavrasdalinha = linha.split()

            for palavra in palavrasdalinha:
                if palavra == nome:
                    cont = 1
                    print("Ja possui este contato, portanto não será adicionado.")
                    break

        if cont == 0:
            agend.write("\n")
            agend.write(f"nome: {nome} telefone: {tel} aniversario:{aniv}\n")


if inicio == 2:

    #Remover contato

    with open('agenda_quest_25.txt', 'r') as agend:
        linhas = agend.readlines()

        with open('agenda_quest_25.txt', 'w') as agend:
            nome = str(input("Digite o nome do contato a ser deletado:"))
            cont = 0
            for linha in linhas:
                palavrasdalinha =linha.split()

                for palavra in palavrasdalinha:
                    if palavra == nome:
                        cont = cont + 1
                        linha = ""

                agend.write(linha)

        if cont != 0:
            print("Agenda atualizada com sucesso.")

        if cont == 0:
            print("Não foi encontrado nenhum contato com esse nome.")


if inicio == 3:
    #Pesquisar um contato pelo nome

    with open('agenda_quest_25.txt', 'r') as agend:
        print("Voce escolheu a opção 3, pesquisar contato pelo nome.\n")

        contatos = agend.read().split()
        contat = str(input("Digite o contato a ser pesquisado:"))
        print('\n')

        print(f"Dados do contato {contat.title()}:")
        cont = 0
        for i, x in enumerate(contatos):
            if contatos[i] == contat:
                cont = cont + 1
                nome = contatos[i]
                tel = contatos[i+2]
                aniv = contatos[i+4]
                print(f"Nome: {nome.title()} telefone: {tel} aniversario: {aniv}")
        if cont == 0:
            print("Não foi encontrado nenhum contato com esse nome.")



if inicio == 4:
    #Listar todos os contatos

    with open('agenda_quest_25.txt', 'r') as agend:
        print("Voce escolheu a opção 4, listar todos os contatos\n")

        agend.seek(0)
        ler = agend.read()
        print(ler)


if inicio == 5:
    #Listar os contatos cujo nome inicia com uma dada letra

    with open('agenda_quest_25.txt', 'r') as agend:
        print("Voce escolheu a opção 5, listar contatos a partir de uma letra.\n")
        print("\n")
        contatos = agend.read().split()
        inic = str(input(("Digite a letra inicial do contato:")))
        print('\n')
        print(f"Contatos com letra {inic.title()} :")
        cont = 0
    
        for i, x in enumerate(contatos):
            if contatos[i] == 'nome:':
                letra = contatos[i+1][0]

                if letra == inic:
                    cont = cont + 1
                    nome = contatos[i+1]
                    tel = contatos[i+3]
                    aniv = contatos[i+5]
                    print(f"Nome: {nome.title()} telefone: {tel} aniversario: {aniv}")
                
        if(cont == 0):
            print("Não foi encontrado nenhum contato com essa inicial.")


if inicio == 6:
    #Imprimir os aniversariantes do mes.

    with open('agenda_quest_25.txt', 'r') as agend:
        print("Voce escolheu a opção 6, imprimir os aniversariantes do mes.\n")

        contatos = agend.read().split()
        data = str(input("Digite o mes q deseja pesquisar os aniversarios:"))
        print('\n')
        print("Aniversariantes do mes:")
        cont = 0
        for i, x in enumerate(contatos):
            if contatos[i] == 'aniversario:':
                aniversarios = contatos[i+1].split('/')[1]
                #aniversarios = str(contatos[i+1][3] + contatos[i+1][4])
                if aniversarios == data:
                    cont = cont + 1
                    nome = contatos[i-3]
                    tel = contatos[i-1]
                    aniv = contatos[i+1]
                    print(f"Nome: {nome.title()} telefone: {tel} aniversario: {aniv}")

        if (cont == 0):
            print("Não foi encontrado nenhum contato que faz aniversario neste mes.")



