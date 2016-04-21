import ctypes

# Load DLL
D2Result = ctypes.CDLL('D2Result.dll')

# Retrieve the functions within the DLL
GetSingleResult =  D2Result['D2R_GetSingleResult']
GetMultipleResults = D2Result['D2R_GetMultipleResult']

#
# 	Get Single Results 
#	Arguments
#
#	pszDOE2Dir: path to DOE-2 directory
#	pszFileName: path to project (do not include any extension)
#	iEntryID: id from NHRList.txt corresponding to the value to retrieve
#	pfData: sample array to store the retrieved value
#	iMaxValues: number of items to retrieve (NI in NHRList.txt); should always be 1 when GetSingleResult is called
#	pszReportKey: to use when NI > 0 and when value to retrieve refers to a particular BDL component; '\0' if not valid
#	pszRowKey: to use when KT > 0 and when a report has multiple row; '\0' if not valid
#

pszDOE2Dir = 
pszFileName = 
iEntryID = 
iMaxValues = 
pfData = (ctypes.c_float*iMaxValues)()
pszReportKey = 
pszRowKey = 

#
# 	Get Multiple Result
#	Arguments
#
#	pszDOE2Dir: path to DOE-2 directory
#	pszFileName: path to project (do not include any extension)
#	iFileType: 0 for Loads results, 1 for HVAC, 2 for Utility Rate; in general first digit of NHRlist ID minus 1
#	pfData: sample array to store the retrieved value
#	iMaxValues: number of items to retrieve (NI in NHRList.txt); should always be 1 when GetSingleResult is called
#	iNumMRTs: number of values in one set of results
#	pMRTs: number of set of results to retrieve (max=12)
#

pszDOE2Dir = 
pszFileName = 
iFileType =
iMaxValues = 
pfData = (ctypes.c_float*iMaxValues)()
iNumMRTs = 

# Define a 'Structue' that contains information about the data to retrieve

class MRTarray(ctypes.Structure):
    _fields_ = [("iEntryID", ctypes.c_int),
                ("iReturnValue", ctypes.c_int),
                ("pszReportKey", ctypes.c_char * 34 ),
				("pszRowKey",ctypes.c_char * 34)]
 

MRT = MRTarray()
MRTS = (MRTarray * iNumMRTs)()

# Below, i is an index from 0 to iNumMRTs

MRTS[i].iEntryID =
MRTS[i].pszReportKey =
MRTS[i].pszRowKey = 

pMRTs = MRTS

# Retrieve and print the data
GetSingleResult(pszDOE2Dir,pszFileName,iEntryID,pfData,iMaxValues,pszReportKey,pszRowKey)
print "GetSingleResult:"
print pfData[0]

GetMultipleResults(pszDOE2Dir,pszFileName,iFileType,pfData,iMaxValues,iNumMRTs,pMRTs)
print "GetMultipleResults:"
for i in range(0,len(pfData)):
	 print pfData[i]
