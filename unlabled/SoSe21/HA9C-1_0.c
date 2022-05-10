#include <stdio.h>

int main( int argc, char* argv[] ) 
{
    char str1[100];
    char str2[100];
    
    int wordCounter = 0;
    int str1Index = 0;
    char* currPointer = argv[1];
    
    int letterCounter = 3;
    int str2Index = 0;
    
    while (wordCounter < (argc - 1)) {
        if (*currPointer == 0) {
            wordCounter++;
        } else {
            char cP = *currPointer;
            if (cP == 'x' || cP == 'y' || cP == 'q' || cP == 'X' || cP == 'Y' || cP == 'Q') {
            } else {
                str1[str1Index] = *currPointer;
                str1Index++;
                
                if (letterCounter == 3) {
                    str2[str2Index] = *currPointer;
                    str2Index++;
                    letterCounter = 0;
                }
                    letterCounter++;
            }
        }
        currPointer++;
    }
    str1[str1Index] = 0;
    str2[str2Index] = 0;
    printf("x,y,q und X,Y,Q aussortiert: %s\n", str1);
    printf("Der neue String lautet: %s\n", str2);
}