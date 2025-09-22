#include <stdio.h>

int main()
{
    int integrantes;
    float desconto , valorBruto , valorLiquido;

    printf("Digite o valor total da comanda: \n");
    scanf("%f", &valorBruto);

    printf("Vai dividir a conta para quantas pessoas? \n");
    scanf("%d", &integrantes);

    printf("Qual será o desconto? \n");
    scanf("%f", &desconto);
    desconto = valorBruto * desconto;

    valorLiquido = (valorBruto - desconto) / integrantes;
    printf("O valor para cada pessoa é: %.2f" , valorLiquido);

    return 0;
}
