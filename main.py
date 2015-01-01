# by Stuart


# spesific times are stored as a tuple in 24 hour time e.g. 2:45 pm = (14, 45)
# 8th period = passing period, 9th period = break, 10th period = lunch, 11th period = homeroom

class schedule:
    def __init__(self, p1, p2, p3, p4, p5, p6, p7):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.p8 =  'Passing Period'
        self.p9 =  'Break'
        self.p10 =  'Lunch'
        self.p11 =  'Homeroom'
        self.p12 = 'Activity (if applicable)'

class user:
    def __init__(self, un, pw, sched): # un = username, pw = password, sched = an instance of schedule
        self.un = un
        self.pw = pw
        self.sched = sched

class admin:
    def __init__(self, un, pw):
        self.un = un
        self.pw = pw

class period:
    def __init__(self, periodNum, startingTime, endingTime):
        self.periodNum = periodNum
        self.startingTime = startingTime
        self.endingTime = endingTime

class calender:
    def __init__(self, order): # order = a dict of tuples of periods
        self.order = order

import datetime
import pickle
import generateCalender
import dispUserInfo
import schedChanges
import setup
import login

TYPICALMONDAY = calender([period(1, (8, 15), (9, 5)), period(8, (9, 5), (9, 15)), period(2, (9, 15), (10, 5)), period(9, (10, 5), (10, 15)), period(8, (10, 15), (10, 20)),
                          period(3, (10, 20), (11, 10)), period(8, (11, 10), (11, 20)), period(4, (11, 20), (12, 10)), period(10, (12, 10), (12, 50)), period(8, (12, 50), (12, 55)),
                          period(5, (12, 55), (13, 45)), period(8, (13, 45), (13, 55)), period(6, (13, 55), (14, 45))])

TYPICALTUESDAY = calender([period(1, (8, 15), (9, 5)), period(8, (9, 5), (9, 15)), period(7, (9, 15), (10, 5)), period(9, (10, 5), (10, 15)), period(8, (10, 15), (10, 20)),
                           period(2, (10, 20), (11, 10)), period(8, (11, 10), (11, 20)), period(3, (11, 20), (12, 10)), period(10, (12, 10), (12, 50)), period(8, (12, 50), (12, 55)),
                           period(4, (12, 55), (13, 45)), period(8, (13, 45), (13, 55)), period(5, (13, 55), (14, 45))])

TYPICALWEDNESDAY = calender([period(12, (8, 15), (8, 50)), period(8, (8, 50), (9, 0)), period(11, (9, 0), (9, 15)), period(8, (9, 15), (9, 25)),
                            period(1, (9, 25), (10, 15)), period(9, (10, 15), (10, 25)), period(8, (10, 25), (10, 30)), period(6, (10, 30), (11, 20)), period(8, (11, 20), (11, 30)),
                            period(7, (11, 30), (12, 20)), period(10, (12, 20), (12, 55)), period(8, (12, 55), (13, 0)), period(2, (13, 0), (13, 50)), period(8, (13, 50), (14, 0)),
                            period(3, (14, 0), (14, 50))])

TYPICALTHURSDAY = calender([period(1, (8, 15), (9, 5)), period(8, (9, 5), (9, 15)), period(4, (9, 15), (10, 5)), period(9, (10, 5), (10, 15)), period(8, (10, 15), (10, 20)),
                            period(5, (10, 20), (11, 10)), period(8, (11, 10), (11, 20)), period(4, (11, 20), (12, 10)), period(10, (12, 10), (12, 50)), period(8, (12, 50), (12, 55)),
                            period(7, (12, 55), (13, 45)), period(8, (13, 45), (13, 55)), period(2, (13, 55), (14, 45))])

TYPICALFRIDAY = calender([period(3, (8, 15), (9, 5)), period(8, (9, 5), (9, 15)), period(4, (9, 15), (10, 5)), period(8, (10, 5), (10, 15)),
                          period(5, (10, 15), (11, 5)), period(9, (11, 5), (11, 25)), period(8, (11, 25), (11, 35)), period(6, (11, 30), (12, 20)), period(8, (12, 20), (12, 30)),
                          period(7, (12, 30), (13, 20))])
    
def addNew():
    currentDict = pickle.load(open('userinfo.txt', 'rb'))
    if currentDict == {}: # for now we will assume that the admin will use it first
        isAdmin = 'yes'
    else:
        isAdmin = 'no'
    del currentDict

    setup.setup(isAdmin)

def adminOptions():
    while True:
        print('Do you want to logout (type: "logout") or enter schedualing changes (type: "sc")')
        inpt = input()
        if inpt == 'logout':
            break
        elif inpt == 'sc':
            schedChanges.takeSchedulingChanges()
        else:
            print('Enter valid input')

def main():
    while True:
        print('Do you want to make a new account (type: "new") or login (type: "login"). To exit simply close this window.')
        inpt = input()
        if inpt == 'new':
            addNew()
            print('Your account has been created')
        elif inpt == 'login':
            valid, userType, userName = login.login()
            if valid:
                break
        else:
            print('Enter valid input')

    if userType == 'admin':
        adminOptions()
    elif userType == 'user':
        print('Now displaying information. To exit simply close this window')
        userInfo = pickle.load(open('userinfo.txt', 'rb'))
        dispUserInfo.dispInfo(userInfo[userName])
    else:
        assert "hay una problema"

    
if __name__ == '__main__':
    main()
    
