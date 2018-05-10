#include <stdio.h>
unsigned int giaithua(int n)
{
	unsigned gt=1;
	for(int i=2;i<=n;i++)
		gt=gt*i;
	return gt;
}
