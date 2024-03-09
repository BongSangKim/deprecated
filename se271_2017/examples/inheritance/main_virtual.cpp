#include <iostream>
#include "shapes_virtual.h"

using namespace std;

void foo()
{
    Rectangle r {1, 2};
    Circle c {2};
    Shape* shapes[] {&r, &c};
    cout << shapes[0]->getArea() << endl;
    cout << shapes[1]->getArea() << endl;
}

int main()
{
    Rectangle rectangle {1, 2};
    Square square {3};
    Circle circle {2};
    cout << "Area of rectangle: " << rectangle.getArea() << endl;
    cout << "Area of square: " << square.getArea() << endl;
    cout << "Area of circle: " << circle.getArea() << endl;
    cout << "Radius of circle: " << circle.getRadius() << endl;

    Shape* shapes[3];
    shapes[0] = new Rectangle(1, 2);
    shapes[1] = new Square(3);
    shapes[2] = new Circle(2);
    for (int i = 0; i < 3; i++)
        cout << "Area of shapes[" << i << "]="
             << shapes[i]->getArea() << endl;

    // just to show this works
    foo();
}

