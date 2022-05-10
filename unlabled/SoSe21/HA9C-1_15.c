#include <stdio.h>



int main(int argc, char** argv){
    
    char str1[100] = "";
    char str2[100] = "";
    char str3[100] = "";
    int f = 0;
    for (int i = 1; i < argc; i++){
        for (int j = 0; argv[i][j] != '\0' ; j++){
        
           str1[f] += argv[i][j];
           f++;

        }  
    }
    int j = 0;
    for (int i = 0; str1[i] != '\0'; i++){
        if(str1[i] != 'x' && str1[i] != 'y' && str1[i] != 'q' && str1[i] != 'X' && str1[i] != 'Y' && str1[i] != 'Q' ){
            str2[j] = str1[i];
            j++;
        }
    }
    
    int g = 0;
    for (int i = 0 ; str2[i] != '\0'; i = i + 3){
        str3[g] = str2[i];
        g++;
    }
  

    printf("x,y,q und X,Y,Q aussortiert: %s\n", str2);
    printf("Der neue String lautet: %s\n", str3);
    
}