#include <stdio.h>

float all_bill_info(void);

int main(void)
{
    // Takes total amount, tip%, tax, total number of people (tnp) in a function
    float each = all_bill_info();

    // Prints the returned value from function
    printf("\nYou will owe $%.2f each!\n", each);

    printf("\n\n---------Task Complete---------");

    return 0;
}

float all_bill_info(void)
{
    float amount, tip, tax;
    int tnp;

    printf("__________________________________");

    printf("\nBill before tax and tip: ");
    scanf("%f", &amount);

    printf("Tip percent: ");
    scanf("%f", &tip);

    printf("Sale Tax Percent: ");
    scanf("%f", &tax);

    printf("Total amount of guests: ");
    scanf("%d", &tnp);

    printf("__________________________________");
    
    amount = amount + ((tip / 100) * amount); // Adding tip
    float after_tax = amount + ((tax / 100) * amount); // Adding tax

    float each = after_tax / tnp;

    return each;
}
