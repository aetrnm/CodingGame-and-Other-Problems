#include <iostream>
#include <regex>

void turnToLowerCase(std::string& s)
{
    std::transform(s.begin(), s.end(), s.begin(),
    [](unsigned char c){return std::tolower(c);});
}

void solution1()
{
    std::string initial, toSearch;
    std::getline(std::cin, initial);  // "Abc abc"
    std::getline(std::cin, toSearch); // "abc"
    // не важен кейс: 2
    
    turnToLowerCase(initial);
    turnToLowerCase(toSearch);
    
    std::regex re (toSearch);
    std::smatch m;

    int numberOfElements = 0;
    while(std::regex_search(initial, m, re))
    {
        initial = m.suffix().str();
        numberOfElements++;
    }

    std::cout << numberOfElements << std::endl;
}

int main()
{
    solution1();
    
    return 0;
}
