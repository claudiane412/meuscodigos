#include <stdio.h>
#include <stdlib.h>

int main()
{
float metros,milimetro,centimetro,decimentro;
    printf("Digite o valor em metros\n");
    scanf("%f", &metros);
    milimetro = metros * 1000;
    centimetro = metros *100;
    decimentro= metros *10;
    printf("%.0f o valor de milimetro e:",milimetro);
    printf("%.0f o valor de centimetro e:",centimetro);
    printf("%.0f o valor de decimentro e:",decimentro);

    return 0;
}
