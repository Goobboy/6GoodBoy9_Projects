#include <stdio.h>
#include <string.h>

void on_true();
void off_false();

int main() {

    char message[] = "www.youtube.com/watch?v=dQw4w9WgXcQ";
    int length_of_message = strlen(message);

    printf("\nMessage: %s\n",message);
    int ASCII, remainder;
    char temp;

    for (int i = 0; i < length_of_message; i++)
    {   
        int binary[8];
        temp = message[i];
        ASCII = temp;

        for (int j = 0; j < 8; j++)
        {   
            remainder = ASCII % 2;  //remainder 1 or 0
            ASCII = ASCII/2;
            binary[j] = remainder;
        }

        printf("\n");
        for (int k = 7; k >= 0; k--)
        {
            if (binary[k]==1)
            {
                on_true();
            }
            else
            {
                off_false();
            }
            
        }
        
    }

    return 0;
}


void on_true()
{
    printf("🟡");
}

void off_false()
{
    printf("⚫");
}

