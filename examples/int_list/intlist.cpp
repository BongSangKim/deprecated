// intlist.cpp

#include <iostream>

#include "intlist.h"

using namespace std;

IntList::IntList(int n_)
{

    // need to replace with dynamic mem mgmt
    n = n_ < max_list ? n_ : max_list;
    for (int i = 0; i < n_; i++)
        elem[i] = 0;
}

IntList::IntList(int n_, int* a)
{
    // need to replace with dynamic mem mgmt
    // need to add index err checking
    for (n = 0; n < n_; n++)
        elem[n] = a[n];
}

IntList::~IntList()
{
    cout << "IntList with " << n << " elements is destroyed." << endl;
}

int IntList::len()
{
    return n;
}

void IntList::set(int index, int value)
{
    // need to add index err checking
    elem[index] = value;
}

int IntList::get(int index)
{
    // need to add index err checking
    return elem[index];
}

void IntList::append(int value)
{
    elem[n++] = value;
}

