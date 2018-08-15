#include <iostream>
#include <cmath>
#include <vector>
#include "time.h"
#include <bitset>
#include <tuple>
#include <typeinfo>
#include <array>
#include <string.h>

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

void memoryArrayPointers()
{
   // Address with & deref with *
   int i = 42;
   int *pi = &i; 
   int j = *pi;

    // nullptr for uninit
    int *ipnull = nullptr;

    // Pointer arithmatic increases by the size of the type pointed to
    int v[] = { 1, 2, 3, 4, 5 };
    int *pv = v;
    *pv = 11;
    v[1] = 12;
    pv[2] = 13;
    *(pv + 3) = 14;

    // Arrays
    constexpr int sq_size = 4;
    int squares[sq_size];
    for (int i = 0; i < sq_size; ++i)
    {
        squares[i] = i * i;
    }
    for(int i : squares)
    {
        cout << i << endl;
    }
    
    // find out size / length
    int sq_sizeof = sizeof(squares);
    int sq_count = sizeof(squares) / sizeof(squares[0]);
    //int sq_count2 = _countof(squares);

    // as a function parameter arrays go down to a dumb pointer to type
    // so safecar(int tires[4]) is the same as safecar(int* tires)
    // Pass an array to a function first dimension of the array is pointer

    // MD arrays
    int four_by_three[4][3]; // four rows of three columns
    int two_by_three[2][3] = { 11, 12, 13, 21, 22, 23 }; // read as two groups of three
    int two_by_three2[2][3] = { {11, 12, 13} , {21, 22, 23} };

    // Passing an MD array the first index is flattened like bool checkThis(int checks[][5]);

}

void stringArrays()
{
    char p1[6];
    //strcpy_s(p1, 6, "hello");
    char p2[6];
    //strcpy_s(p2, 6, p1);
    // strcpy_s copy characters fromthe pointer in the last parameter (until NULL) into the first parameters
    // second param as max size to copy. Note we can't compare p1 and p2 as the pointers are different.

    // String comparison functions return an int not bool. If operand > parameter returns positive, if paramters is >    // the operand then returns -. Returns zero if the same. Overloaded == for std:: string

}

void basicPointers()
{
    // Not much reason to use anymore. Use null_ptr for pointers to deallocated memory
    // Pointers point to a specific type unless void* such as returned by malloc

    // Const can be funky syntax
    char c[] { "hello" }; // c as a pointer
    *c = 'H';             // Ok, can change the data pointed at
    const char *ptc {c};  // Pointer to constant character
    cout << ptc << endl;   // Ok, can read the memory pointed to
    //*ptc = 'Y';           // Not allowed, cannot write over the constant char data
    char *const cp {c};   // Constant pointer to character
    *cp = 'y';            // Can write to the char data
    //cp++;                 // Not allowed, cannot change where the pointer points
    // Read the name right to left to get the correct terms "ptr to const char" "const ptr to char"

    // static_cast to convert pointer type pointed at
    // int *pi = static_cast<int*>(malloc(sizeof(int))));
    // reinterpret_cast does the same with zero type checking
    
    // Allocations return typed pointer
    int *p = new int; // allocate memory for one int
    delete p;

    // delete calls destructor

    // Can initialize at new time
    int *p1 = new int (42);
    int *p2 = new int (42);

    delete p1;
    delete p2;

    // Also allocate arrays
    int *pa = new int[2];
    pa[0] = 1;
    *(pa + 1) = 2;
    delete []pa;

    // if allocation on new fails std::bad_alloc exception is thrown
}

void references()
{
    int i = 42;
    int& ri = i;
    ri = -1;
    int& ri2 = {i};
    ri2 = 2;

    // Reference is an alias to an object
    // it's an alias to the variable's name, can be used where ever the var name would be
    // Can only exist when initialized to a variable and only ever an alias to that one variable

    int j = 42;
    const int& rj = j;
    // Can't do rj = 99 as it's const for the data in ref
    
    // references are used when we don't want to be making copies all over the place
    // for example stream operators use them ostream& operator<<(ostream& _Ostr, int _val)
    // Need to be careful when returning a ref since you must ensure that object lifetime lasts
    // as long as the reference. Don't return a ref for a variable that is function scoped

    // for a const reference C++ will create a temp variable for the reference to use
    const int& cri { 42 };
    // temp int is created and aliased to cri. available to the ref while it is in scope

    // ranged for and refs
    constexpr int size = 4;
    int squares[size];
    for (int i = 0; i < size; ++i)
    {
        squares[i] = i * i;
    }

    // j is a copy of the items in squares, we can't change it
    for (int j : squares)
    {
        cout << j << endl;
    }

    // Now we can actually edit the values
    for (int& k : squares)
    {
        k *= 2;
    }
    // alias to actual member

    // can get interesting with 2D arrays
    int arr[2][3] = { { 2, 3, 4 }, { 5, 6, 7} };
    
    // for (auto row : arr)
    // {
    //     for (auto col : row) // will not compile
    //     {
    //         cout << col << " " << endl;
    //     }
    // }
    // outer loop gets a copy of each row as int[3], can't copy array so get an int*
    // which the next for can't find an iterator for

    // this actually works
    for (auto& row : arr)
    {
        for (auto col : row)
        {
            cout << col << " " << endl;
        }
    }
    // auto hides ugly types. Using a ref means that we have an alias to the int[3] not an int*


}

// RValue references added in C++11
// Lets us know if an rvalue is temporary or not. If temp, won't live after function is complete
// so we don't have to be careful about it. So for temp objects assignment can just move instead
// of copying the info. Can prevent an expensive copy, called move semantics.

string global{ "global" };

string& get_global()
{ return global; }

string& get_static()
{ static string str { "static" }; return str; }

string get_temp()
{ return "temp"; }

void moveSemantics()
{
    cout << get_global() << endl;
    cout << get_static() << endl;
    cout << get_temp() << endl;

    // First two return lived object, last returns a temp
    // use a reference parameter to pass the objects
    // Imagine a function use_string(string& myString)
    // use_string if it manipulated the string would need to first make a copy
    // because for get global or get static it would be changing the string reference
    // But for get_temp we could actually manipulate it without the copy as it's just a temp rvalue
    // Imagine a function use_string(string&& myString)
    // This version would actually be used if you call it like use_string(get_temp()) or use_string("CString")
    // The original version would be used for use_string(get_global) or use_string(str)
    // the new version can operate on the string without making a copy first

}

void STLArray()
{
   // STL array class, fixed size arrays on the stack, size known at compile time
   array<int, 4> arr { 1, 2, 3, 4 };
   for (int i : arr) cout << i << endl;
   int aSize = arr.size(); 
}

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
    //void f(int i);
    //short s = 42;
    //f(s); // s is promoted to int

    // Narrowing coversions go big to small and lose data
    // int i = 0.0 // converts down to 0 with a complier warning

    // Casting away constness
    const char* ptr = "12345678";
    char* pWrite = const_cast<char*>(ptr);
    pWrite[3] = 'A';

    // static_cast does no runtime check
    double pi = 3.14159;
    int pi_whole = static_cast<int>(pi); // No warning for narrowing due to cast

    // reinterpret_cast pointer of one type to another
    double pi3 = 3.14159;
    //int i = reinterpret_cast<int>(&pi);
    //cout << hex << i << endl; // print memory address of pi

    // dynamic_cast for casting with runtime checks

    // you can cast with initializer list
    double pi2 = 3.14159;
    //int i = {pi}; // will warn on narrowing

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

// functions

// You can use a function before you define it with a forward declaration
int myMult(int, int);

int myOtherFunction()
{
    myMult(5, 6);
}

int myMult(int lhs, int rhs)
{
    return lhs * rhs;
}
// If you add extern on the prototype you define that it is defined in another file
// Static on prototype indicates internal linkage and name can only be used in current file

// constexper if parameters are literals you can mark a function like this (also one line)
// makes it generated at compile time.
// inline suggests to the compiler that instead of a jump actually insert in function body

// Can write return value like so return type can be deduced if you omit the last bit
inline auto MyMult2(int lhs, int rhs) -> int
{ return lhs * rhs; }

// Mark with noexcept if it doesn't throw an exception
int increment(int param) noexcept
{ return param++; }

// Function parameters can do basic conversions if no specific overload is available.
// If you pass a temp to const & parameter it will make a copy to use

// Passing an initializer list
struct myPoint {int x; int y; };
void set_point(point pt);

int setPoints()
{
    point p;
    p.x = 1; p.y = 1;
    set_point(p);
    set_point({ 1, 1});
    return 0;
}
// Since this is pass by value the compiler creates a new point on the stack in the function

// default parameters. If not specified, use the default value. Done at declaration, not prototype
// always put default parameters on the far right
void log_message(const string& msg, bool clear_screen = false)
{
    if (clear_screen) { };
    cout << msg << endl;
}

// Pass by reference here as an out parameter. Lets us actually change the vector
bool get_items(int count, vector<int>& values)
{
    for (int i = 0; i < count; ++i)
    {
        values.push_back(i);
    }
    return true;
}

// pointer to pointer to have a pointer as an out parameter

// Pre and post conditions. Assumptions about the data coming in and coming out of a function

// If you leave off the () on a function you actually get the function address
int getMyStatus()
{
    return 1;
}

void functionPointers()
{
    void *pv = getMyStatus;
    int (*fn)() = getMyStatus; // Pointer to a function
    int error_value = fn();    // Now call the function via the pointer

    // Can often use an alias
    // using pf1 = int(*)();
    // typedef int (*pf2)();
    // using MyPtr = bool(*)(MyType*, MyType*)
    // Parens are used to break the associativity of the * operator    

    using callback = void(*)(const string&);

    void big_routine(int loopCount, const callbackProgress)
    {
        for (int i = 0; i < loopCount; ++i)
        {
            if(i % 100 == 0)
            {
                string msg ("loop ");
                progress(msg);
            }
        }
    }

    void monitor(const string& msg)
    {
        cout << msg << endl;
    }

    big_routine(1000, monitor);
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
