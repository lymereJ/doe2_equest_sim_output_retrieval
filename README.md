# Retrieve non-hourly data from DOE-2 simulation output files using Python

## Description
This repository contains a set of Python scripts that levrage the functions (writen in C++) in D2Result.dll to retrieve non-hourly data from DOE-2 simulation output files.

## Why?
The functions in D2Result.dll allows the user to retrieve exact values out of the DOE-2 simulation output files, unlike the values shown in the *.SIM files.
Using this method it is also possible to create custom output reports for a particular project.

## Important Notes
There are two versions of D2Result.dll, a 32-bits and 64-bits compatible one.

## Example
An example on how to use the script and the dll file is presented in the Example folder of this repository.

## Disclamer
The 32 bits version of D2Result.dll is available through the installation of eQUEST. The D2Result.dll (64-bits) is available through the installation of the [Model Manager](http://www.rmi.org/ModelingTools) developed by the Rocky Mountain Institute.

## Notes
This repository is still being updated, more examples and a more robust set of Python scripts will be committed soon.