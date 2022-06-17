#include <stdio.h>
#include <stdlib.h>



int main( int argc, char* argv[] )
{
 char erg[100];
 int len=0;
 for(int i=0;i<argc-1;i++){
	 int j=0;

	 while(argv[i+1][j] != '\0'){
		 char temp=argv[i+1][j];

		 if(temp != 'x' && temp != 'y' && temp != 'q'){
			 if(temp != 'X' && temp != 'Y' && temp != 'Q'){
			 erg[len]=argv[i+1][j];
			 len++;
			 }
		 }
		 j++;

	 }
erg[len]='\0';
 }
 printf("x,y,q und X,Y,Q aussortiert: %s\n",erg);

 char erg2[100];
 int k=0;
 int j=0;
 	 while(erg[k] != '\0'){

 		 if(k % 3==0){
 			 erg2[j]=erg[k];
 			 j++;
 		 }
 		 k++;
 	 }
 erg2[len]='\0';
printf("Der neue String lautet: %s\n",erg2);
}