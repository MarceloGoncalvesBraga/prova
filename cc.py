class Bibliotecario:
    def __init__(self, nome):
        self.nome = nome
        
class Cadastrar_livro(Bibliotecario):
    def __init__(self, nome, livro, ISBN, autor, edicao, editora, emprestimo):
        super().__init__(nome)
        self.livro = livro
        self.ISBN = ISBN
        self.autor = autor
        self.edicao = edicao
        self.editora = editora
        self.emprestimo = emprestimo
     def get_livro(self):
        return self.livro
     def get_isbn(self):
        return self.ISBN
     def get_autor(self):
        return self.autor
     def get_edicao(self):
        return self.edicao
     def get_editora(self):
        return self.editora
     def get_emprestimo(self):
        return self.emprestimo
Lista = [
Cadastrar_livro(nome='marcelo',livro='o livro', ISBN='2828', autor='marcelo', edicao='1998', editora='atlanta', emprestimo='27/03/2022',
Cadastrar_livro(nome='marcelo2',livro='o livro2', ISBN='2828', autor='marcelo', edicao='1998', editora='atlanta', emprestimo='27/03/2022'
]
