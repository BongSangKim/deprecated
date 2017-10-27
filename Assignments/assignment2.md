# Assignment #2

## Notes

The description of this assignment will be updated as needed. Please check this page frequently.

## Due

The due of this assignment is 11:59 pm on 11/8 (Wed). But it is strongly recommend to spend sometime on this problems before taking midterm.

Submission after the due WILL NOT be accepted.

## Submission

You are required to submit your assignment on elice. As of now, the assignment is NOT prepared on elice.io. The notice will be made when it is ready.

The entry will be open by 10/28 (Sat).

## Overview

Write 4 member functions for class `IntList`.

* append()
* pop()
* min_max()
* copy_from()

In this assignment, you are supposed to improve the dynamic memory management version of class `IntList`.

Check the following files at
 https://github.com/chomg/se271_2017/tree/master/examples/int_list
 - intlist_dynamic.h
 - intlist_dynamic.cpp

This version of the class performs poorly when we append a value one by one with `append()` function. Whenever `append()` is called, it allocates a new memory to store one more element and copies all the elements in `elem` to a newly allocated memory.

To alleviate this problem, we want to allocate spare spaces in advance. The member variable `sz` is added to store the capacity (i.e., the size of allocated memory).

So the member functions which may increase the capacity, we should be very careful about dynamic memory management not to access memory area beyond the allocated memory. See the requirement of `append()` and `copy_from()` for details.

## Sample output

```cpp
#include <iostream>
#include "intlist.h"

using namespace std;

int main()
{
    IntList t1;
    IntList t2 {2};
    int result;
    int max;
    int min;

    cout << "t1: len=" << t1.len() << ", capacity=" << t1.capacity() << endl;
    t1.append(42);
    cout << "t1: len=" << t1.len() << ", capacity=" << t1.capacity() << endl;
    t1.append(23);
    cout << "t1: len=" << t1.len() << ", capacity=" << t1.capacity() << endl;
    t1.append(1024);
    cout << "t1: len=" << t1.len() << ", capacity=" << t1.capacity() << endl;

    cout << "Before copying_from...\n";
    cout << "t2: len=" << t2.len() << ", capacity=" << t2.capacity() << endl;
    for (int i = 0; i < t2.len(); i++)
        cout << "t2[" << i << "]=" << t2.get(i) << endl;

    t2.copy_from(&t1); // copy t1 to t2

    cout << "After copying_from...\n";
    cout << "t2: len=" << t2.len() << ", capacity=" << t2.capacity() << endl;
    for (int i = 0; i < t2.len(); i++)
        cout << "t2[" << i << "]=" << t2.get(i) << endl;

    result = t1.min_max(&min, &max);
    cout << "t1: return value of min_max()=" << result;
    cout << ", min=" << min << ", max=" << max << endl;
    cout << "t1: poped value=" << t1.pop() << endl;
    cout << "t1: len=" << t1.len() << ", capacity=" << t1.capacity() << endl;
    cout << "t1: poped value=" << t1.pop() << endl;
    cout << "t1: len=" << t1.len() << ", capacity=" << t1.capacity() << endl;
    cout << "t1: poped value=" << t1.pop() << endl;
    cout << "t1: len=" << t1.len() << ", capacity=" << t1.capacity() << endl;
    result = t1.min_max(&min, &max);
    cout << "t1: return value of min_max()=" << result << endl;
}
```

For the above code, you need to get the following results. The test code may include, but not limited to the above test cases.

```
t1: len=0, capacity=0
t1: len=1, capacity=2
t1: len=2, capacity=4
t1: len=3, capacity=4
Before copying_from...
t2: len=2, capacity=2
t2[0]=0
t2[1]=0
After copying_from...
t2: len=3, capacity=4
t2[0]=42
t2[1]=23
t2[2]=1024
t1: return value of min_max()=0, min=23, max=1024
t1: poped value=1024
t1: len=2, capacity=4
t1: poped value=23
t1: len=1, capacity=4
t1: poped value=42
t1: len=0, capacity=4
t1: return value of min_max()=-1
```

## Function specification

### `IntList::append()`
```cpp
/**
 * Copy the parameter 'value' to the end of elem,
 * increasing the number of elements stored in 'elem' by 1.
 *
 * If necessary, increase the capacity of the elem (i.e., the size of
 * allocated memory);
 *     when the current capacity is 0, increase by init_list_size
 *     otherwise; double the capacity
 *
 * @param value     int value
 */
void IntList::append(int value);
```

### `IntList::pop()`
```cpp
/**
 * Remove the last element in elem and return it;
 * as a result, the number of elements stored in 'elem' is decreased by 1
 *
 * @return          the last element stored in elem
 */
int IntList::pop();
```
### `IntList::min_max()`
```cpp
/**
 * Copy the maximum value stored in 'elem' to the memory pointed by max,
 * and copy the minimum value stored in 'elem' to the memory pointed by min
 *
 * @return          -1: if the member variable 'n' is 0 (i.e., elem does not
 *                      store anything); and the values pointed by min and max
 *                      are not changed in this case
 *                  0: otherwise
 */
int IntList::min_max(int* min, int* max);
```

### `IntList::copy_from()`
```cpp
/**
 * Copy n, capacity (=sz) and elements stored in elem from 'list';
 * as a result, this instance should have the same values for 'n' and 'sz'
 * with those of 'list', and store the same elements in 'elem' with those in
 * 'elem' of 'list'.
 *
 * If necessary (the capacity of 'list' is greater than the capacity of this
 * instance, you should allocate new memory.
 *
 * @param list     another instance of IntList
 */
void IntList::copy_from(IntList* list);
```
