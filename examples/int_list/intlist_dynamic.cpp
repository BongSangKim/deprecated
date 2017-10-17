// intlist_dynamic.cpp
/
#include <iostream>

#include "intlist_dynamic.h"

using namespace std;

IntList::IntList(int n_)
{
    n = n_;
    elem = new int[n];

    for (int i = 0; i < n; i++)
        elem[i] = 0;
}

IntList::IntList(int n_, int* a)
{
    elem = new int[n];

    for (n = 0; n < n_; n++)
        elem[n] = a[n];
}

IntList::~IntList()
{
    // we should use delete[]
    // since we allocated array
    delete[] elem;

    cout << "IntList with " << n << " elements is destroyed." << endl;
}

void IntList::append(int value)
{
    // This is NOT an efficient implementation
    int* new_elem = new int[n + 1];
    for (int i = 0; i < n; i++)
        new_elem[i] = elem[i];
    // can we exchange the order of the following lines?
    delete[] elem;
    elem = new_elem;
    elem[n++] = value;
}

