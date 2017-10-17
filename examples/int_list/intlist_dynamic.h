// intlist_dynamic.h

class IntList
{
private:
    int n;
    int* elem;

public:
    IntList(int n_ = 0);
    IntList(int n_, int* a);
    ~IntList();
    int len() { return n; }
    void set(int index, int value) { elem[index] = value; }
    int get(int index) { return elem[index]; }
    void append(int value);
};

