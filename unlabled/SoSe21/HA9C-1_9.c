#include <stdio.h>
#include <stdlib.h>

void xyzz(char* string)
{
  int t = 0;
  for(char *temp = string; *temp!=0; temp++, t++);
  for(int i = 0,j = 0; i<=t; i++){
    if(i%3==0){
      string[j]=string[i];
      j++;
    }
    if(i==t){
      string[j]=0;
    }
  }
}

void xyz(char* out,int *temp,char* in)
{ 
  char *pout=out;
  for(int i = 0; i<*temp; i++)
  {
    *pout++;
  } 
  for(char *pin=in;*pin!=0;pin++)
  {
    switch (*pin)
    {
      case ' ':
      case 'x':
      case 'X':
      case 'y':
      case 'Y':
      case 'q':
      case 'Q':
        break;
      default:
      *pout++ = *pin;
      *temp+=1;
        break;  
    }    
  }
  *pout=0;
}
int main(int argc, char* argv[])
{
  char str[100];
  int times=0;
  
  for(int i=1; i<argc;i++)
  {
    xyz(str, &times, argv[i]);
  }
  printf( "x,y,q und X,Y,Q aussortiert: %s\n",str);
  xyzz(str);
  printf( "Der neue String lautet: %s\n",str);
}