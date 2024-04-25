%{
#include<stdio.h>
int lineCount = 0;
%}
%%
\n {lineCount++ ;}
. ;
%%
int main(){
	printf("Enter the source code:(ctrl z to stop)\n");
	yylex();
	printf("\nNumber of lines : %d",lineCount);
	return 0;
}

int yywrap(){
	return 1;
}
