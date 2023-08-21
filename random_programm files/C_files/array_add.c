#include<stdio.h>

int main(void)
{
    int all_num[] = {5,10,15,20};

    int length = sizeof(all_num) / sizeof(all_num[0]);

    int sum=0;
    for (int i = 0; i < length; i++)
    {
        printf("%d",all_num[i]);
        sum +=all_num[i];
        printf("\n");
    }

    printf("\nTotal sum: %d", sum);
}
