#include <iostream>
#include "shapes_original.h"

using namespace std;

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
}

