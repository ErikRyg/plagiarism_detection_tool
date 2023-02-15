#include <stdio.h>
#include <stdlib.h>

void umdrehen(char *str)
{
  char temporaer = 0;
  int length = 0;
  while (!(str[length] == '\0'))
    length++;
  int k = 0;
  do
  {
    k++;
    temporaer = str[k - 1];
    str[k] = str[length - k - 2];
    str[length - k - 2] = temporaer;
  } while (length / 2 > k);
}

void ersetzen(char *dest, int zahl, char *src)
{
  int k = 0;
  do
  {
    if (!(dest[k] != '\0' && src[k] != '\0'))
      break;
    k++;
    dest[k - 1] = src[k - 1];
  } while (k < zahl);
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