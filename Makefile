example1:
	gcc -fPIC -c example1.c
	gcc -g -shared -Wl,-soname,libexample1.so -o libexample1.so example1.o

example2:
	g++ -fPIC -c example2.cpp
	g++ -g -shared -Wl,-soname,libexample2.so -o libexample2.so example2.o

example3:
	g++ -fPIC -c example3.cpp $(shell root-config --cflags --libs)
	g++ -g -shared -Wl,-soname,libexample3.so -o libexample3.so example3.o \
		$(shell root-config --cflags --libs)

clean:
	rm *.o *.so
