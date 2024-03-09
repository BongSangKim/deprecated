#include <iostream>

using namespace std;

constexpr int max_list = 1024;

class IntList
{
private:
    int n;
    // need to replace with dynamic mem mgmt
    int elem[max_list];

public:
    IntList(int n_ = 0);
    IntList(int n_, int* a);
    ~IntList();
    int len() { return n; }
    void set(int index, int value) { elem[index] = value; }
    int get(int index) { return elem[index]; }
    void append(int value) { elem[n++] = value; }
};

