#include <algorithm>
#include <iostream>
#include <regex>
#include <vector>
#include <sstream>
//#include <boost/algorithm/string>

using namespace std;

void solution1()
{
    string s;
    cin >> s;
    vector<int> v;
    v.resize(100);
    //some.text.of.this.type <- R
    //some_text_of_another_type <- такое уже не парсится
    stringstream ssin(s);
    int numberOfElements = 0;
    while (ssin.good()){
        ssin >> v[numberOfElements];
        numberOfElements++;
    }
    
    sort(v.begin(), v.begin()+numberOfElements);
    for (int i = 0; i < numberOfElements; i++)
    {
        if (i == numberOfElements - 1)
        {
            cout << v[i];
        }
        else
        {
            cout << v[i] << '+';
        }
    }
}

void solution2()
{
    string s;
    cin >> s;
    vector<int> v;
    smatch m;
    regex re ("[0-9]+");
    int numberOfElements = 0;
    while(std::regex_search(s, m, re))
    {
        v.push_back(stoi(m[0]));
        s = m.suffix().str();
        numberOfElements++;
    }

    sort(v.begin(), v.begin()+numberOfElements);
    for (int i = 0; i < numberOfElements; i++)
    {
        if (i == numberOfElements - 1)
        {
            cout << v[i];
        }
        else
        {
            cout << v[i] << '+';
        }
    }
}

auto main() -> int
{
    // solution1();
    solution2();
    
    return 0;
}
