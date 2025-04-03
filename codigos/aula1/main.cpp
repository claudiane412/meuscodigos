#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int i,j;
	printf("tabuada de 1 a 9:\n");
	for(i=1;i<=9;i++){
		printf("tabuada do%d:\n",i);
		for(j=1; j<=10; j++){
			printf("%dx %d=%d\n",i,j,i*j);
			}
		printf("\n");
		
return 0;
