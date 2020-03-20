from faker import Faker
import os
import random
import pandas as pd


CurrentDir = os.path.dirname(os.path.realpath(__file__))

def CreateFakeInformation(fake,AccountsCSV):
    AccountData = pd.read_csv(os.path.join(CurrentDir,AccountsCSV),encoding='latin-1')
    AccountDF = pd.DataFrame(AccountData)

    DataColumns = ['Phone','Email','Bank Account Number','Federal Tax ID#','Social Security Number']


    for i in AccountDF.index:
        FakeInfo = [fake.phone_number(),fake.email(),random.randint(100000,9999999),random.randint(100000,9999999),random.randint(100000,9999999)]
        for j in range(0,len(DataColumns)):
            AccountDF[DataColumns[j]][i] = FakeInfo[j]
    
    FakeAccountsFinalFile = "FakeInfoAccounts.csv"
     
    while(os.path.exists(os.path.join(CurrentDir,FakeAccountsFinalFile))): 
        FakeAccountsFinalFile = input("%s already exists! New Name: " %FakeAccountsFinalFile) + '.csv'

    AccountDF.to_csv(os.path.join(CurrentDir,FakeAccountsFinalFile), index = False)

    print("Success")



AccountsCSV = input("Accounts Data file : ")
fake = Faker('en_US')
CreateFakeInformation(fake,AccountsCSV)