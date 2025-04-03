#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
 float nota1, nota2, media;
    printf("Digite sua primeira nota!\n");
    scanf("%f", &nota1);
    printf("Digite sua segunda nota\n");
    scanf("%f", &nota2);

    media = (nota1 + nota2) / 2;

    if (media >= 7) {
        printf("Aprovado! A media foi: %.2f\n", media);
    } else {
        printf("Reprovado! A media foi: %.2f\n", media);
    }

    return 0;
}