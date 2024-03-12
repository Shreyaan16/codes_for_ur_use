#include<stdio.h>

void fibo(int n)
{
int x1=1;
int x2=1;
printf("%d \n",x1);
printf("%d \n",x2);
for(int i=0;i<n-2;i++)
{
int x3=x2+x1;
printf("%d \n",x3);
x1=x2;
x2=x3;
}
}

int main()
{
fibo(5);
}