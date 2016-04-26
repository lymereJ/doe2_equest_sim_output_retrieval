# Retrieve non-hourly data from DOE-2 simulation output files using Python

## Description
This repository contains a set of Python scripts that levrage the functions (writen in C++) in D2Result.dll to retrieve non-hourly data from [DOE-2/eQUEST](http://www.doe2.com/) simulation output files.

## Why?
The functions in D2Result.dll allows the user to retrieve exact values out of the DOE-2/eQUEST simulation output files, unlike the values shown in the *.SIM files.
Using this method it is also possible to create custom output reports.

## Important Notes
There are two versions of D2Result.dll, a 32-bits and 64-bits compatible one.

## Scripts
- `NHRData-Retrieval.py` is a 'skeleton' that can be use to create custom Python functions to retrieve non-hourly data using both the D2R_GetSingleResult and D2R_GetMultipleResult functions included in the D2Result.dll file
- NHRData-RetrieveSingleResult.py is a fully functionning Python module that contains a function that allows the user to retrieve single non-hourly data from the simulation output files. The function uses other functions contained in D2Result.dll (D2R_LoadNHKData (load the non-hourly data in memory), D2R_GetNumComponents (retrieve the number of items corresponding to a particular DOE-2 command, ex: how many SYSTEM?) and D2R_GetComponentName (retrieve the name of a particular item corresponding to a particular command, ex: name of the first SYSTEM in the mode)). The function can be called via basic command line as long as the right arguments are passed to it. This makes the function versatile and able to be used in conjonction with other scripts or other programs. For example, the NHRData-RetrieveSingleResult.py script can be used with the RetrieveNHRData.xlsm workbook to create batch runs to harvest a large number of information from a large number of model at once.

## Example
An example showing how to use the basic script (NHRData-Retrieval.py) is presented in the Example folder of this repository. This example shows how to use both the D2R_GetSingleResult and D2R_GetMultipleResult functions.

## Disclamer
The 32 bits version of D2Result.dll is available through the installation of [eQUEST](http://www.doe2.com/equest/). The D2Result.dll (64-bits) is available through the installation of the [Model Manager](http://www.rmi.org/ModelingTools) developed by the Rocky Mountain Institute.

## Notes
This repository is still being updated, more examples and a more robust set of Python scripts will be committed soon.