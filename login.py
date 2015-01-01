# by Kush, modified by Stuart during debuging

from main import *

NUMATTEMPTS = 2
typeAdmin = type(admin('x', 'y'))

def askForInfo(info):
    print("What is your "+info)
    rVal = input()
    return rVal

def checkIfInDict(var, dictionary):
    if var in dictionary.keys():
        return True
    else:
        return False
def compareVals(var, val):
    if var == val:
        return True
    else:
        return False

def login():

    userInfo = pickle.load(open('userinfo.txt', 'rb'))

    isInDict = False
    while isInDict == False:
        userUsername = askForInfo("username")
        isInDict = checkIfInDict(userUsername, userInfo)
        
    password = askForInfo("password")

    isCorrect = compareVals(password, userInfo[userUsername].pw)

    remainingAttempts = NUMATTEMPTS
    while isCorrect == False and remainingAttempts>0:
        password = askForInfo("password")       
        isCorrect = compareVals(password, userInfo[userUsername].pw)
        remainingAttempts -= 1

    if isCorrect==True and type(userInfo[userUsername]) == typeAdmin:
        print("HI ADMIN")
        return True, 'admin', userUsername
        
    elif isCorrect == True:
        print("HI USER")
        return True, 'user', userUsername
    else:
        print("INVALID")
        return False, None, None
