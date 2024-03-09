// intlist_dynamic.cpp

#include <iostream>

#include "intlist.h"

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

IntList::IntList(const IntList& list)
{
    n = list.n;
    elem = new int[n];

    for (int i = 0; i < n; i++)
        elem[i] = list.elem[i];
}

IntList::~IntList()
{
    // we should use delete[]
    // since we allocated array
    delete[] elem;

    //cout << "IntList with " << n << " elements is destroyed." << endl;
}

IntList& IntList::operator=(const IntList& list)
{
    n = list.n;
    delete[] elem;
    elem = new int[n];
    for (int i = 0; i < n; i++)
        elem[i] = list.elem[i];
    return *this;
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

IntList IntList::operator+(const IntList& list)
{
    // FIXME: need to throw an exception
    // when the size of two lists differ
    int min_n = min(n, list.n);
    IntList tmp {*this};
    for (int i = 0; i < min_n; i++)
        tmp.elem[i] += list.elem[i];
    return tmp;
}

IntList& IntList::operator++()
{
    // Just an example
    // DO NOT overload operators,
    // which is NOT intuitive
    for (int i = 0; i < n; i++)
        ++elem[i];
    return *this;
}

IntList IntList::operator++(int)
{
    IntList old {*this};
    ++(*this);
    return old;
}

ostream& operator<<(ostream& output, const IntList& list)
{
    output << "[";
    for (int i = 0; i < list.n; i++)
        output << list.elem[i] << (i != list.n - 1 ? ", " : "");
    output << "]";

    return output; // to enable chaining
}
