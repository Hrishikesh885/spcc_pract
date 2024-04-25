%{
    #include <stdio.h>
    int count_vow=0;
    int count_cons=0;
%}
%%
[a-zA-z] {
    if(yytext[0]=='a' || yytext[0]=='e'|| yytext[0]=='i'|| yytext[0]=='o'|| yytext[0]=='u' ||
            yytext[0]=='A'|| yytext[0]=='O'|| yytext[0]=='U'|| yytext[0]=='I'|| yytext[0]=='E'){
                printf("Vowel %c\n",yytext[0]);
                count_vow++;
            }
            else{
                printf("Consonant %c\n",yytext[0]);
                count_cons++;
            }
                printf("Consonants are:- %d\n",count_cons);
    printf("Vowels are:- %d\n",count_vow);
        

}

%%
int main()
{
    yylex();
    
    return 0;
}