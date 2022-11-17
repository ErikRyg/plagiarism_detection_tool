#include <stdio.h>

int main(int argc, char *argv[])
{
  int collection = 0;
  char aussortiert[100] = "";
  int o = 1;
  do
  {
    char *p = argv[o];
    do
    {
      if ((*p != 'x') && (*p != 'y') && (*p != 'q') && (*p != 'X') && (*p != 'Y') && (*p != 'Q'))
      {
        aussortiert[collection] = *p;
        collection++;
      }
      p++;
    } while ((*p) != '\0');
    o++;
  } while (o < argc);
  char newString[100] = "";
  int p = 0;
  aussortiert[collection] = '\0';
  printf("x,y,q und X,Y,Q aussortiert: %s\n", aussortiert);
  for (; p < collection; p += 3)
  {
    newString[p / 3] = aussortiert[p];
  }
  newString[p / 3] = '\0';
  printf("Der neue String lautet: %s \n", newString);
}
