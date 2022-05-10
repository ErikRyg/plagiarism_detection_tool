#include <stdio.h>

int main(int argc, char* argv[] )
{  
	char str[100];
	char str2[100];
	int j = 0;
	for (int i = 0; i < argc -1; i++)
	{
		int lange = 0;
		for (lange; *(*(argv+1+i)+lange) != '\0'; lange++)
		{
			str[j] = *(*(argv+1+i)+lange);
			j++;
		}
	}
	str[j] = '\0';
	for (int i = 0; i < j+1; i++)
	{
		if ((str[i] == 'x') || (str[i] == 'y') || (str[i] == 'q') || (str[i] == 'X') || (str[i] == 'Y') || (str[i] == 'Q'))
		{
			while (1)
			{
				str[i] = str[i+1];
				i++;
				if (str[i] == '\0')
				{	
					break;
				}
			}
			j--;
			i = 0;
		}
	}
	printf("x,y,q und X,Y,Q aussortiert: %s\n",str);
	for (int i = 0, z = 0; i < ((j/2)-2); i++, z += 3)
	{
		str2[i] = str[z];
	}
	int lange = 0;
	for (lange; str[lange] != '\0'; lange++)
		;
	str2[lange] = '\0';
	printf("Der neue String lautet: %s",str2);
}


//**(argv + 1 + lange) != '\0'