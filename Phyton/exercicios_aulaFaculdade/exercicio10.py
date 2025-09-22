import matplotlib.pyplot as plt

meses = ['Janeiro','Fevereiro','Março','Abril','Maio']
vendas = [100,150,160,200,250]

plt.bar(meses,vendas, color = "black")

plt.xlabel("Mes")
plt.ylabel("Vendas em (Unidades)")

plt.title("VENDA MENSAL")
plt.show()
