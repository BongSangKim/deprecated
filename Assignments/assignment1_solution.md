# Assignment #1

## Notes

This solution shows one of the examples of implementing functions
for assignment1.

## Function specification

```cpp
#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;

// version 1
int find_max(int* a, int start, int end)
{
    int max_value = -1;

    for (; start < end; start++)
        max_value = max_value > a[start] ? max_value : a[start];

    return max_value;
}

// version 2
int find_max(int* start, int* end)
{
    int max_value = -1;

    for ( ; start != end; start++)
        max_value = max_value > *start ? max_value : *start;

    return max_value;
}

void sprint_ascii(char* buffer, int start, int end, int item_per_line)
{
    int i;

    for (i = 1; start < end; start++, i++)
    {
        buffer += sprintf(buffer, "%4d %c", start, (char)start);
        if (i % item_per_line == 0)
            buffer += sprintf(buffer, "\n");
    }
    i--;
    if (i % item_per_line != 0)
        buffer += sprintf(buffer, "\n");
}

int string_compare(const char* left, const char* right)
{
    // when the first operand of && is evaluated as false,
    // the second operand is NOT evaluated at all
    while (*left && *right && *left++ == *right++) ;
    return *left - *right > 0 ? 1 : (*left == *right ? 0 : -1);

    //If we want to string_compare returns the same return value,
    //you can change 
    //return *left - *right;
}

int string_n_compare(const char* left, const char* right, int n)
{
    while (*left && *right && --n > 0 && *left++ == *right++) ;
    return *left - *right > 0 ? 1 : (*left == *right ? 0 : -1);
}

char* string_copy(char* dst, const char* src)
{
    char* save = dst;
    while (*dst++ = *src++) ;
    return save;
}

int string_in(const char character, const char* pattern)
{
    while (*pattern)
        if (character == *pattern++)
            return 1;
    return 0;
}
```
