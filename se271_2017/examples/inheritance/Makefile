CC=g++
CXX=g++
CXXFLAGS=-std=c++14 -pedantic-errors -Wall -g

all: main_original main_virtual

main_original: main_original.o
	$(CXX) $(CXXFLAGS) -o main_original main_original.o

main_virtual: main_virtual.o
	$(CXX) $(CXXFLAGS) -o main_virtual main_virtual.o

%.o : %.cpp
	$(CXX) -c $(CXXFLAGS) $< -o $@

clean:
	rm *.o main_original
