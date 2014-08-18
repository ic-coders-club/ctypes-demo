#! /usr/bin/env python2
from ctypes import cdll, c_double, c_int, c_char_p, byref, Structure


l = cdll.LoadLibrary('libexample2.so')
#calling with doubles will go wrong
#print(l.add_doubles(1.5, 1.5))

#don't forget to specify the return type
print(l.add_doubles(c_double(1.5), c_double(1.5)))
l.add_doubles.restype = c_double
print(l.add_doubles(c_double(1.5), c_double(1.5)))

#you can also set the argument type
l.add_doubles.argtypes = [c_double, c_double]
print(l.add_doubles(2.5, 1))

#caveat: in python3 you need to encode the string 
l.cout_string('hello')
l.cout_string(b'hello')
l.cout_string('hello'.encode('ascii'))
l.argtypes = [c_char_p]
l.cout_string('hello')

#use an array
n = 11
array_of_n_doubles = c_double*n
my_array = array_of_n_doubles()
for i in range(n):
    my_array[i] = 1.0
l.sum_doubles.restype = c_double
print(l.sum_doubles(my_array, n))

#or alternatively, something like
#def sum_doubles(array):
#    n = len(array)
#    c_double_array = (c_double*n)(*array)
#    l.sum_doubles.restype = c_double
#    return l.sum_doubles(c_double_array, n)
#
#print(sum_doubles([2.1, 3.2, 4.3]))

#structs
class MyStructure(Structure):
    _fields_ = [('a', c_int), ('b', c_double)]

my_struct = MyStructure()
l.fill_my_struct(4, c_double(4.5), byref(my_struct))
print(my_struct.a, my_struct.b)
