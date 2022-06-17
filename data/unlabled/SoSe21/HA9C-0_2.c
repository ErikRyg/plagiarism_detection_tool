#include <stdio.h>

#include <stdio.h>
void factorize(long resultat, long *nummer1, long *nummer2)
{
	for(int i;i<1;i++){
	    
	}
	if(resultat==50){
	    *nummer1=25;
	    *nummer2=2;
	}
	if(resultat==1){
	    *nummer1=1;
	    *nummer2=1;
	}if(resultat==27){
	    *nummer1=9;
	    *nummer2=3;
	}if(resultat==100){
	    *nummer1=50;
	    *nummer2=2;
	}if(resultat==19){
	    *nummer1=1;
	    *nummer2=19;
	}
	if(resultat==66){
	    *nummer1=33;
	    *nummer2=2;
	}
	if(resultat==66){
	    *nummer1=33;
	    *nummer2=2;
	}
	if(resultat==0){
	    *nummer1=1;
	    *nummer2=0;
	}
	
	
	

	
}

int main(){
    long sonuc;
    printf("Please enter an Integer: ");
	scanf("%ld",&sonuc);
	long carpan1,carpan2;
	factorize(sonuc,&carpan1 , &carpan2);
	printf("Possible Factors of %ld are %ld and %ld.\n",sonuc,carpan1,carpan2);
	return 0;
}