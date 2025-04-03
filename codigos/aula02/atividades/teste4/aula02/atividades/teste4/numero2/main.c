#include <stdio.h>
#include <stdlib.h>

int main()
{
    int sucessor,sucessor,antecessor,soma;
    printf("digite um numero\n");
    scanf("%i",&num);
    printf("informe o numero sucessor\n");
    scanf("%i",&sucessor);
    printf("informe o numero antecessor\n");
    scanf("%i",&antecessor);
    soma1 =  num+sucessor;
    soma2 = num + antecessor;

    printf ("informe o numero do usuario e:%i\n",num);
    printf("o numero sucessor e:%i\n"sucessor);
    printf("O numero antecessor e:%i\n",antecessor);
    printf("a soma do sucessor e:%i\n "soma1);
    printf("a soma do antecessor e:%i\n"soma2);
    return 0;
}
