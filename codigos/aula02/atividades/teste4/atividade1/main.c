#include <stdio.h>
#include <stdlib.h>

int main()
{
    char nome[30],bairro[20],cidade[30];
    int telefone;
    printf("ola estou programando em linguagem c \n");
    scanf("%s");
    printf("informe seu nome:\n");
    scanf("%s",&nome);
    printf("informar seu telefone:\n");
    scanf("%i",&telefone);
    printf("informe seu bairro:");
    scanf("%s",&bairro);
    printf("informe sua cidade:");
    scanf("%s",&cidade);

    printf("Meu nome e:%s\n",&nome);
    printf("meu telefone e:%i\n",&telefone);
    printf("meu bairro e:%s\n",&bairro);
    printf("minha cidade e:%s\n",&cidade);
    printf("E irei trabalhar com poo!!!");
    return 0;
}
