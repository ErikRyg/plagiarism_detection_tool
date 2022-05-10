#include <stdio.h>

int main(int argc, char* argv[]) {
    //char* str[] = {"./[programm]", "PPR", "macht", "Spass!"}; //zum testen
    //int agc = 4;                                              //zum testen
    for(int i= 1; i<5; i++){
    //printf("%s\n", str[i]);                                 //test
    }
    
    char string1[100]; string1[99] = '\0';
    char string2[100]; string2[99] = '\0';
    char string3[100];
    for(int i = 0; i < 100; i++){
        string1[i] = '\0';
        string2[i] = '\0';
        string3[i] = '\0';
    }
    
    int pos = 0;
    for(int i = 1; i<argc; i++){
        int j = 0;
        int laenge = 0;
        while(argv[i][j] != '\0'){
        laenge++;
        j++;
        }
        //printf("i=%i - laenge=%i\n", i, laenge);                //test
        for(int y = 0; y<laenge; y++){
            string1[pos] = argv[i][y];
            pos++;
        }
    }
    
    //buchstabenloeschen
    int j = 0;
    int length = 0;
    while(string1[j] != '\0'){
    length++;
    j++;
    }
    //printf("length: %i\n", length);                       //test
    int zaehler = 0;
    for(int i=0; i<length; i++){
        if(string1[i] == 'x' || string1[i] == 'y' || string1[i] == 'q'){
            
        }
        else if(string1[i] == 'X' || string1[i] == 'Y' || string1[i] == 'Q'){
            
        }
        else{
            string2[zaehler] = string1[i];
            zaehler++;
        }
    }
    printf("x,y,q und X,Y,Q aussortiert: %s\n", string2);
    
    //nur noch jeden 3ten Buchstaben verwenden
    int countah = 0;
    for(int i=0; i<=zaehler; i+=3){
        string3[countah] = string2[i];
        countah++;
    }
    printf("Der neue String lautet: %s\n", string3);
    
    //string1[0] = str[1][0];                                   //test
    //printf("%s\n", string1);                                  //test
    //printf("%s\n", string2);                                  //test
    //printf("%s\n", string3);                                  //test
    
    return 0;
}