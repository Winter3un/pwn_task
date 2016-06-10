#include<stdio.h>

int main()
{
	char a[50];
	printf("plz overflow me!\n");
	gets(a);
	return 1;
}