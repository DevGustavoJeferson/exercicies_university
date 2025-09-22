a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"União entre a e b = {a | b}")
print(f"Interseção entre a e b = {a & b}")
print(f"Diferença entre a e b = {a - b}")
print(f"Diferença simétrica entre a e b = {a ^ b}")

a.remove(1)
a.add(int(input("Adicione um número: ")))
item = 3
if item in a:
     print("Sim o item está em a")

