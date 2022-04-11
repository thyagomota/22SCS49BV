#!/bin/zsh
echo Building oauthecho...
rm -rf build 
mkdir build 
mkdir build/python
mkdir build/python/lib
mkdir build/python/lib/python3.8
mkdir build/python/lib/python3.8/site-packages
cp src/controller.py build/python/lib/python3.8/site-packages 
cd build 
zip -r oauthecho.zip .
cd ..
echo done!