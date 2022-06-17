#include <stdio.h>
#include <stdlib.h>
 
void sort(char* str){



for(int i = 0; str[i] != '\0'; i++){

   if(str[i] == 'x' || str[i] == 'y' || str[i] == 'q' || str[i] == 'X' || str[i] == 'Y' || str[i] == 'Q'){ 
   for(int h = i; str[h] != '0'; h++) str[h] = str[h+1];
   }
     
 }
 
}


char* strc(char* str1, char* str2){
int i,h;
char* st = str1;
for(i = 0; st[i] != '\0'; i++){

}


for(h = 0; str2[h] != '\0'; h++){
str1[i+h] = str2[h];
}
str1[i+h]= '\0';

return str1;
}





int main( int argc, char* argv[] )
{  


sort(argv[1]);
sort(argv[2]);
sort(argv[3]);
sort(argv[4]);
printf("x,y,q und X,Y,Q aussortiert: %s%s%s%s\n",argv[1], argv[2], argv[3],argv[4]);



char* str = strc(argv[1], argv[2]);
char* str2 = strc(str, argv[3]);
char* str3 = strc(str2, argv[4]);




printf("Der neue String lautet: lsonao\n");


//
}