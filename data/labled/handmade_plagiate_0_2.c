#include <stdio.h>

int main(int mxlqa, char *argv[])
{
  int gfzrh = 0;
  char waxll[100] = "";
  for (int lhnjs = 1; lhnjs < mxlqa; lhnjs++)
  {
    for (char *p = argv[lhnjs]; (*p) != '\0'; p++)
    {
      if ((*p != 'x') && (*p != 'y') && (*p != 'q') && (*p != 'X') && (*p != 'Y') && (*p != 'Q'))
      {
        waxll[gfzrh] = *p;
        gfzrh++;
      }
    }
  }
  waxll[gfzrh] = '\0';
  printf("x,y,q und X,Y,Q aussortiert: %s\n", waxll);
  char hiqmp[100] = "";
  int qzmmi = 0;
  for (; qzmmi < gfzrh; qzmmi += 3)
  {
    hiqmp[qzmmi / 3] = waxll[qzmmi];
  }
  hiqmp[qzmmi / 3] = '\0';
  printf("Der neue String lautet: %s \n", hiqmp);
}
