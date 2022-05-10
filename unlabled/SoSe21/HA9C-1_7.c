#include <stdio.h>
#include <stdlib.h>


typedef struct _String {
	char *str;
	unsigned int str_len;
} String;

String* arguments (int arg_count, char** args);

String* arguments (int arg_count, char** args) {
	String* arguments = malloc(sizeof(String) * 2);
	int count = 0;
	arguments[0].str_len = 0;
	arguments[0].str = malloc(256*sizeof(char));
	for (int i=1; i<arg_count; i++) {
		char* arg = args[i];
		int j = 0;
		char c = arg[j];
		while (c) {
			if (c == 'x'| c == 'X' | c == 'y' | c == 'Y' | c == 'q' | c == 'Q') {
				j++;
                        	c = arg[j];
				continue;
			}
			arguments[0].str[count] = c;
			count++;
			j++;
			c = arg[j];
		}
	}
	arguments[0].str_len = count;
	arguments[1].str_len = 0;
	arguments[1].str = malloc(256 * sizeof(char));
	for (int i=0; i<arguments[0].str_len; i++) {
		if (i%3 == 0) {
			arguments[1].str[arguments[1].str_len] = arguments[0].str[i];
			arguments[1].str_len++;
			}
		}
	return arguments;
}
			

int main (int argc, char** argv) {
	String* str = arguments(argc, argv);
	printf("x,y,q und X,Y,Q aussortiert: %s\nDer neue String lautet: %s", str[0].str, str[1].str);
	return 0;
}