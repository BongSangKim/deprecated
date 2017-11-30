#include <iostream>

using namespace std;

class complex {
    double re, im;
public:
    complex(double r = 0., double i = 0.) : re(r), im(i) {}
    double real() { return re; }
    double imag() { return im; }

    complex& operator+=(complex b);
};

complex& complex::operator+=(complex b)
{
    re += b.re;
    im += b.im;

    return *this;
}

ostream& operator<<(ostream& output, complex c)
{
    output << "(" << c.real() << "," << c.imag() << ")";
    return output;
}

// define operator+ using operator +=
complex operator+(complex a, complex b)
{
    return a += b;
}

int main()
{
    complex unit_x {1., 0.};
    complex unit_y {0., 1.};

    cout << unit_x << endl;
    cout << unit_y << endl;

    complex c {unit_x};
    cout << c << endl;

    c += unit_x;
    cout << c << endl;

    c = unit_x + unit_y;
    cout << c << endl;

}

