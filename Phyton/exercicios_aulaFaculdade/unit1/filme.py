filmes = ["Filme 1","Filme 2","Filme 3","Filme 4","Filme 5"]
avaliacoes = {}
for filme in filmes:
    classificacao = int(input(f"Classifique o {filme} entre 1 a 5 estrelas, caso nao queira classificao digite 0: "))
    while  classificacao not in [0,1,2,3,4,5]:
            print("Por favor, digite um valor entre 1 e 5, ou 0 para encerrar o programa")
            classificacao = int(input("Digite um valor correto dessa vez: "))
       
    if classificacao == 0:
        print("Que pena, o programa irá encerrar -_-!")
        break
    
    avaliacoes[filme] = classificacao 
    print(f"Voce avaliou o {filme} com {classificacao} estrelas") 


        