import sys

def function(test):
    test = test + 1
    return test

def main():
    print 'Hello there', sys.argv[1]
    output = function(5)
    print output


if __name__ == '__main__':
    main()


