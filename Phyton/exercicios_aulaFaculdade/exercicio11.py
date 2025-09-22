import matplotlib.pyplot as plt

# Classe para representar um livro

class Livro:

    def __init__(self, titulo, autor, ano_publicacao):

        self.titulo = titulo

        self.autor = autor

        self.ano_publicacao = ano_publicacao

 

    def __str__(self):

        return f"{self.titulo} por {self.autor}, Publicado em {self.ano_publicacao}"

 

# Criar uma lista de livros

biblioteca = []
anos = []

# Função para adicionar um livro à biblioteca

def adicionar_livro(titulo, autor, ano_publicacao):

    novo_livro = Livro(titulo, autor, ano_publicacao)

    biblioteca.append(novo_livro)

    print(f"{titulo} foi adicionado à biblioteca.")

# Função para listar todos os livros na biblioteca

def listar_livros():

    print()

    for livro in biblioteca:

        print(livro)

# Adicionar alguns livros à biblioteca

adicionar_livro('a','b', 1605)

adicionar_livro('a','v', 1813)

adicionar_livro('a','a', 1949)

adicionar_livro('a','a', 1967)

adicionar_livro('b','c', 1951)

 

# Listar todos os livros na biblioteca

listar_livros()

# Criar um gráfico de livros por ano

anos = list(set(anos))# Remove duplicatas dos anos

anos.sort()

 

# Contagem de livros por ano

contagem_por_ano = [anos.count(ano) for ano in anos]

 

# Criar um gráfico de linha

plt.plot(anos, contagem_por_ano, marker='o', linestyle='-')

plt.xlabel('Ano de Publicação')

plt.ylabel('Número de Livros')

plt.title('Distribuição de Livros na Biblioteca por Ano de Publicação')

 

# Adicionar rótulos aos pontos de dados

for i, valor in enumerate(contagem_por_ano):

    plt.text(anos[i], valor, str(valor), ha='center', va='bottom')

 

plt.grid(True)

 

plt.show()