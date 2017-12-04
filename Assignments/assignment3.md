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

1. Correct implementation of 4 functions: 70 pts.
2. Coding style: 30 pts.
  - Proper use of pointers and/or arrays
  - Readability of codes; indentation, variable/function names, etc.
  - Simple and clean code without redundancy
  - Adequate comments (SHOULD BE IN ENGLISH)

  **_Subject to change_**

## Overview

Write a C++ class called 'List'. Using templates and operator overloading, you should make the class behave like python 'list' class.

You need to impelment the following member or non-member functions.

_**Description will be added soon**_

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
    lst1.append(23);
    cout << lst1 << endl;
    cout << endl;

    cout << "Testing List<int> with operator overload...\n";
    List<int> lst2 = lst1 + lst1;
    cout << lst2 << endl;
    cout << endl;

    List<int> lst3 = lst1 + lst2;
    cout << lst3 << endl;
    cout << endl;

    cout << "Testing List<int>::pop()...\n";
    cout << "lst.pop(): " << lst3.pop() << endl;;
    cout << lst3 << endl;
    cout << "lst.pop(): " << lst3.pop() << endl;;
    cout << lst3 << endl;
    cout << endl;

    cout << "Testing List<double>...\n";
    List<double> lst4 {3.14, 1.618};
    cout << lst4 << endl;
    lst4 += lst4;
    cout << lst4 << endl;
    cout << endl;

    cout << "Testing List<std::string>...\n";
    List<string> lst5 {"python", "C++"};
    cout << lst5 << endl;
    lst5.append("Java");
    cout << lst5 << endl;
    lst5.append("Lisp");
    cout << lst5 << endl;
    cout << endl;

    cout << "Testing copy constructor...\n";
    List<string> lst6 {lst5};
    cout << lst6 << endl;
}

```

For the above code, you need to get the following results. The test code may include, but not limited to the above test cases.

```
Testing List<int>::append()...
[42, 23], size=2, capacity=2

Testing List<int> with operator overload...
[42, 23, 42, 23], size=4, capacity=4

[42, 23, 42, 23, 42, 23], size=6, capacity=8

Testing List<int>::pop()...
lst.pop(): 0
[42, 23, 42, 23, 42], size=5, capacity=8
lst.pop(): 23
[42, 23, 42, 23], size=4, capacity=8

Testing List<double>...
[3.14, 1.618], size=2, capacity=2
[3.14, 1.618, 3.14, 1.618], size=4, capacity=4

Testing List<std::string>...
[python, C++], size=2, capacity=2
[python, C++, Java], size=3, capacity=4
[python, C++, Java, Lisp], size=4, capacity=4

Testing copy constructor...
[python, C++, Java, Lisp], size=4, capacity=4
```

## Function specification

_**Description will be added soon**_
