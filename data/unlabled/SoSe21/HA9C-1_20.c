#include <stdio.h>

int main(int laenge, char** Zeichen){
    char Ausgabe[100]="";
    char Ausgabe2[100]="";
    int j=0;
    int k=0;
    for (int l=1;l<laenge;l++){
        for (int i=0;Zeichen[l][i]!='\0';i++){
            if (Zeichen[l][i]!='x' && Zeichen[l][i]!='y' && Zeichen[l][i]!='q' && Zeichen[l][i]!='X' && Zeichen[l][i]!='Y' && Zeichen[l][i]!='Q'){
               Ausgabe[j]=Zeichen[l][i];
               j+=1;
            }
        }
    }
    for (int i=0;Ausgabe[i]!='\0';i++){
        if(i%3==0){
            Ausgabe2[k]=Ausgabe[i];
            k+=1;
        }
    }
    printf("x,y,q und X,Y,Q aussortiert: %s\n",Ausgabe);
    printf("Der neue String lautet: %s\n",Ausgabe2);
}