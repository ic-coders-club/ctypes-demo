#! /usr/bin/env python
from ctypes import cdll, c_int

#modified from http://blog.prashanthellina.com/2008/01/07/interfacing-python-with-c-using-ctypes/

# load the shared object
libexample1 = cdll.LoadLibrary('libexample1.so.1.0')

# call the function, yes it is as simple as that!
print(libexample1.add(10, 20))

