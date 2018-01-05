test: test.o time.o
	g++ -Wall -std=c++17 -g -o test test.o time.o

test.o: test.cpp test.h time.h
	g++ -Wall -std=c++17 -g -c test.cpp

time.o: time.cpp time.h
	g++ -Wall -std=c++17 -g -c time.cpp
