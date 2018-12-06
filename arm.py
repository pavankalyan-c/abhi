#include<stdio.h>
int main()
{
	char ch;
	printf("\n please enter any character\n");
	scanf("%c", &ch);
	if(ch >=97 && ch<=122)
	{
		printf("\nEntered character is lowercase alphabet");
		
	}
else	
   {
   	   printf("\nEntered character is not lowercase alphabet");
   }
}
