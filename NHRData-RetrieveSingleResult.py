import ctypes
import sys
import os

def RetrieveNHRData(ProjectPath,DOE2Path,NHRID,Command,ChildCommand,OutputFileName):
	# Load or create outpout file
	Output = open(os.path.dirname(os.path.abspath(__file__))+'\\'+OutputFileName+".csv","a")
	OutputLine = ProjectPath + ','

	DOE2Path = DOE2Path + "\\"
	ProjectPath = os.path.normpath(ProjectPath)
	
	# Load DLL
	D2Result = ctypes.CDLL(os.path.dirname(os.path.abspath(__file__)) +'\D2Result.dll')

	# Retrieve the functions within the DLL
	GetSingleResult =  D2Result['D2R_GetSingleResult']
	LoadNHKData = D2Result['D2R_LoadNHKData']
	GetNumComponents = D2Result['D2R_GetNumComponents']
	GetCompName = D2Result['D2R_GetComponentName']

	# Load NHR Data and count each DOE-2 command defined below
	LoadNHKData(ProjectPath)
	Commands = {'COMPONENT-COST': 2001,
	'UTILITY-RATE': 2005,
	'BLOCK-CHARGE': 2006,
	'RATCHET': 2007,
	'SYSTEM': 2010,
	'ZONE': 2019,
	'EXTERIOR-WALL': 2020,
	'UNDERGROUND-WALL': 2040,
	'INTERIOR-WALL': 2046,
	'WINDOW': 2050,
	'DOOR': 2055,
	'PUMP': 2061,
	'CIRCULATION-LOOP': 2062,
	'CHILLER': 2063,
	'BOILER': 2064,
	'DW-HEATER': 2065,
	'COOLING-TWR': 2066,
	'ELEC-GENERATOR': 2068,
	'THERMAL-STORAGE': 2069,
	'SPACE': 2070,
	'ELEC-METER': 2085,
	'FUEL-METER': 2086,
	'STEAM-METER': 2087,
	'CHW-METER': 2088,
	'MATERIALS-COST': 2091}
	CommandCount = GetNumComponents(Commands[Command],-1)
	if ChildCommand <> "-":
		ChildCommandCount = GetNumComponents(Commands[ChildCommand],-1)
		
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

	pszDOE2Dir = DOE2Path
	pszFileName = ProjectPath
	iEntryID = int(NHRID)
	iMaxValues = 1
	
	for i in range(0,CommandCount):
		pfData = (ctypes.c_float*iMaxValues)()
		# Get the name of the Command
		CompName = ctypes.c_char_p('')
		GetCompName(Commands[Command],-1,i,CompName,33)
		pszReportKey = CompName.value

		if ChildCommand <> "-":
			for j in range(0,ChildCommandCount):
				# Get the name of the ChildCommand
				CompName = ctypes.c_char_p('')
				GetCompName(Commands[ChildCommand],-1,j,CompName,33)
				pszRowKey = CompName.value
				GetSingleResult(pszDOE2Dir,pszFileName,iEntryID,pfData,iMaxValues,pszReportKey,pszRowKey)
				if pfData[0] <> -99999 and pfData[0] <> 0:
					OutputLine = str(OutputLine) + str(pfData[0]) + ","
		else:
			pszRowKey = ''
			# Retrieve and store the data
			GetSingleResult(pszDOE2Dir,pszFileName,iEntryID,pfData,iMaxValues,pszReportKey,pszRowKey)
			OutputLine = str(OutputLine) + str(pfData[0]) + ","
	Output.write(OutputLine+'\n')
	
if __name__ == '__main__':
	RetrieveNHRData(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])	