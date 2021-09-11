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

void memLeak(int megabytes, char *program_name) {
	int *ptr;
    
    printf("Filling memory with value close to %dMB...\n", megabytes);
    /* weird math to fill memory at least somewhat accurate */	
    for(int i = 0; i < (megabytes * 130000 / 4); i++) {
        ptr = malloc(1);
    }

    /* execute GNU/Linux command to see how much memory does the process holds */
    char mem[1000];   
    snprintf(mem, sizeof(mem), "echo -n \"Filled memory with: \" && ps -eo rss,pid,euser,args --sort %%mem | grep -i %s | grep -v grep | awk '{printf $1/1024 \"MB\"; $1=\"\"; print }' | cut -d ' ' -f 1", program_name);
    system(mem);
 
    /* loop to keep program running, so memory won't get free */
    printf("\nPress Ctrl+C to exit program and free the memory.\n");
	while(1) {
	
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
            memLeak(atoi(argv[1]), argv[0]); /* convert string to int */
        }
	}

	return 0;
}
