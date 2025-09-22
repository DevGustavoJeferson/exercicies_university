#include <stdio.h>

int main()
{
    int tv_2020, tv_2021, tv_2022;
    int noteb_2020, noteb_2021, noteb_2022;
    int smart_2020, smart_2021, smart_2022;

    float media_2020 = 0;
    float media_2021 = 0;
    float media_2022 = 0;

    printf("digite a quantidade de tvs vendidas respectivamente no ano de 2020, 2021 e 2022: ");
    scanf("%d", &tv_2020);
    scanf("%d", &tv_2021);
    scanf("%d", &tv_2022);

    printf("\n digite a quantidade de notebooks vendidos respectivamente no ano de 2020, 2021 e 2022: ");
    scanf("%d", &noteb_2020);
    scanf("%d", &noteb_2021);
    scanf("%d", &noteb_2022);

    printf("\n digite a quantidade de Smartphones vendidos respectivamente no ano de 2020, 2021 e 2022: ");
    scanf("%d", &smart_2020);
    scanf("%d", &smart_2021);
    scanf("%d", &smart_2022);

    media_2020 = (tv_2020 + noteb_2020 + smart_2020) / 3;
    media_2021 = (tv_2021 + noteb_2021 + smart_2021) / 3;
    media_2022 = (tv_2022 + noteb_2022 + smart_2022) / 3;

    printf("\n A media de 2020 é: %f" , media_2020);
    printf("\n A media de 2021 é: %f" , media_2021);
    printf("\n A media de 2022 é: %f" , media_2022);

    printf("\n 2020 obteve a maior media? %d", ((media_2020 > media_2021) && (media_2020 > media_2022)));
    printf("\n 2020 obteve a maior media? %d", ((media_2021 > media_2020) && (media_2021 > media_2022)));
    printf("\n 2022 obteve a maior media? %d", ((media_2022 > media_2021) && (media_2022 > media_2020)));
    return 0;
}
