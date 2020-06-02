"""
Dicionarios também são conhecidos como mapas em outras linguagens.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por {}.

Tuplas são bastante utilizadas nos dicionarios pois são imutaiveis


Chave e valor são separados por : --> 'chave:valor'.

#Forma 2 (menos comum)

paises = dict(br = 'Brasil', eua = 'Estados unidos', py = 'Paraguai')
print(paises)
print(type(paises))


"""

#Criação de dicionarios

paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'Py': 'Paraguai'}
print(paises)
print(type(paises))

#Acessando via chave, da mesma forma que lista e tuplas a chave é o indice:

print(paises['br'])

#Melhor forma de acessar:
print(paises.get('eua'))

#Verificando chaves:

print('br' in paises)
print('ru' in paises)
print('Estados unidos' in paises)

#Adicionando elementos no dicionario:

paises['arg'] = 'Argentina'
print(paises)

#Atualizando dados em um dicionario (Caso o dado nao seja tupla que é imutavel):
paises['Ch'] = 'Venezuela'
print(paises)
paises.update({'Ch': 'Chile'})
print(paises)

#Remover dados de um dicionario:

#Forma 1   (Neste caso é possivel retornar o valor)

ret = paises.pop('arg')
print(ret)
print(paises)

#Forma 2 (Neste caso nao retorna valor)

del paises['Ch']
print(paises)

#Aplicações

"""
Carrinho de compra:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        -nome;
        -quantidade;
        -preço;

Para fazer um carrinho de compras com dois produtos o dicionario é a forma mais facil
        
"""

carrinho = []
produto1 ={'nome': 'Playstation', 'quantidade': 1 ,'preço': 2300.00 }
produto2 ={'nome': 'GodOfWar', 'quantidade': 1 ,'preço': 150.00 }
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

d = {'a': 1, 'b': 2, 'c': 3}
print(type(d))
print(d)

#deep copy, copia não compartilhada
novo = d.copy()
novo['d'] = 4
print(d)
print(novo)

#shallow copy, copia compartilhada, se um é modificado o outro tbm é

d1 = {'a': 1, 'b': 2, 'c': 3}
print(d1)
novo1 = d1
novo1['d'] = 4
print(novo1)
print(d1)

#Interar em dicionarios( coloca o dicionario[chave] para pegar o valor da chave

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

for chave in receita:

    print(receita[chave])

#Uma forma simples de receber apenas as chaves
print(receita.keys())

#Forma simples de receber aspenas ums valores
print(receita.values())



