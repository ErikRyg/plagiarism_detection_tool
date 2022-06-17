#include <stdio.h>

int main(int argc, char* argv[] )
{  
	char str[100];
	char strneu[100];
	int a = 0;
	for (int i = 0; i < argc -1; i++)
	{
		for (int length = 0; *(*(argv+1+i)+length) != '\0'; length++)
		{
			str[a] = *(*(argv+1+i)+length);
			a++;
		}
	}
	str[a] = '\0';
	
	
	for (int i = 0; i < a+1; i++)
	{
		if ((str[i] == 'x') || (str[i] == 'y') || (str[i] == 'q') || (str[i] == 'X') || (str[i] == 'Y') || (str[i] == 'Q'))
		{
			
			
			
			
			do
			{
				str[i] = str[i+1];
				i++;
				if (str[i] == '\0')
				{	
					break;
				}
			} while(1);
			a--;
			i = 0;
		}
	}
	printf("x,y,q und X,Y,Q aussortiert: %s\n",str);
	for (int i = 0, z = 0; i < ((a/2)-2); i++, z += 3)
	{
		strneu[i] = str[z];
	}
	int length = 0;
	for (length; str[length] != '\0'; length++){}
	strneu[length] = '\0';
	printf("Der neue String lautet: %s",strneu);
}