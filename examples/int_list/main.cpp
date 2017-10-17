#include <iostream>

#ifdef INITIAL
#include "intlist.h"
#endif

#ifdef INCLASS
#include "intlist_inclassdef.h"
#endif

#ifdef DYNAMIC
#include "intlist_dynamic.h"
#endif

using namespace std;

int main()
{
    IntList list(3);
    for (int i = 0; i < list.len(); i++)
        cout << list.get(i) << ' ';
    cout << endl;
    list.append(42);
    for (int i = 0; i < list.len(); i++)
        cout << list.get(i) << ' ';
    cout << endl;
}

