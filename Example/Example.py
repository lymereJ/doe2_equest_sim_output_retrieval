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
#	pszReportKey: to use when NI > 0 and when value to retrieve refers to a particular BDL component
#	pszRowKey: to use when KT > 0 and when a report has multiple row
#

pszDOE2Dir = 'C:\\DOE-2\\'
pszFileName = 'Test'
iEntryID = 2001001
pfData = (ctypes.c_float*1)()
iMaxValues = 1
pszReportKey = "\0"
pszRowKey = "\0"

#
# 	Get Multiple Result
#	Arguments
#
#	pszDOE2Dir: path to DOE-2 directory
#	pszFileName: path to project (do not include any extension)
#	iFileType: 0 for Loads results, 1 for HVAC, 2 for Utility Rate; in general first digit of NHRlist ID minus 1
#	pfData: sample array to store the retrieved value
#	iMaxValues: number of items to retrieve (NI in NHRList.txt); should always be 1 when GetSingleResult is called
#	iNumMRTs: 
#	pMRTs: 
#

#pszDOE2Dir = 'C:\\DOE-2\\'
#pszFileName = 'Test'
iFileType = 1
pfData = (ctypes.c_float*13)()
iMaxValues = 13
iNumMRTs = 1

class MRTarray(ctypes.Structure):
    _fields_ = [("iEntryID", ctypes.c_int),
                ("iReturnValue", ctypes.c_int),
                ("pszReportKey", ctypes.c_char * 34 ),
				("pszRowKey",ctypes.c_char * 34)]
 

MRT = MRTarray()
MRTS = (MRTarray * iNumMRTs)()

MRTS[0].iEntryID = 2309007
MRTS[0].pszReportKey = "EM1"
MRTS[0].pszRowKey = "\0"

pMRTs = MRTS

#Retrieve and print the data
GetSingleResult(pszDOE2Dir,pszFileName,iEntryID,pfData,iMaxValues,pszReportKey,pszRowKey)
print "GetSingleResult:"
print pfData[0]

GetMultipleResults(pszDOE2Dir,pszFileName,iFileType,pfData,iMaxValues,iNumMRTs,pMRTs)
print "GetMultipleResults:"
for i in range(0,len(pfData)):
	 print pfData[i]
