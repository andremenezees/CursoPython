"""

Métodos mágicos, são todos os métodos que utilizam dunder(__).
ex de dunder: __init__

1 - (__repr__) ou (__str__)  str tem vantagem de ordem em relacao a repr -> Representa um objeto
"""

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


    #repr and str
    def __repr__(self):
        return f"Titulo: {self.titulo} Autor: {self.autor} paginas:{self.paginas} "


    #Len
    def __len__(self): #Definimos que ao utilizar len aparecera o numero de paginas
        return self.paginas

    #Deleta um objeto
   # def __del__(self):
        #print(f'Um objeto do tipo Livro foi deletado da memoria')

    #Juntar informacoes
    def __add__(self, outro):
        return f'{self} - {outro}'



livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligencia Artificial com python', 'Geek University', 350)

print(livro1)
print(livro2)


print('\n')
print(len(livro1))
print(len(livro2))

print('\n')
print(livro1 + livro2)


