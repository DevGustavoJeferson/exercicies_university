//calcular o preço final de um produto com base no preço
//de venda, impostos e descontos aplicáveis.

#include <stdio.h>

int main(){
    const float taxaImposto = 0.1F;
    const float descontoProduto = 0.05F;

    float vendaProduto, precoFinal, valorImposto , valorDesconto;
    printf("digite o valor do produto: ");
    scanf("%f" , &vendaProduto);

    valorImposto = vendaProduto * taxaImposto;
    valorDesconto = vendaProduto * descontoProduto;
    precoFinal = vendaProduto + valorImposto - valorDesconto;

    printf("valor final = %2.f" , precoFinal);

    return 0;
}