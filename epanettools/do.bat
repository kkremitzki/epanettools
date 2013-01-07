rem do.bat
rem "c:\Program Files (x86)\CodeBlocks\MinGW\mingwvars.bat"
del *.pyd
del epanet2.py
c:\swigwin-2.0.4\swigwin-2.0.4\swig.exe -python epanet2.h
gcc -c *.c -Ic:\python26\include
gcc -shared *.o -o _epanet2.pyd  -Lc:\Python26 -lpython26
sleep 2
copy *epanet2.py* c:\Python26\Lib\site-packages\