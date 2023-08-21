//works like a charm


#include<stdio.h>

int main(void)
{
    int position = 3;
    int all_num[] = {1,2,3,4,5,6,7,8,9};
    int length = sizeof(all_num) / sizeof(all_num[0]);

    int rotated[length];

    printf("before rotation: ");
    for (int i = 0; i < length; i++)
    {
        printf("%d, ",all_num[i]);
    }


    //conversion part
    int total=0;
    printf("\nrotation postion: %d", position);
    for (int i = 0, j = position; j <length;i++,j++)
    {      
        total++;
        rotated[i] = all_num[j];
    }
    for (int i = 0; i < position; i++)
    {
        rotated[total] = all_num[i];
        total++;
    }


    //printing the rotated value
    printf("\n\nAfter rotation: ");
    for (int i = 0; i < length; i++)
    {
        printf("%d, ",rotated[i]);
    }
    printf("\n");

}
