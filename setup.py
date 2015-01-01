# by Kush (more added in debugging by Stuart)

from main import *
import pickle

def askForPeriod(periodNum):
    print("What class is your period "+periodNum)
    period = input()
    return period

def setup(adminYN):
    
    userInfo = pickle.load(open('userinfo.txt', 'rb'))

    if adminYN == 'yes' or adminYN == 'y':
        print('You are setting up as an administrator')
    
    print("What do you want to be your username")
    username = input()
    print("What do you want to be your password")
    password = input()
    
    if adminYN == "yes" or adminYN == "y":
        userInfo[username] = admin(username, password)

    else:
        period1 = askForPeriod("1")
        period2 = askForPeriod("2")
        period3 = askForPeriod("3")
        period4 = askForPeriod("4")
        period5 = askForPeriod("5")
        period6 = askForPeriod("6")
        period7 = askForPeriod("7")

        userSchedule = schedule(period1, period2, period3, period4, period5, period6, period7)

        userInfo[username] = user(username, password, userSchedule)

    print('Saving...')
    pickle.dump(userInfo, open('userinfo.txt', 'wb'))
