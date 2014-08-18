#! /usr/bin/env python
from ctypes import cdll, c_int

l = cdll.LoadLibrary('libexample1.so.1.0')
print(l.add(10, 20))
