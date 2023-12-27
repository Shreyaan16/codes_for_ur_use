#include<stdio.h>
int main()
{
    int num;
    printf("enter a number: ");
    scanf("%d",&num);
    int digit_sum=0;
    int sum=0;
    while(num>=10)
    {
        sum+=num%10;
        num=num/10;

    }
    if(num<10)
    {
        sum+=num;
    }
    while(sum>=10)
    {
        digit_sum+=sum%10;
        sum=sum/10;
    }
    if(sum<10)
    {
        digit_sum+=sum;
    }
    if(digit_sum==10)
    {
        digit_sum=1;
    }
    printf("sum reduced to one digit is %d \n",digit_sum);
}