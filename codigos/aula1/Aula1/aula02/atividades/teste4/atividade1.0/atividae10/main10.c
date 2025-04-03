#include <stdio.h>
#include <stdlib.h>

int main()
{
    float largura,altura,area,quantidade;
    printf("digite a largura da parede em metros:\n");
    scanf("%f",&largura);
    printf("Digite a altura em metros:\n");
    scanf("%f",&altura);
    area = largura * altura;
    quantidade =area/2;
    printf("A area a ser pintada e:%.2f metros quadrados\n",area);
    printf(" A quantidade de tinta necessariae de:%0.f litros\n",quantidade);
    return 0;
}
