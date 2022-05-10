#include <stdio.h>

int main(int argc, char** argv){
	char a[100];
	int u = 0;
	printf("x,y,q und X,Y,Q aussortiert: ");
	for(int i = 1; i < argc; i++){
		for(int j = 0; argv[i][j] != '\0'; j++){
			if(argv[i][j] == 'x'){
				for(int z = j; argv[i][z] != '\0'; z++){
					argv[i][z] = argv[i][z+1];
				}
			};
			if(argv[i][j] == 'X'){
				for(int z = j; argv[i][z] != '\0'; z++){
					argv[i][z] = argv[i][z+1];
				}
			};
			if(argv[i][j] == 'y'){
				for(int z = j; argv[i][z] != '\0'; z++){
					argv[i][z] = argv[i][z+1];
				}
			};
			if(argv[i][j] == 'Y'){
				for(int z = j; argv[i][z] != '\0'; z++){
					argv[i][z] = argv[i][z+1];
				}
			};
			if(argv[i][j] == 'q'){
				for(int z = j; argv[i][z] != '\0'; z++){
					argv[i][z] = argv[i][z+1];
				}
			};
			if(argv[i][j] == 'Q'){
				for(int z = j; argv[i][z] != '\0'; z++){
					argv[i][z] = argv[i][z+1];
				}
			};
			if(argv[i][j] == '\0') u -= 1;
			if(argv[i][j] != '\0') a[u] = argv[i][j];
			u++;
		}
	}
	char b[100];
	int k = 0;
	for(int i = 0; i < u; i++){
			if((i % 3) == 0){
				b[k] = a[i];
				k++;
			}
	}
	for(int i = 0; i < u; i++){
		printf("%c", a[i]);
	}
	printf("\nDer neue String lautet: ");
	for(int i = 0; i < k; i++){
		printf("%c", b[i]);
	}
	printf("\n");
}