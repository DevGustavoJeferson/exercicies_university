pessoa = {"nome":'Gustavo', "idade" : 0 , "cidade":'Rio Preto'}
pessoa["Profissão"] = "Açougueiro"
pessoa["idade"] = int(input("Atualize a sua idade: "))

for chave,valor in pessoa.items():
    print(f"{chave} : {valor}")