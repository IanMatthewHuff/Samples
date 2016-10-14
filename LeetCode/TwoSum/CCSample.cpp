#include <iostream>
#include <vector>
#include <unordered_map>

using std::cout;
using std::vector;
using std::unordered_map;

std::vector<int> add(std::vector<int> inputs, int target) {
   // Check inputs here including 0 and 1 items in inputs
   std::vector<int> targetValues;

    for(uint firstIndex = 0; firstIndex < inputs.size(); firstIndex++)
    {
        int firstInt = inputs[firstIndex];

        uint secondIndex = firstIndex + 1;
        if(secondIndex >= inputs.size())
        {
            continue;
        }

        for(; secondIndex < inputs.size(); secondIndex++)
        {
            int secondInt = inputs[secondIndex];

            if(firstInt + secondInt == target)
            {
                targetValues.push_back(firstInt);
                targetValues.push_back(secondInt);
                return targetValues;
            }
        }
    }
   
   return targetValues;
}

std::vector<int> add2(std::vector<int> inputs, int target)
{
    std::vector<int> targetValues;

    // Take a first pass and put all values into a map of index to value
    std::unordered_map<int, int> valueMap;

    for(uint index = 0; index < inputs.size(); index++)
    {
        int value = inputs[index];
        valueMap[value] = index;    // Map the index with value as the key
    }

    // Now we just look for the comp. values for each item in the array
    for(int value : inputs)
    {
        int comp = target - value;

        if(valueMap.find(comp) != valueMap.end())
        {
            targetValues.push_back(value);
            targetValues.push_back(comp);
            break;
        }
    }
    return targetValues;
}

int main(int argc, char *argv[], char *envp[]) {
    cout << "Hello World" << std::endl;

    vector<int> testData { 2, 3, 4, 5 };
    int target = 6; 

    //vector<int> returnValue = add(testData, target);
    vector<int> returnValue = add2(testData, target);

    // Print the results
    cout << "Results: ";
    for(int val : returnValue)
    {
        cout << val << " ";
    }
    
    cout << std::endl;

    return (0);
}


