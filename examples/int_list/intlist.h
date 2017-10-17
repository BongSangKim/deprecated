#include <iostream>

using namespace std;

constexpr int max_list = 1024;

class IntList
{
private:
    int n;
    // need to replace with dynamic mem mgmt
    int elem[max_list] = {0, };
public:
    IntList(int n_ = 0);
    IntList(int n_, int* a);
    ~IntList();
    int len();
    void set(int index, int value);
    int get(int index);
    void append(int value);
};

