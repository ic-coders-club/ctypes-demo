ctypes-demo
===========

Demonstration of the use of ctypes in the Coders Club meeting on Tuesday 19th 
August 2014.

Links
=====
* [ctypes](https://docs.python.org/2.7/library/ctypes.html#module-ctypes)
* [argparse](https://docs.python.org/2.7/library/argparse.html)

Requirements
============

* this package
* ROOT
* Python version >=2.7 or >=3.2 (for argparse and ctypes)

On the lx-machines, all you need to do is

    git clone git@github.com:ichep-coders-club/ctypes-demo
    source setup.sh

Example 1
=========

(Modified from [this blog post](http://blog.prashanthellina.com/2008/01/07/interfacing-python-with-c-using-ctypes/) )
This is the 'trivial example'

    make example1
    ./example1.py

Example 2
=========

Here some more features are shown:

* argtypes
* restype
* Python3 subtleties
* arrays
* structs


    make example2
    ./example2.py

Example 3
=========

Wrapping ROOT

    make example3
    ./example3.py -h
    ./example3.py --rootfile ~/cpp-mc-tools/nuhm2_140812_mc10.root --plot-name m0_nuhm2_m12_chi2 --outfile test.pdf 
