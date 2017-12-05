#include <iostream>

#ifdef INITIAL
#include "intlist_initial.h"
#endif

#ifdef INCLASS
#include "intlist_inclassdef.h"
#endif

#ifdef DYNAMIC
#include "intlist_dynamic.h"
#endif

#ifdef FINAL
#include "intlist.h"
#endif

using namespace std;

#ifdef FINAL
int foo()
{
    IntList list1 {2};
    list1.set(0, 42);
    list1.set(1, 23);
    cout << list1 << endl;
    IntList list2 = list1 + list1;
    //IntList list2;
    list2 = list1 + list1;

    cout << list1 << endl;;
    cout << list2 << endl;;
    cout << list1++ << endl;;
    cout << ++list1 << endl;;

    return 0;
}
#endif

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

    // copy constructor and copy assignment
    IntList list1 {2};
    list1.set(0, 42);
    list1.set(1, 23);
    IntList list2 = list1;
    IntList list3 {list1};

    list1.set(0, 63);

    list1.display();
    list2.display();
    list3.display();

#ifdef FINAL
    foo();
#endif
}

