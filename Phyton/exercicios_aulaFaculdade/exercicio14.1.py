import pandas as pd

exemplo = [10,20,30,40,50]

series1 = pd.Series(data = exemplo)
print(series1)
print(exemplo)

profissao = {'Gustavo':24,'Sarah':23,'Jessica':20}
series2 = pd.Series(data=profissao)
print(series2)