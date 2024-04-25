#include<stdio.h>
#include<conio.h>
#include "greater.h"

int main(){
	int a,b,res;
	printf("Enter number a: ");
	scanf("%d",&a);
	printf("Enter number b: ");
	scanf("%d",&b);
	res = greaterThan(a,b);
	printf("Greater number is %d",res);
	return 0;
}
