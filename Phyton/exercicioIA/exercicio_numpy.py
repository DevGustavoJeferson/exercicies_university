import numpy as np
notas = {
    "Ana": [7, 8, 9],
    "Pedro": [6, 5, 7],
    "Maria": [10, 9, 8]
}

for chave ,valor in notas.items():
    media = np.median(valor)
    if media > 6.0:
        print(f"{chave} = APROVADO(A)")
    else:
        print(f"{chave} = REPROVADO")

#FUNCIONALIDADES NUMPY

a = np.array([1, 2, 3])                # array a partir de lista
b = np.zeros((2, 3))                   # matriz 2x3 só com zeros
c = np.ones((2, 2))                    # matriz 2x2 só com uns
d = np.arange(0, 10, 2)                # [0 2 4 6 8]
e = np.linspace(0, 1, 5)               # [0. 0.25 0.5 0.75 1.]

arr = np.array([1, 2, 3, 4, 5])

print(arr + 10)     # soma 10 em todos -> [11 12 13 14 15]
print(arr * 2)      # multiplica todos -> [2 4 6 8 10]
print(arr ** 2)     # quadrado -> [1 4 9 16 25]

mat = np.array([[1, 2], [3, 4]])
print(mat.T)          # transposta
print(np.sum(mat))    # soma todos os elementos
print(np.sum(mat, axis=0))  # soma por coluna
print(np.sum(mat, axis=1))  # soma por linha

print(np.random.randint(0, 10, size=5))   # 5 números inteiros de 0 a 9
print(np.random.rand(2, 3))               # matriz 2x3 com valores [0,1)
    