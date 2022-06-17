#include <stdio.h>
int main() {
   char satz[100], satz2[100];
   int l, k;
   
   fgets(satz, sizeof(satz), stdin);


   for (int i = 0, j; satz[i] != '\0'; ++i) {
      while (!(satz[i] >= 'a' && satz[i] <= 'p') && !(satz[i] >= 'r' && satz[i] <= 'w') && !(satz[i] == 'z') && !(satz[i] >= 'A' && satz[i] <= 'P') && !(satz[i] >= 'R' && satz[i] <= 'W') && !(satz[i] == 'Z') && !(satz[i] == '!') && !(satz[i] == '?') && !(satz[i] == '\0')){
         for (j = i; satz[j] != '\0'; ++j) {
            satz[j] = satz[j + 1];
         }
         satz[j] = '\0';
      }
   }
   printf("x,y,q und X,Y,Q aussortiert: ");
   puts(satz);
     for (int l = 0, k; satz[l] != '\0'; ++l) {
        satz2[k] == satz[l];
        k++;
        l=l+3;
    }
    printf("Der neue String lautet: %s", satz2);
    return 0;
}