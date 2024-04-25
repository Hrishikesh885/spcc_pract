#include<stdio.h>
#include<conio.h>
#include "areaa.h"

int main(){
	float side,res,l,b;
	int ch;
	while(1){
		printf("\n1. Area of Square\n2. Area of Rectangle\n3. Exit\nEnter the choice: ");
		scanf("%d",&ch);
		
		if(ch == 3){
			exit(0);
		}
		switch(ch){
			case 1:
				printf("Enter the side for a square : ");
				scanf("%f",&side);
				res = areas(side);
				printf("Result for square with side %.2f is %.2f",side,res);
				break;
			
			case 2:
				printf("Enter the length for a rectangle : ");
				scanf("%f",&l);
				printf("Enter the breadth for a rectangle : ");
				scanf("%f",&b);
				res = arear(l,b);
				printf("Result for rectabgle with length %.2f and breadth %.2f is %.2f",l,b,res);
				break;
				
			default:
				printf("Enter a valid choice!");
				break;
							
		}
	}
}
