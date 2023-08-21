#include <stdio.h>

int eos()
{
    int a,s[50],i,odd=0,even=0;
    printf("Upto to how many number you want to enter:");
    scanf("%d",&a);
    
    printf("Please enter the numbers:\n");
    
    for(i=0;i<a;i++)
    {
        scanf("%d",&s[i]);
    }
    
    for(i=0;i<a;i++)
    {
        if(s[i]%2==0)
        {
            even=even+s[i];
        }
        else
        {
            odd=odd+s[i];
        }
    }
    
    printf("\nThe sum of all even numbers is %d",even);
    printf("\nThe sum of all odd numbers is %d",odd);

    printf("\n\n");
    printf("__________Task Completed__________\n");

    printf("Press Enter to exit.");
    getchar(); // Consume newline characters
    getchar(); // Waits for the user to press Enter

    return 0;
}

int main()
{
    eos();
}


