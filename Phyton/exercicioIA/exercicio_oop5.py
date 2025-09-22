class libre:
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def detalhes(self):
        return f"TITULO = {self.titulo} \n AUTOR = {self.autor} \n PAGINAS = {self.paginas}"
    def eh_grande(self):
        if self.paginas > 300:
            return True

livro = libre("PROGRAMACAO","GUSTAVO",310)
print(livro.detalhes())
print(livro.eh_grande())