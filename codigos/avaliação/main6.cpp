#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int num_macas;
	float preco_unitario,valor_total;
	printf("Digite o numero de maçãs compradas:\n");
	scanf("%d",&num_macas);
	if (num_macas <12){
		preco_unitario =0.30;
	}else}
		preco_unitario = 0.25;
	}
	valor_total = (num_marcas * preco_unitario);
	printf('O valor total da compa é: R$%.2f\n',valor_total);
	return 0;
}