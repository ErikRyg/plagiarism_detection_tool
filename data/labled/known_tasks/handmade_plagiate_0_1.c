#include <stdio.h>

int main(int argc, char *argv[])
{
  char sammlung[100] = "";
  int counter = 0;
  int k = 1;
  while (k < argc)
  {
    char *p = argv[k];
    while ((*p) != '\0')
    {
      if ((*p != 'x') && (*p != 'y') && (*p != 'q') && (*p != 'X') && (*p != 'Y') && (*p != 'Q'))
      {
        counter++;
        sammlung[counter - 1] = *p;
      }
      p++;
    }
    k++;
  }
  int l = 0;
  char neuerString[100] = "";
  sammlung[counter] = '\0';
  printf("x,y,q und X,Y,Q aussortiert: %s\n", sammlung);
  while (l < counter)
  {
    neuerString[l / 3] = sammlung[l];
    l += 3;
  }
  neuerString[l / 3] = '\0';
  printf("Der neue String lautet: %s \n", neuerString);
}
