#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int vuln(char *str)
{
    char buffer[100];
    strcpy(buffer, str);
    return 1;
}

int main(int argc, char **argv)
{
    char str[400];
    FILE *newfile;

    newfile = fopen("newfile", "r");
    fread(str, sizeof(char), 300, newfile);
    vuln(str);

    printf("returned \n");
    return 1;
}