// intlist_dynamic.h

#include <iostream>

using namespace std;

class IntList
{
private:
    int n;
    int* elem;

public:
    IntList(int n_ = 0);
    IntList(int n_, int* a);
    ~IntList();

    // copy constructor and assignment
    IntList(const IntList& list);
    IntList& operator=(const IntList& list);

    // others
    int len() { return n; }
    void set(int index, int value) { elem[index] = value; }
    int get(int index) { return elem[index]; }
    void append(int value);
    void display() {
        for (int i = 0; i < n; ++i)
            cout << elem[i] << " ";
        cout << endl;
    }

    // operator overloading
    IntList operator+(const IntList& list);
    IntList& operator++(); // prefix
    IntList operator++(int); // postfix
    friend ostream& operator<<(ostream& output, const IntList& list);
};

