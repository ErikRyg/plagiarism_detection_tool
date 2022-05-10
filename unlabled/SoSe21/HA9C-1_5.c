#include <stdio.h>



int main(int argc, char** argv){

    
    char string1[100]= "";
    char string2[100]= "";
    int counter =0;
    int counter2 =0;


    for (int i = 1; i < argc ; i++)
    {   
        for (int j = 0; argv[i][j] != '\0'; j++)
        {   
            if (argv[i][j] != 'x' && argv[i][j] != 'y' && argv[i][j] != 'q' && argv[i][j] != 'X' && argv[i][j] != 'Y' && argv[i][j] != 'Q')
            {
                string1[counter] = argv[i][j];
                if (counter % 3 == 0)
                {
                    string2[counter2] = argv[i][j];
                    counter2++;
                }
                counter++; 
            }
        }
    }
    printf("x,y,q und X,Y,Q aussortiert: %s\n", string1);
    printf("Der neue String lautet: %s\n",string2);
}