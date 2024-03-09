# Assignment #3

## Notes

The description of this assignment will be updated as needed. Please check this page frequently.

## Due

The due of this assignment is 11:59 pm on 12/16 (Sat). It is strongly recommend to fully understand what this assignment covers before taking final exam. The final exam will cover templates and operator overloading (the scope of this assignment).

Submission after the due WILL NOT be accepted.

## Submission

You are required to submit your assignment on elice. As of now, the assignment is NOT prepared on elice.io. The notice will be made when it is ready.

The entry will be open soon.

## Scores

1. Correct implementation of 11 functions: 120 pts.
2. Coding style: 30 pts.
  - Proper use of pointers and/or arrays
  - Readability of codes; indentation, variable/function names, etc.
  - Simple and clean code without redundancy
  - Adequate comments (SHOULD BE IN ENGLISH)

  **_Subject to change_**

## Overview

Write a C++ class called 'List'. Using templates and operator overloading, you should make the class behave like python 'list' class.

You need to impelment the following member or non-member functions.


## Sample output

```cpp
#include <iostream>
#include <string>
#include "list.h"

using namespace std;

int main()
{
    cout << "Testing List<int>::append()...\n";
    List<int> lst1;
    lst1.append(42);
    lst1.append(1024);
    lst1.append(23);
    cout << "lst1: " << lst1 << endl;
    cout << endl;

    cout << "Testing List<int> with operator overload...\n";
    List<int> lst2 = lst1;
    cout << "lst2: " << lst2 << endl;

    List<int> lst3 = lst1 + lst2;
    cout << "lst3: " << lst3 << endl;
    cout << endl;

    cout << "Testing List<int>::pop()...\n";
    cout << "lst.pop(): " << lst3.pop() << endl;;
    cout << "lst3: " << lst3 << endl;
    cout << "lst.pop(): " << lst3.pop() << endl;;
    cout << "lst3: " << lst3 << endl;
    cout << endl;

    cout << "Testing List<double>...\n";
    List<double> lst4 {3.14, 1.618};
    cout << "lst4: " << lst4 << endl;
    lst4 += lst4;
    cout << "lst4: " << lst4 << endl;
    cout << endl;

    cout << "Testing List<std::string>...\n";
    List<string> lst5 {"python", "C++"};
    cout << "lst5: " << lst5 << endl;
    lst5.append("Java");
    cout << "lst5: " << lst5 << endl;
    lst5.append("Lisp");
    cout << "lst5: " << lst5 << endl;
    cout << endl;

    cout << "Testing copy constructor...\n";
    List<string> lst6 {lst5};
    cout << "lst6: " << lst6 << endl;
    cout << endl;

    cout << "Test list initializer...\n";
    List<int> lst7 {2, 3, 5, 7, 11, 13};
    cout << "lst7: " << lst7 << endl;
    cout << endl;
}
```

For the above code, you need to get the following results. The test code may include, but not limited to the above test cases.

```
Testing List<int>::append()...
lst1: [42, 1024, 23], size=3, capacity=4

Testing List<int> with operator overload...
lst2: [42, 1024, 23], size=3, capacity=3
lst3: [42, 1024, 23, 42, 1024, 23], size=6, capacity=6

Testing List<int>::pop()...
lst.pop(): 23
lst3: [42, 1024, 23, 42, 1024], size=5, capacity=6
lst.pop(): 1024
lst3: [42, 1024, 23, 42], size=4, capacity=6

Testing List<double>...
lst4: [3.14, 1.618], size=2, capacity=2
lst4: [3.14, 1.618, 3.14, 1.618], size=4, capacity=4

Testing List<std::string>...
lst5: [python, C++], size=2, capacity=2
lst5: [python, C++, Java], size=3, capacity=4
lst5: [python, C++, Java, Lisp], size=4, capacity=4

Testing copy constructor...
lst6: [python, C++, Java, Lisp], size=4, capacity=4

Test list initializer...
lst7: [2, 3, 5, 7, 11, 13], size=6, capacity=6
```

## Function specification

### `List<T>::List(int n_)`

```
/*
 * Reserve a space for n_ items of type T, and set the member variables
 * as needed
 *
 * @param n_    the number of items that should be reserved for
 */
template<typename T>
List<T>::List(int n_);
```

### `List<T>::List(List<T> const& list)`

```
/*
 * Copy constructor
 *
 * Allocate memory for the items stored in list
 *
 * @param list    an instance of List<T>
 */
template<typename T>
List<T>::List(List<T> const& list);
```

### `List<T>::List(initializer_list<T> list)`

```
/*
 * Construct List<T> with the items in argument list
 *
 * Reserve capacity for the number of items in list
 *
 * @param   list    an initializer list with items of type T
 */
template<typename T>
List<T>::List(initializer_list<T> list);
```

### `List<T>::~List()`

```cpp
/*
 * Deconstruct List<T>
 *
 * deallocate any memory if necessary
 */
template<typename T>
List<T>::~List();
```

### `List<T>::reserve(int new_cap)`

```cpp
/*
 * Reserve storage
 *
 * Increase the capacity of List to a value to new_cap. If new_cap is
 * greater than the current capacity(), new storage is allocated, otherwise
 * this function does nothing
 *
 * When a new memory is allocated, you should copy the existing items
 * to a newly allocated memory.
 *
 * @param   new_cap     the size of newly reserved memory (int)
 */
template<typename T>
void List<T>::reserve(int new_cap);
```

### `List<T>::operator=(List<T> const& list)`

```cpp
/*
 * Copy assignment
 *
 * Copy all the items to the current instance of List<T>
 *
 * If the number of items exceeds capacity() of the current instance,
 * allocate a new memory with the number of items in list.
 *
 * @param   list    an instance of List<T>, from where items should be copied
 * @return          the current instance
 */
template<typename T>
List<T>& List<T>::operator=(List<T> const& list);
```
### `List<T>& List<T>::operator+=(List<T> const& list)`

```cpp
/*
 * Append all the items in the argument list to the end of the current
 * instance of List<T>
 *
 * If there is not enough reserved memory, allocate a memory with the
 * size of the number of items in the current instance plus the number of
 * items in list
 *
 * @param   list an instance of List<T> whose items should be appended
 * @retur        the current instance of List<T>
 */
template<typename T>
List<T>& List<T>::operator+=(List<T> const& list);
```

### `operator+(List<T> const& lhs, List<T> const& rhs)`

```cpp
/*
 * Create a new instance of List<T> which holds all the items in lhs and
 * all the items in rhs (in order)
 *
 * @param   lhs     an instance of List<T>
 * @param   rhs     an instance of List<T>
 * @return          the newly created instance of List<T>
 */
template<typename T>
List<T> operator+(List<T> const& lhs, List<T> const& rhs);
```

### `operator<<(ostream& output, List<T> const& list)`

```cpp
/*
 * Print the items to the output stream
 *
 * The output format should follow that of python list, i.e.,
 *   - print '['
 *   - if there is any item, print that item
 *   - if there is more than one item, print ", " between items
 *   - after the last item (or after '[' if there is none), print ']'
 *   - print ", size="
 *   - print size()
 *   - print ", capacity=:
 *   - print capacity()
 *   - Note: DO NOT CHANGE THE LINE
 *
 * @param   output  an instance of ostream where the items of list
 *                  will be printed
 * @param   list    an instance of List<T>
 * @return          ostrem (the first arugment)
 * Do not change the line after printing ']'
 */
template<typename T>
ostream& operator<<(ostream& output, List<T> const& list);
```

### `append(T const& value)`

```cpp
/*
 * Append value to the end of this container (List<T>)
 *
 * Double capacity() if necessary
 *
 * @param   value   a value to be added to the List<T>
 */
template<typename T>
void List<T>::append(T const& value);
```

### `List<T>::pop()`

```cpp
/*
 * Removes the last element and return it
 *
 * @return      the last element
 */
template<typename T>
T List<T>::pop();
```
