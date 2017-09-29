import sys

def function(testValues, targetValue):
    valueMap = {}
    for currVal in testValues:
        valueMap[currVal] = currVal

    # Now iterate the complements of the testValues
    for currVal in testValues:
        comp = targetValue - currVal
        if comp in valueMap:
            return [currVal, comp]

    return

def main():
    print 'Hello there'
    testValues = [2, 3, 4, 5]
    targetValue = 6
    returnValue = function(testValues, targetValue)
    print(returnValue)

if __name__ == '__main__':
    main()


