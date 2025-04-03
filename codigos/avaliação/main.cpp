#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	#include <stdio.h>

float calcular_peso_ideal(float altura, int sexo) {
    float peso_ideal;
    if (sexo == 1) {
        peso_ideal = (62.1 * altura) - 44.7;
    } else if (sexo == 2) {
        peso_ideal = (72.7 * altura) - 58;
    } else {
        printf("Código de sexo inválido! Use 1 para feminino e 2 para masculino.\n");
        return -1;
    }
    return peso_ideal;
}

int main() {
    float altura, peso_ideal;
    int sexo;
    
    printf("Digite a altura (em metros): ");
    scanf("%f", &altura);
    printf("Digite o sexo (1 para feminino, 2 para masculino): ");
    scanf("%d", &sexo);
    
    peso_ideal = calcular_peso_ideal(altura, sexo);
    
    if (peso_ideal != -1) {
        printf("O peso ideal é %.2f kg.\n", peso_ideal);
    }
    



	return 0;
}