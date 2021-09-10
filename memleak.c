/*
* Author: AISK11
* This program will fill memory with specified amount of Megabytes
*/

#include <stdio.h>
#include <stdlib.h>

/* return 1, if variable is number, return 0 otherwise */
int isNumber(char number[]) {
	
	for (unsigned short i = 0; number[i] != 0; i++) {
		if(number[i] > '9' || number[i] < '0') {
			return 0;
		}
	}
	return 1;
}

void memLeak(int megabytes) {
	int *ptr;
	int assigned_bytes = 1000000; /* 1MB */

	for (unsigned int i = 0; i < megabytes; i++) {
		ptr = malloc(assigned_bytes);
		printf("%d: %d bytes were assigned.\n", i+1, assigned_bytes);
	}


    printf("Filled memory with %dMB.\n\nPress Ctrl+C to exit program and free the memory.\n", megabytes);	
	while(1) {
		//printf("a\n");
	}

}

int main(int argc, char *argv[]) {

	if(argc < 2) {
		fprintf(stderr, "ERROR: not enough arguments (%d)!\n", argc);
		fprintf(stderr, "SYNTAX: %s <NUMBER-OF-MEGABYTES>\n", argv[0]);
		fprintf(stderr, "EXAMPLE: (create 1GB memory leak): '%s 1000'\n", argv[0]);
		return -1;
	}
	else if(argc > 2) {
		fprintf(stderr, "ERROR: too many arguments (%d)!\n", argc);
		fprintf(stderr, "SYNTAX: %s <NUMBER-OF-MEGABYTES>\n", argv[0]);
		fprintf(stderr, "EXAMPLE: (create 1GB memory leak): '%s 1000'\n", argv[0]);
		return -2;
	}
	else {
		if(!isNumber(argv[1])) {
			fprintf(stderr, "ERROR: supplied argument (%s) is not a number!\n", argv[1]);
            return -3;
		}
        else {
            memLeak(atoi(argv[1])); /* convert string to int */
        }
	}

	return 0;
}
