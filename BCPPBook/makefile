test: test.o time.o 
	g++ -Wall -std=c++17 -g -o test test.o time.o

test.o: test.cpp test.h time.h
	g++ -Wno-unused-but-set-variable -Wno-unused-local-typedefs -Wno-unused-variable -Wall -std=c++17 -g -c test.cpp

time.o: time.cpp time.h
	g++ -Wall -std=c++17 -g -c time.cpp

hexdump: hexdump.o
	g++ -Wall -std=c++17 -g -o hexdump hexdump.o

hexdump.o: hexdump.cpp
	g++ -Wall -std=c++17 -g -c hexdump.cpp

