#include <stdio.h>
void main()
{
    int a[20],n,i,j,temp;
    printf("enter the size of the array");
    scanf("%d",&n);
    printf("enter the elemnts of array")
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);

    }
    for(i=0;i<n-1;i++)
    {
       for(j=0;j<n-1;j++)
       {
           temp= a[j];
           a[j]=a[j+1];
           a[j+1]=temp;
       }
    }
    printf("the sorted array is");
    for(i=0;i<n-1;i++)
    {printf("%d\t",a[i]);}
}

