//this this progam finds the longest subarray

#include<stdio.h>

int highest_num_find(int count[], int length);

int main()
{
    int zero_one[] = {1, 0, 1, 7, 8, 2, 3, 0, 0, 1, 0, 1, 1, 4, 0, 1, 0, 1, 1, 3, 0, 0, 1, 0, 1, 1, 0,4,1,0,23};
    
    int length = sizeof(zero_one)/sizeof(zero_one[0]);
    printf("Length: %d",length);

    // arrays for all info
    int count[length/2];
    int start[length/2];
    int stop[length/2];
    for (int i = 0; i < length/2; i++)
    {
        count[i] = -1;
        start[i] = -1;
        stop[i] = -1;
    }
    
    int count_counter = 0;
    int flag_start = 1;
    int flag_stop = 0;
    int append_counter = 0;
    for (int i = 0; i < length; i++)
    {   
        printf("\n\ntop loop");

        if(zero_one[i] == 1 || zero_one[i] == 0)
        {   
            count_counter++;
            if (flag_start == 1)
            {   
                printf("\nflag start: %d",i);
                flag_start = 0;
                flag_stop = 1;
                start[append_counter] = i;
            }
        }
        else
        {
            if (flag_stop == 1)
            {   
                printf("\nflag stop: %d",i-1);
                printf("\tCount-counter: %d",count_counter);
                flag_start = 1;
                flag_stop = 0;
                stop[append_counter] = (i-1);
                count[append_counter] = count_counter;
                append_counter++;
                printf("\nappend_counter: %d",append_counter);
                count_counter = 0;
            }
        }
    }

    if (zero_one[(length-1)] == 1 || zero_one[length-1] == 0)
    {   
        printf("\nendvalue? %d\n",zero_one[length-1]);
        printf("flag stop: %d",(length-1));
        printf("\tCount-counter: %d",count_counter);
        flag_start = 0;
        flag_stop = 1;
        stop[append_counter] = (length-1);
        append_counter++;
    }
    
    int highest_count = highest_num_find(count,(length/2));

    for (int i = 0; i < append_counter; i++)
    {
        if (count[i] == highest_count)
        {   
            printf("\nThe longest subarray Starts from index %d and stops at %d \n",start[i],stop[i]);
            printf("Subarray: ");
            for (int j = start[i]; j <= stop[i]; j++)
            {
                printf("%d  ",zero_one[j]);
            }
        }
        
    }
 
}


int highest_num_find(int count[], int length)
{
    printf("\n\nLength of count: %d",length);

    int high_num = 0;

    for (int i = 0; i < length; i++)
    {
        if(count[i]>high_num)
        {
            high_num = count[i];
        }
    }

    printf("\nHigest count: %d",high_num);
    printf("\n\n\n");

    return high_num;
}





