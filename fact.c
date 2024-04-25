#include <stdio.h>
#include "fact.h"
int main(){
    int num;
    printf("Enter the number:- ");
    scanf("%d",&num);
    printf("Factorial of %d: %d\n",num,Factorial(num));
    return 0;
}