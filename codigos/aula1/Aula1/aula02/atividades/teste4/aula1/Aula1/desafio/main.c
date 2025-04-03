#include <stdio.h>
#include <stdlib.h>

int main()
{
float n1,n2,n3,media;
    printf("digite a primeira nota\n");
    scanf("%f",  &n1);
    printf("digite a segunda nota\n");
    scanf("%f", &n2);
    printf("digite a terceira nota\n");
    scanf("%f", &n3);
    media= (n1+n2+n3)/3 ;
    printf("A media das notas é  é:%.2f",media);
    return 0;
}
