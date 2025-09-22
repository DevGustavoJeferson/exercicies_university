notas = [float(input('Digite a primeira nota: ')), float(input('Digite a segunda nota: '))
         ,float(input('Digite a terceira nota: ')), float(input('Digite a quarta nota: '))]

def calcular_media(notas):

    total = sum(notas)

    media = total / len(notas)

    return media

arredondar_media = lambda media: round(media, 1)

media = calcular_media(notas)

media_arredondada = arredondar_media(media)

if media_arredondada >= 7:
    situacao = "Aprovado" 
else:
    situacao = "Reprovado"
 
print(notas)
print(media_arredondada)
print(situacao)