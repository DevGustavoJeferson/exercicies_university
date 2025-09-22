from math import sqrt
def dobrar(n):
    return n * 2

def quadrado(n):
    return n * n

def raiz(x):
    return sqrt(x)

def aplicar_funcao(func, lista):
    return [func(n) for n in lista]

print('bem vindo ao programa que faz a raiz, o quadrado e dobra quatro numeros seguidos que voce digitar (eu sei bem especifico kkkkkkk)...')

lista_de_numeros = [int(input('Digite um número: ')), int(input('Digite um número: '))
                    , int(input('Digite um número: ')), int(input('Digite um número: '))]

dobroLista = aplicar_funcao(dobrar, lista_de_numeros)
quadradoLista = aplicar_funcao(quadrado,lista_de_numeros)
raizLista = aplicar_funcao(raiz,lista_de_numeros)
print("Resultado(dobro) = ", dobroLista)
print("Resultado(quadrado) = ", quadradoLista)
print("Resultados(raiz) = ", raizLista)