#include <stdio.h>

int main(int  argc, char *argv[]) // start at argv[1]
{


char array[100];
int slot_count = 0;
char b[100];
int slot_count_b = 0;
			
for(int i = 1; i < argc; i++)
	{
	int j = -1;
	do
		{
		j++;
		if(argv[i][j] == 'x') continue;
		else if(argv[i][j] == 'y') continue;
		else if(argv[i][j] == 'q') continue;
		else if(argv[i][j] == 'X') continue;
		else if(argv[i][j] == 'Y') continue;
		else if(argv[i][j] == 'Q') continue;
		else if(argv[i][j] == '\0')
			{
			array[slot_count] = '\0';
			b[slot_count_b] = '\0';
			}
		else
			{
			array[slot_count] = argv[i][j];
			
			if( (slot_count == 0 || (slot_count) % 3 == 0) )
				{
				b[slot_count_b] = array[slot_count];
				slot_count_b++;
				}		
			slot_count++;
			}
		
		
		}		
	while(argv[i][j] != '\0');
	}
printf("x,y,q und X,Y,Q aussortiert: ");
for(int m = 0; m < slot_count; m++) printf("%c", array[m]); 
printf("\nDer neue String lautet: ");
for(int n = 0; n < slot_count_b; n++) printf("%c", b[n]); 
}