#include <stdio.h>
#include <stdlib.h>

int main()
{
    char nome [100];
    printf("qual seu nome?\n");
    scanf("%s",&nome);
    printf("Ola,seja bem vindo e um prazer te conhecer %s",&nome);
    return 0;
}
