#include<stdio.h>

/*

    #
   ##                                       
  ###                                   
 ####                  ╥¼↨‼V↨φ↓R?§╫╫§§╙               
#####        ╥ ╫§╔å└╚╔╩╦═╬╧╨╤ú╘▀♠○▒   ⁿ√éä█    


▀
▀ ▀
▀ ▀ ▀
▀ ▀ ▀ ▀
▀ ▀ ▀ ▀ ▀

*/

int size=5;

int main(void)
{
    printf("\n\n\n\n\n");
    for(int i = 1; i<=size;i++)
    {
        printf("\n");
        int count = 0;
        int block = 0;
        int air = size-i;
        while (air>count)
        {
            printf("  ");
            air--;
        }

        
        while (block<i)
        {
            /* code */
            block++;
            printf(" ▀");
        }

        printf("     ");

        for (int another= 0; another < block; another++)
        {
            printf(" ▀");
        }
        
    }
}

