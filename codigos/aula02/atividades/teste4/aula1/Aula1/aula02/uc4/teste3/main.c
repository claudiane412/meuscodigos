#include <stdio.h>
#include <stdlib.h>

int main()
{
    char nome[45];
    int telefone,idade,idadeM,soma,quadrado;
    printf("informe seu nome: \n");
    scanf("%s\n",&nome);
    printf("informe seu telefone: \n");
    scanf("%d\n",&telefone);
    printf("informe sua idade: \n");
    scanf("%d\n",&idade);
    printf("informe a idade da sua mãe: \n");
    scanf("%d\n",&idadeM);
    soma =idade+idadeM;
    quadrado=soma*soma;

    printf("O nome do usuáro e:%s\n",nome);
    printf("O numero de telefone e:%d\n",telefone);
    printf("A idade do usuario e:%d\n",idade);
    printf("A idade da sua mãe e :%d\n",idadeM);
    printf("A soma das idades e :%d\n",soma);

    return 0;
}
