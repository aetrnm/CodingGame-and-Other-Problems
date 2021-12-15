#include <iostream>
#include <string>
#include <regex>

int main ()
{
    if (std::regex_match ("subject", std::regex("(sub)(.*)") ))
        std::cout << "string literal matched1\n";

    if (std::regex_match ("fox", std::regex("fox") ))
        std::cout << "string literal matched2\n";

    if (std::regex_match ("fox", std::regex("dog") ))
        std::cout << "string literal matched3\n";

    if (std::regex_match ("8", std::regex("[0-9]") ))
        std::cout << "string literal matched4\n";
    
    if (std::regex_match ("c", std::regex("[a-z]") ))
        std::cout << "string literal matched5\n";
    
    if (std::regex_match ("c", std::regex("[A-Z]") ))
        std::cout << "string literal matched6\n";
    
    if (std::regex_match ("21563", std::regex("[0-9]*") ))
        std::cout << "string literal matched7\n";

    if (std::regex_match ("asfgsdf", std::regex("[a-z]*")))
        std::cout << "string literal matched8\n";

    //std::string s = "The+ quick brown+ fox jumps+ over + the lazy dog";
    //std::string s = "ababab c acbacb abab esrgfh c";
    //std::string s = "T+h+e+ quick b+r+o+w+n+ fox jumps o+v+e+r+ the lazy dog";
    //std::string s = "sa09f0 32 46  fdgtrhy u 45 45frt";
    //std::string s = "The a alll bd quick brown ljh  lalala fox jumps bccdef over the facb lazy dog! ";
    std::smatch m;
    //std::regex re ("[a-z]+\\+");
    //std::regex re ("(ab)+");
    //std::regex re ("([a-zA-Z]\\+)+");
    //std::regex re ("\\b[al]+\\b");
    //std::regex re ("\\b[^al\\s]+\\b");
    // someline@domain.zone
    //std::regex re("\\b[b-km-zB-KM-Z]+\\b");
    std::string s = "This@is.an!24.email";
    std::regex re ("[a-zA-Z\\.]+\\@[a-z]+\\.[a-z]+");
    while(std::regex_search(s, m, re))
    {
        std::cout << m[0] << std::endl;
        s = m.suffix().str();
    }
    return 0;
}