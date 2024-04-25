%{
#include<stdio.h>
int upperCase = 0;
%}
%%
[A-Z] {upperCase++;}
. ;
\n {
	printf("Number of Uppercase Characters : %d",upperCase);
	return 0;
}
%%
int main(){
	printf("Enter the sentence : ");
	yylex();
	return 0;
}
 int yywrap(){
 	return 1;
 }
 
