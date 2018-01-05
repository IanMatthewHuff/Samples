#include <iostream>
#include <cmath>
#include "time.h"

// Test a define
#define NUMBER 4
// Test a Macro
#define LINEPRINT(s) std::cout << s << std::endl;
// Const
const double sqrtOf2 = std::sqrt(2);

const double pi = 3.14159;

// constexpr function
constexpr int triang(int i)
{
    return (i == 0) ? 0 : triang(i - 1) + i;
}

using std::cout;
using std::endl;

namespace utilities
{
    bool pollData()
    {
        return true;
    }
    int getData();

    namespace V2
    {
        int getData();
    }
}

namespace ut = utilities;

int utilities::getData()
{
    return 1;
}

int utilities::V2::getData()
{
    return 2;
}

// Non class enum
enum suits {clubs, diamonds, hearts, spades};

// Enum class
enum class suits2 {clubs, diamonds, hearts, spades};

// Set data type
enum class suit : char {clubs, diamonds, hearts, spades};

// Entry point
int main(int argc, char *argv[])
{
    std::cout << "Hello, world!" << std::endl;
    std::cout << "There are: " << argc << " parameters" << std::endl;
    for (int i = 0; i < argc; ++i)
    {
        std::cout << argv[i] << std::endl;
    }
    std::cout << "Define value is: " << NUMBER << std::endl;
    LINEPRINT("Test Macro");
    LINEPRINT(5);

    std::cout << "Your first name? ";
    std::string name;
    std::cin >> name;
    std::cout << name << std::endl;

    printTime();

    if(utilities::pollData())
    {
        int i = utilities::getData();
        std::cout << i << std::endl;
    }
}
