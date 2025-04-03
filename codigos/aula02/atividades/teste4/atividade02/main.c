#include <stdio.h>
#include <stdlib.h>

int main()
{
    #include <stdio.h>

int main() {
    float numero, sucessor, antecessor;

    printf("Digite um numero:\n");
    scanf("%f", &numero);

    sucessor = numero + 1;
    antecessor = numero - 1;

    printf("O sucessor desse numero e: %0.f\n", sucessor);
    printf("O antecessor desse numero e: %0.f\n", antecessor);

    return 0;
}


}
