#include stdio.h

def char* kedi(int sayi, char* isim[]){
    char array[100];
   int count=0;
    for (int i=0;i<sayi;i++){
    
    int uzunluk = strlen(isim[i]);
    for (int j=0;j<uzunluk;j++){
        if (isim[i][j]=="x"||isim[i][j]||=="y"||isim[i][j]=="q"||isim[i][j]=="X"||isim[i][j]=="Y"||isim[i][j]=="Q"){
            }
            else {array[count]=isim[i][j];count++;}
    }
    
}    
char yeniarray[count];
for (int i=0;i<=count;i++){
    yeniarray[i]=array[i];
}



char enyeni[count];
for (int i=0;i<count;i++){
    enyeni[i]=yeniarray[i];
}



return(yeniarray,yeniarray);

}










int main( int argc, char* argv[] )
{  
  char test[11]= "0123456789";
  printf( "x,y,q und X,Y,Q aussortiert: " );
  
  printf( "%s \n", kedi(argc,argv)[0] );
  printf( "Der neue String lautet:" );
  printf( "%s \n", kedi(argc,argv)[1] );
}