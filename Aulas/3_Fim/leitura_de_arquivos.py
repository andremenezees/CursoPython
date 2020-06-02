arquivo = open('texto.txt')

ret = arquivo.read()
print(type(ret))
print(ret.split())

# A função read le todo o conteudo do arquivo. Então dois prints não funcionam
# pois le uma vez e o cursor vai para o final e não le mais.
