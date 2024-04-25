#include<stdio.h>
#include<stdlib.h>
#include "bin-dec.h"

int main() {
    char hexadecimal[20], binary[20];
    int ch;

    while(1){
        printf("\n1. Binary to Decimal\n2. Binary to Hexadecimal\n3. Exit\nEnter Choice: ");
        scanf("%d",&ch);
        
        if (ch == 3){
            exit(0);
        }
        
        switch(ch){
            case 1:
                printf("Enter the binary: ");
                scanf("%s", binary);
                printf("The decimal for binary %s is %ld", binary, binDec(binary));
                break;
            case 2:
                printf("Enter the binary: ");
                scanf("%s", binary);
                binHex(binary, hexadecimal);
                printf("The hexadecimal for binary %s is %s", binary, hexadecimal);
                break;
            default:
                printf("Invalid choice!\n");
        }
    }

    return 0;
}

