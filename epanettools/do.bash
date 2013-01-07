#!/bin/bash
swig -python    epanet2.h
gcc -c -fPIC *.c -I/usr/include/python2.7
ld -shared *.o -o _epanettools.so 
