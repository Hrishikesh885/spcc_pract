%{
#include<stdio.h>
int upperCase = 0;
int lowerCase = 0;
%}

%%
[A-Z]+ {upperCase++;}
[a-z]+ {lowerCase++;}
. ;
%%

int main(){
	printf("Enter the code : (ctrl z to stop)");
	yylex();
	printf("Number of uppercase characters: %d\n",upperCase);
	printf("Number of lowercase characters: %d",lowerCase);
	return 0;
}

int yywrap(){
	return 1;
}
