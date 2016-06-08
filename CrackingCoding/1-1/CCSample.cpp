#include <iostream>
#include <unordered_map>

using std::cout;

bool checkUnique(std::string target) {
    // Assert here to check validity of target
    bool isUnique = true;

    std::unordered_map<char,char> seenChars;

    for(uint i = 0; i < target.size(); i++)
    {
        char current = target[i];

        if(seenChars.find(current) != seenChars.end())
        {
            isUnique = false;
            break;
        }

        seenChars.emplace(current, current);
    }

    return isUnique;
}

int main() {
    cout << "Hello World" << std::endl;

    cout << "Testing is: " << checkUnique("Testing") << std::endl;
    cout << "abcdefg is: " << checkUnique("abcdefg") << std::endl;
    cout << "xxxxxxx is: " << checkUnique("xxxxxxx") << std::endl;

    return (0);
}

