constexpr double pi = 3.14159265;

class Shape {
protected:
    double width;
    double height;
public:
    Shape(double w, double h): width{w}, height{h} {}
    virtual double getArea() { return 0.; }
};

class Rectangle : public Shape {
public:
    Rectangle(double w, double h): Shape{w, h} {}
    double getArea() { return width * height; }
};

class Square : public Rectangle {
public:
    Square(double length) : Rectangle{length, length} {}
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double radius) : Shape{radius * 2., radius * 2.} { this->radius = radius; }
    double getArea() { return width * width * pi / 4.; }
    double getRadius() { return radius; }
};


