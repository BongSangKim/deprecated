#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

void parser(istream& is)
{
    for (string line; getline(is, line); ) {
        if (line == "qq")
            break;

        istringstream iss {line};
        vector<string> words {istream_iterator<string> {iss},
                              istream_iterator<string> {}};

        cout << "tokenized words\n---------------\n";
        for (string& w: words)
            cout << w << endl;
    }
}

int main(int argc, const char* argv[])
{
    if (argc > 1) {
        // if command line argument is provided,
        // take the first argument as a filename
        ifstream ifs {argv[1]};
        if (ifs)
            parser(ifs);
        else
            cout << "Cannot open " << argv[1] << endl;
    }
    else
        parser(cin);
}

