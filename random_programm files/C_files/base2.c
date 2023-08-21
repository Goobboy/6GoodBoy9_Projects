#include <stdio.h>
#include <string.h>

int main()
{
    char message[] = "Oh hi mark";
    int length_of_message = strlen(message);

    printf("length: %d\n\n",length_of_message);
    int ASCII, remainder;
    char temp;

    for (int i = 0; i < length_of_message; i++)
    {   
        int binary[8];
        temp = message[i];
        ASCII = temp;

        printf("\n\nTemp: %c %d\n",temp,ASCII);
        // printf("\n%d",temp);
        for (int j = 0; j < 8; j++)
        {   
            remainder = ASCII % 2;  //remainder 1 or 0
            ASCII = ASCII/2;
            binary[j] = remainder;
            printf("%d",remainder);
        }

        printf("\nBinary of %c(%d): ",temp,temp);

        for (int k = 7; k >= 0; k--)
        {
            printf("%d",binary[k]);
        }
        
    }

    return 0;
}
