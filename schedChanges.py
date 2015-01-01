# by Stuart

from main import *
import pickle
import datetime
import generateCalender

def takeSchedulingChanges():
    while True:
        print('In what year is the change you want to make (last 2 digits only)')
        yr = input()
        try:
            yr = int(yr)
            if yr < 0 or yr >=100:
               print('Enter the last two digits of the year in which you would like to make a scheduling change to')
            else:
                break
        except:
            print('Enter a valid number')
    
    while True:
        print('In what month is the change you want to make (e.g. november = 11)')
        mth = input()
        try:
            mth = int(mth)
            if mth < 1 or mth >12:
               print('Enter the month in which you would like to make a scheduling change to')
            else:
                break
        except:
            print('Enter a valid number')

    while True:
        print('In what day would you like to appy the change to')
        day = input()
        try:
            day = int(day)
            if day < 1 or day > 31:
               print('Enter the day in which you would like to make a scheduling change to')
            else:
                break
        except:
            print('Enter a valid number')

    dayForChange = (day, mth, yr)
    newSchedule = eval(generateCalender.generate())
    currentDict = pickle.load(open('schedChanges.txt', 'rb'))

    newDict = currentDict
    newDict[dayForChange] = newSchedule
    
    pickle.dump(newDict, open('schedChanges.txt', 'wb'))
