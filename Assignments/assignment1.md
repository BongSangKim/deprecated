# Assignment #1

## Notes

The description of this assignment will be updated as needed. Please check this page frequently.

## Overview

Write 7 functions with the specification shown below. These functions access or manipulate data stored in arrays and/or pointers.

* find_max() (version 1)
* find_max() (version 2)
* sprint_ascii()
* string_compare()
* string_n_compare()
* string_copy()
* string_in()

When implementing the above functions, you cannot use any C/C++ library functions (one exception is `sprintf()`).

**Note** a couple of more functions may be added to assignment1.

## Scores

1. Correct implementation of 7 functions: 70 pts. (10 pts each)
2. Coding style: 30 pts.
  - Proper use of pointers and/or arrays
  - Readability of codes
  - Simple and clean code without redundancy
  - Adequate comments (SHOULD BE IN ENGLISH)

  **_Subject to change_**

## Due

This assignment is due by 11:59 pm on 10/16 (Monday). The penalty due to the late submission is as follows.

| Delay    | Penalty |
|----------|---------|
|  <  2 hr | 10%     |
|  < 24 hr | 30%     |
|  < 48 hr | 50%     |
| >= 48 hr | 100%    |

**_Subject to change_**

## Submission

You are required to submit your assignment on elice. As of now, the assignment is NOT prepared on elice.io. The notice will be made when it is ready.

## Sample output

```cpp
#include <cstring>
#include <cstdio>

#define MAX_LINE 1024
#define NULL 0

using namespace std;

int main()
{
    char buffer[MAX_LINE];
    int array[] = {42, 23, 6, 28, 10};
    int n = sizeof(array) / sizeof(int);

    printf("* Examples of find_max()\n");
    printf("%d\n", find_max(array, 0, n));
    printf("%d\n", find_max(array, 1, 2));
    printf("%d\n", find_max(array, 1, 4));
    printf("%d\n", find_max(array, array + n));
    printf("%d\n", find_max(array + 1, array + 2));
    printf("%d\n", find_max(array + 1, array + 4));

    printf("* Examples of sprint_ascii()\n");
    sprint_ascii(buffer, 32, 128, 8);
    printf("%s", buffer);

    // this example doesn't change a line
    sprint_ascii(buffer, 32, 33, 8);
    printf("%s", buffer);

    sprint_ascii(buffer, 32, 40, 8);
    printf("%s", buffer);

    printf("* Examples of string_compare()\n");
    printf("%d\n", string_compare("abc", "abc"));
    printf("%d\n", string_compare("abc", "ab"));
    printf("%d\n", string_compare("abc", "abcd"));

    printf("* Examples of string_n_compare()\n");
    printf("%d\n", string_n_compare("Hello!", "Hello, world!", 5));
    printf("%d\n", string_n_compare("Hello!", "Hello, world!", 7));
    printf("%d\n", string_n_compare("Hello, world!", "Hello!", 5));
    printf("%d\n", string_n_compare("Hello, world!", "Hello!", 7));

    printf("* Examples of string_copy()\n");
    string_copy(buffer, "Hello, world!");
    printf("%s\n", buffer);
    printf("%s\n", string_copy(buffer, "How are you doing?"));

    printf("* Examples of string_in()\n");
    printf("%d\n", string_in('!', " .,:"));
    printf("%d\n", string_in(' ', " .,:"));
    printf("%d\n", string_in(',', " .,:"));
    printf("%d\n", string_in(':', " .,:"));
}
```

For the above code, you need to get the following results. The test code may include, but not limited to the above test cases.

```
* Examples of find_max()
42
23
28
42
23
28
* Examples of sprint_ascii()
  32    33 !  34 "  35 #  36 $  37 %  38 &  39 '
  40 (  41 )  42 *  43 +  44 ,  45 -  46 .  47 /
  48 0  49 1  50 2  51 3  52 4  53 5  54 6  55 7
  56 8  57 9  58 :  59 ;  60 <  61 =  62 >  63 ?
  64 @  65 A  66 B  67 C  68 D  69 E  70 F  71 G
  72 H  73 I  74 J  75 K  76 L  77 M  78 N  79 O
  80 P  81 Q  82 R  83 S  84 T  85 U  86 V  87 W
  88 X  89 Y  90 Z  91 [  92 \  93 ]  94 ^  95 _
  96 `  97 a  98 b  99 c 100 d 101 e 102 f 103 g
 104 h 105 i 106 j 107 k 108 l 109 m 110 n 111 o
 112 p 113 q 114 r 115 s 116 t 117 u 118 v 119 w
 120 x 121 y 122 z 123 { 124 | 125 } 126 ~ 127 
  32
  32    33 !  34 "  35 #  36 $  37 %  38 &  39 '
* Examples of string_compare()
0
1
-1
* Examples of string_n_compare()
0
-1
0
1
* Examples of string_copy()
Hello, world!
How are you doing?
* Examples of string_in()
0
1
1
1
```

## Function specification

### `find_max()` (version 1)

```cpp
/**
 * Return the maximum value of specified elements in the given array
 *
 * @param array     int array
 * @param start     int, low endpoint (inclusive) of the array (index)
 * @param end       int, high endpoint (exclusive) of the array (index)
 * @return          the maximum of the elements from start, inclusive
 *                                              to end, exclusive
 */
int find_max(int* a, int start, int end);
```

### `find_max()` (version 2)

```cpp
/**
 * Return the maximum value of specified elements in the given array
 *
 * @param start     low endpoint (inclusive) of the array (pointer)
 * @param end       high endpoint (exclusive) of the array (pointer)
 * @return          the maximum of the elements from start, inclusive
 *                                              to end, exclusive
 */
int find_max(int* start, int* end);
```

### `sprint_ascii()`

```cpp
/**
 * Print ascii tables to a char array
 *
 * @param buffer        char array that an ascii table will be written
 * @param start         low endpoint (inclusive) of the ascii code
 * @param end           high endpoint (exclusive) of the ascii code
 * @param item_per_line items to be printed per line
 * @return              void
 *
 * Note: you may use sprintf()
 * Note: Be careful about adding a new line at the end of the output
 *       You need to add a new line only when necessary.
 *       Do NOT make a blank line by adding a new line when it is NOT
 *       necessary.
 */
void sprint_ascii(char* buffer, int start, int end, int item_per_line);
```

Hint: use casting to convert int to char.

### `string_compare()`
```cpp
/**
 * Compare two null-terminated strings lexicographically
 *
 * Similiar to std::strcmp()
 *
 * @param lhs       pointers to the null-terminated byte string to compare
 * @param rhs       pointers to the null-terminated byte string to compare
 * @return          -1: if lhs appres before rhs in lexicographical order
 *                   0: if lhs and rhs compare euqal
 *                   1: if lhs appres after rhs in lexicographical order
 */
int string_compare(const char* lhs, const char* rhs);
```

### `string_n_compare()`
```cpp
/**
 * Compare at most n characters of two null-terminated strings
 * lexicographically
 *
 * Similiar to std::strnmp()
 *
 * @param lhs       pointers to the null-terminated byte string to compare
 * @param rhs       pointers to the null-terminated byte string to compare
 * @param n         maximum number of characters to compare
 * @return          -1: if lhs appres before rhs in lexicographical order
 *                   0: if lhs and rhs compare euqal
 *                   1: if lhs appres after rhs in lexicographical order
 */
int string_n_compare(const char* lhs, const char* rhs, int n);
```

### `string_copy()`
```cpp
/**
 * Copy a C string from src to dst and return the destination pointer (dst)
 *
 * Equivalent to std::strcpy()
 *
 * @param dst       pointer to the character array to write to
 * @param src       source char array
 * @return          desitination char array (should be the same with dst)
 */
char* string_copy(char* dst, const char* src);
```

### `string_in()`
```cpp
/**
 * Return whether pattern includes character
 *
 * @param character character value
 * @param patterns  patterns to be compared
 * @return          0: if pattern does not include character
 *                  1: if pattern includes character
 */
int string_in(const char character, const char* pattern);
```
