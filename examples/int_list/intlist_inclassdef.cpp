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
    for (int n = 0; n < n_; n++)
        elem[n] = a[n];
}

IntList::~IntList()
{
    cout << "IntList with " << n << " elements is destroyed." << endl;
}

