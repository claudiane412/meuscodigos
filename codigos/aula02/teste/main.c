#include <stdio.h>
#include <stdlib.h>

int main()
{   char comida[20];
    char cor[20];
    char signo[20];
    printf("qual sua comida favorita?\n");
    scanf("%s", &comida);
    printf("qual sua cor favorita?\n");
    scanf("%s",&cor);
    printf("qual o seu signo?\n");
    scanf("%s",&signo);
    printf("comida: %s\n",comida );
    printf("cor: %s\n",cor );
    printf("signo: %s\n",signo );
    return 0;
}
