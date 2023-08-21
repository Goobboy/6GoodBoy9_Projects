//Say we have a population of n llamas. Each year, n / 3 new llamas are born, and n / 4 llamas pass away.
//this progam claculates how many year will it take

#include<stdio.h>

float year_calculation(int start_s, int end_s);

int main(void)
{   
    //get initial and end population.
    int start_s, end_s;
    printf("\n\n_______________________________________________________________________________________");
    printf("\nNote: Every year a third popuolation increases and a fourth populationn pass away.\n");
    printf("What is the start size? ");
    scanf("%d",&start_s);
    printf("What is the end size? ");
    scanf("%d",&end_s);

    // calcualte how many year it will take 

    float total_days = year_calculation(start_s,end_s);
    float total_years = total_days/365;
    float total_months = (total_years - (int)total_years)*12;

    printf("\n\nIt will take approximately %d Year(s) and %d Month(s)", (int)total_years, (int)total_months);


}

float year_calculation(int start_s, int end_s)
{
    if (start_s <= 0) {
        printf("%d",start_s);
        printf("Invalid input: start_s cannot be less than 1.\n");
        return -1; // Or any appropriate error value
    }
    else if (end_s <= start_s)
    {
        printf("Invalid input: end cannot be less than start.\n");
        return -1; // Or any appropriate error value
    }

    float increase_by_day = start_s + ((start_s/3)/365) - ((start_s/4)/365);
    printf("\n%f", increase_by_day);

    int day = 0;

    do {
        day++;
        increase_by_day = increase_by_day + ((increase_by_day/3)/365) - ((increase_by_day/4)/365);
        printf("\n%f", increase_by_day);
    } while (increase_by_day < end_s);

    return day;
}