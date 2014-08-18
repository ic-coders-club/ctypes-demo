#! /usr/bin/env python2
from ctypes import cdll, c_int

# the trivial example
l = cdll.LoadLibrary('libexample1.so')
print(l.add(10, 20))
