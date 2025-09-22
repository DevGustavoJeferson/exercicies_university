
Nota_1 = int(input('Digite a nota do primeiro bimestre: '))
Nota_2 = int(input('Digite a nota do segundo bimestre: '))
Nota_3 = int(input('Digite a nota do terceiro bimestre: '))
Nota_4 = int(input('Digite a nota do quarto bimestre: '))

#observe que utilizamos a função int(), pois, sem ela, o Python entenderia que as notas seriam String
 
#condição para a aprovação do aluno.

media = (Nota_1 + Nota_2 + Nota_3 + Nota_4) / 4

if media >= 6:

    situacao = "aprovado"

else:

    situacao = "reprovado"

 
#dadas as notas, mostramos a média final e a situação do aluno.

print(f"MEDIA = {media}")

print(f"SITUACAO = {situacao}")
