#include <stdio.h>
#include <stdlib.h>

void ersetzen(char *dest, int zahl, char *src)
{
  int abc = 0;
  do
  {
    if (!(dest[abc] != '\0' && src[abc] != '\0'))
      break;
    abc++;
    dest[abc - 1] = src[abc - 1];
  } while (abc < zahl);
}

void umdrehen(char *str)
{
  int def = 0;
  int entfernung = 0;
  char zwischen = 0;
  while (!(str[entfernung] == '\0'))
    entfernung++;
  do
  {
    def++;
    str[def] = str[entfernung - def - 2];
    zwischen = str[def - 1];
    str[entfernung - def - 2] = zwischen;
  } while (entfernung / 2 > def);
}

int main(int argc, char *argv[])
{
  char test[11] = "0123456789";
  printf("Das Original ist: %s \n", test);
  ersetzen(test, atoi(argv[1]), argv[2]);
  printf("Ersetzt : %s \n", test);
  umdrehen(test);
  printf("Rückwärts : %s \n", test);
}