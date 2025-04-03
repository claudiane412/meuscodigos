#include <stdio.h>
#include <stdlib.h>

int main()
/* quais sao as variaveis da linguagem C int numeros inteiros,
float numeros com casas decimais representado com até 7 digitos
double numeros decimais até com 14 digitos char para caracter*/
{
float n1,n2,soma;
    printf("Digite o primeiro numero a ser somado\n");
    scanf ("%f", &n1);
    printf("Digite o segundo numero a ser somado\n");
    scanf ("%f", &n2);
    // a variavel soma vai receber as variaveis n1 e n2;
    soma = n1+n2;
    printf("A soma dos  valores é:%.2f",soma);
    return 0;
}
