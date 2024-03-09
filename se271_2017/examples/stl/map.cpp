#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

class Simple {
    int value;
public:
    Simple(int v = 0) : value(v) {}
    int getValue() { return value; }
    void setValue(int v) { value = v; }
};

int main()
{
    //Note: For this simple case, it may be okay to use array,
    //but using vector would be recommended in most cases
    vector<string> keys {"cpp", "python", "java"};
    map<string, Simple> m;

    Simple s;
    for (auto key: keys)
        m[key] = s;

    for (auto key: keys)
        cout << key << ": " << m[key].getValue() << endl;

    m["cpp"].setValue(271);
    m["python"].setValue(213);
    m["java"].setValue(999);

    for (auto key: keys)
        cout << key << ": " << m[key].getValue() << endl;
}
