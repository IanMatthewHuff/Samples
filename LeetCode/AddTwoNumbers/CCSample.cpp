#include <iostream>
#include <vector>
using std::cout;
using std::vector;

struct ListNode
{
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* ConstructList(std::vector<int> intValues)
{
    ListNode* returnList = nullptr;
    ListNode* previousNode = nullptr;
    for(int val : intValues)
    {
       ListNode* currentNode = new ListNode(val);

       // Head
       if(returnList == nullptr)
       {
            returnList = currentNode;
       }

       // Link in item
       if(previousNode != nullptr)
       {
            previousNode->next = currentNode;
       }

       // Move forward our list
       previousNode = currentNode;
    }

    return returnList;
}

void DeleteList(ListNode* head)
{
    ListNode* currentNode = head;
    
    while(currentNode != nullptr)
    {
        ListNode* nextNode = currentNode->next;
        delete currentNode;
        currentNode = nextNode;
    }
}

ListNode* AddLists(ListNode* left, ListNode* right)
{
    ListNode* returnList = nullptr;
    ListNode* previousNode = nullptr;
    bool carryOne = false;

    while(!(left == nullptr && right == nullptr))
    {
        int leftValue = 0;
        int rightValue = 0;

        if(left != nullptr) {
            leftValue = left->val;
            left = left->next;
        }

        if(right != nullptr) {
            rightValue = right->val;
            right = right->next;
        }
        
        // Have left and right values now
        int combo = leftValue + rightValue;
        if(carryOne)
        {
            combo++;
        }

        if (combo > 9)
        {
            carryOne = true;
            combo = combo - 10;
        }
        else
        {
            carryOne = false;
        }

        ListNode* newNode = new ListNode(combo);

        if(returnList == nullptr)
        {
            returnList = newNode;
        }

        else
        {
            previousNode->next = newNode;
        }

        // Move our pointer forward
        previousNode = newNode;
    }

    // Bug: could be one final carryOne here
    if (carryOne)
    {
        ListNode* finalNode = new ListNode(1);
        previousNode->next = finalNode;
    }

    return returnList;
}

void PrintList(ListNode* target)
{
    while(target != nullptr)
    {
        cout << target->val << " - ";
        target = target->next;
    }
    cout << std::endl;
}

int main(int argc, char *argv[], char *envp[]) {
    cout << "Hello World" << std::endl;

    // Construct our sample data here
    vector<int> numberOne { 2, 4, 3 };
    vector<int> numberTwo { 5, 6, 4 };

    ListNode* listOne = ConstructList(numberOne);
    PrintList(listOne);
    ListNode* listTwo = ConstructList(numberTwo);
    PrintList(listTwo);

    // Do our work here
    ListNode* valueList = AddLists(listOne, listTwo);
    PrintList(valueList);

    DeleteList(listOne);
    DeleteList(listTwo);
    DeleteList(valueList);

    return (0);
}
