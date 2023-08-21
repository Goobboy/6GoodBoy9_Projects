#include <stdio.h>

float year_calculation(int start_s, int end_s) {
    if (start_s == 0) {
        printf("Invalid input: start_s cannot be zero.\n");
        return -1; // Or any appropriate error value
    }

    float year = start_s + (start_s / 3.0) - (start_s / 4.0);
    float per_day = start_s - year;
    printf("\n%f", year);

    if (year >= end_s) {
        printf("\nInside break\n");
        return year;
    }

    do {
        year = year + (year / 3.0) - (year / 4.0);
        printf("\n%f", year);
    } while (year < end_s);

    return year;
}

int main() {
    int start_s = 100;
    int end_s = 200;

    float result = year_calculation(start_s, end_s);
    printf("\nFinal year: %f\n", result);

    return 0;
}