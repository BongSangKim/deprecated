#include <iostream>
#include <iterator>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
    istringstream stream("1 2 3 4 5");
    copy(
        istream_iterator<int>(stream),
        istream_iterator<int>(),            // until the end of the stream
        ostream_iterator<int>(cout, " ")
    );

    // just to change a line
    cout << endl;
}

