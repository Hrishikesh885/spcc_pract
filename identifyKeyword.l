%{
#include <stdio.h>
int if_count = 0;
int else_count = 0;
int while_count = 0;
%}

%%
if      { if_count++; }
else    { else_count++; }
while   { while_count++; }
[[:alpha:]]+    ; // Ignore other words
.       ; // Ignore other characters

%%

int main() {
	printf("Enter the code: (Ctrl+Z to end)\n");
    yylex();
    printf("Occurrences of:\n");
    printf("if: %d\n", if_count);
    printf("else: %d\n", else_count);
    printf("while: %d\n", while_count);
    return 0;
}

int yywrap(){
	return 1;
}

