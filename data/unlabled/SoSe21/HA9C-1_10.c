#include <stdio.h>

int main(int argc, char** argv){
    char array [100];
    char array2 [100];
    int k = 0;
    for( int i = 1; i < argc; i++){
        for(int j = 0; '\0' != argv[i][j]; j++){
             if(argv[i][j] != 'x' && argv[i][j] && argv[i][j] != 'y' && argv[i][j]!= 'q' && argv[i][j] != 'X' && argv[i][j] != 'Y' && argv[i][j] != 'Q'){ 
             array[k] = argv[i][j];
             k++;
             }
        }
    }
    array[k] = '\0';
    printf("x,y,q und X,Y,Q aussortiert: %s\n", array);
    for(int i = 0; 3 * i < k ; i++){
        array2[i] = array[3*i];
    }
    printf("Der neue String lautet: %s", array2);
}