#include <iostream>
#include <string>
#include <ctime>
#include "time.h"

void printTime()
{
    std::time_t now = std::time(nullptr);
    std::cout << ", the time and date are " << std::ctime(&now) << std::endl;
}
