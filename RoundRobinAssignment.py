import pandas as pd
import os,datetime

CurrentDir = os.path.dirname(os.path.realpath(__file__))


def InitializeAssignments(): # Load assignments from File
   assignmentsFile = 'AccountAssignments.csv'
   AssignmentsData = pd.read_csv(os.path.join(CurrentDir,assignmentsFile),encoding='latin-1')
   return pd.DataFrame(AssignmentsData)


AssignmentsDF = InitializeAssignments() 

def RoundRobinAssignment(ReasonLost): 
    LowestAssignment = AssignmentsDF[ReasonLost].idxmin()
    AssignmentsDF[ReasonLost][LowestAssignment] += 1
    NewOwner = AssignmentsDF['USER ID'][LowestAssignment]
    return NewOwner


sourcefile = "LeadDistroCopy.csv" #This has to change



LeadsData = pd.read_csv(os.path.join(CurrentDir,sourcefile),keep_default_na = False ,encoding='latin-1')

LeadsDF = pd.DataFrame(LeadsData)
try:
    for i in LeadsDF.index:
        if(LeadsDF['NEW OWNER ID'][i] == "Available"):
            LeadsDF['NEW OWNER ID'][i] = RoundRobinAssignment(LeadsDF['Reason Lost'][i])

except:

    print(LeadsDF.loc[[i]])



LeadFinalFile = "LeadPoolDistroUpdated.csv"
     
while(os.path.exists(os.path.join(CurrentDir,LeadFinalFile))): 
     LeadFinalFile = input("%s already exists! New Name: " %LeadFinalFile) + '.csv'

LeadsDF.to_csv(os.path.join(CurrentDir,LeadFinalFile), index = False)

print("Success")

AssignmentsDF.to_csv(os.path.join(CurrentDir,"ResultsFinish.csv"), index = False)