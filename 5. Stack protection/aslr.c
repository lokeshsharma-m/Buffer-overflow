#include <stdio.h>
#include <stdlib.h>

void main()
{
    char a[12];
    char *b = malloc(sizeof(char) * 12);

    printf("Address of buffer x(stack): 0x%x\n", a);
    printf("Address of buffer x(heap): 0x%x\n", b);
}