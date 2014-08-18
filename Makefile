example1:
	gcc -fPIC -c example1.c
	ld -shared -soname libexample1.so.1 -o libexample1.so.1.0 -lc example1.o
