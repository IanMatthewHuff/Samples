#include <iostream>
#include <cmath>
#include <vector>
#include "time.h"
#include <bitset>
#include <tuple>
#include <typeinfo>

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
using std::vector;
using namespace std;

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

void types()
{
    char chType = 1; // 1 byte 32-bit system
    chType++;
    short shType = 1; // 2 bytes
    shType++;
    int itType = 1; // 4 bytes
    itType++;
    long lgType = 1; // 4 bytes
    lgType++;
    long long lglgType = 1; // 8 bytes
    lglgType++;

    // the <cstdlib> header has non variable int types like int8_t -> int64_t for 1 to 8 bytes
    int charBytes = sizeof(chType);
    cout << endl << charBytes << endl;

    unsigned long long every_other = 0xAAAA'AAAA'AAAA'AAAA;
    std::bitset<64> bs_every(every_other);
    cout << bs_every << endl;
    bs_every.set(0);  // Sets the bit at position 0 to 1
    every_other = bs_every.to_ullong();
    cout << bs_every << endl;
    cout << every_other << endl;

    double one = 0.001;
    float onefl = 1.0f;
    long double oneLong = 1e6L;
    cout << one << onefl << oneLong << endl;
}

// Reverse the byte order of a unsigned short
// Big Endian: First Byte is highest byte
// Little Endian: First Byte is the smallest byte
unsigned short reverseUShortByteOrder(unsigned short us)
{
    return ((us & 0xff) << 8) | ((us & 0xff00) >> 8);
}

// basic strings and characters
void stringchar()
{
    //char t = 't'; // 8 bit character
    //wchar_t wct = 't'; // largest extended character set
    //wchar_t wct1 = L'$'; // Normal chars are promoted. L makes the wide explicit

    // <cctype> header has c style functions for testing characters
    // like isdigit isalpha isspace isupper
    // also modify like toupper and tolower

    // String literal to escape all
    cout << R"(newline is \n in C++ and "quoted text" use quotes)";
}

void initialization()
{
    //int i = 1;
    //int j = int(2);
    //int k(3);
    //int m{4};

    // Careful
    vector<int> a1(42);
    cout << " size " << a1.size() << endl;
    for(int i : a1)
    {
        cout << i << endl;
    }
    
    vector<int> a2{42};
    cout << " size " << a2.size() << endl;
    for(int i : a2)
    {
        cout << i << endl;
    }
    // The first sizes to 42 with all zeros
    // the second is size 1 with a single element 42

    //int a {};  // Initialize to default value of type

    // auto to initialize via the inferred type
    vector<tuple<string, int> > beatles;
    beatles.push_back(make_tuple("John", 1940));
    beatles.push_back(make_tuple("Paul", 1942));
    beatles.push_back(make_tuple("George", 1943));
    beatles.push_back(make_tuple("Ringo", 1940));

    for (auto musician : beatles)
    {
        cout << get<0>(musician) << " " << get<1>(musician) << endl;
    }

    // static = local only to current file : extern = visible to other source files
    // thread_local each thread has copy of variable

    #define name_year tuple<string, int>
    // not the best as it replaces all text
    //typedef tuple<string, int> name_year_t;
    // better and can alias more times like so
    //typedef vector<name_year_t> musician_collection_t;
    // musician_collection_t beatles2;
    
    // New C++11 syntax for this
    using name_year_using = tuple<string, int>;
}

void aggregatetypes()
{
    // remember public by default
    struct time_of_day
    {
        int sec;
        int min;
        int hour;
    };

    time_of_day startWork;
    startWork.sec = 0;
    startWork.min = 20;
    startWork.hour = 8;
    
    // initializer list with initialize items in order
    // remaining members set to zero if not enough
    time_of_day lunch {0, 0, 12};
    time_of_day midnight{};

    // Nesting
    struct workingHours
    {
        time_of_day startWork;
        time_of_day endWork;
    };

    workingHours weekday {{0,30,8},{0,0,17}};
    
    struct item_length
    {
        unsigned short len : 10;
        unsigned short : 5;
        bool dirty : 1;
    };
    // the : 1 specifies the bits of space. So this uses 10 bits and a single dirty bit

    // Unions to say one or the other of two types in a structure
    union d_or_i {double d; long long i;}; // Can be double or long long
    d_or_i test;
    test.i = 42; // Can't do test.d now

    // use typeif() function for name / info of a type at runtime
    int i = 42;
    cout << "i type name: " << typeid(i).name() << endl;
    // can compare type_info classes with == or !=
}

// Type conversion
void TypeConversion()
{
    // Promotion smaller types are promoted to larger types
    void f(int i);
    short s = 42;
    f(s); // s is promoted to int
}

void looping()
{
    for (int i = 0; i < 10; ++i)
    {
        std::cout << i << " ";
    }
    
    std::cout << std::endl;

    vector<std::string> beatles = {"John", "Paul", "George", "Ringo"};
    for(uint i = 0; i < beatles.size(); ++i)
    {
        cout << beatles.at(i) << std::endl;
    }

    for (std::string musician : beatles)
    {
        cout << musician << endl;
    }
}

void input()
{
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

    int inputI;
    std::cout << "Enter a number: ";
    std::cin >> inputI;
    switch(inputI)
    {
        case 1:
            std::cout << "one" << std::endl;
            break;
        case 2:
            std::cout << "two" << std::endl;
            break;
        default:
            std::cout << "other" << std::endl;
            break;
    }
}

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

    // test input
    //input();

    // test looping
    //looping();

    // test types
    //types();

    // test strings and characters
    //stringchar();

    // test initialization
    initialization();
}
