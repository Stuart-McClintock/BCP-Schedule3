# by Stuart

import pickle
import datetime
import main

def isChangeNeeded(currentDate, anomalies):
    try:
        anomalies[currentDate]
        return True
    except:
        return False

def numMinutes(time):
    rVal = time[0]*60
    rVal += time[1]
    return rVal

def hasSchoolStarted(time, schedule):
    '''Determines is school has started that day(is still true even after it ends)'''
    try:
        if numMinutes(time) >= numMinutes(schedule.order[0].startingTime):
            return True
        else:
            return False
    except:
        return False

def minVsMins(numMins):
    if numMins == 1:
        return 'minute'
    else:
        return 'minutes'

def findCurrentDate():
    today = datetime.date.today()
    currentDay = today.day
    currentMonth = today.month
    currentYear = int(str(today.year)[2:4])
    currentDate = (currentDay, currentMonth, currentYear)
    return currentDate

def findCurrentSchedule():
    currentDate = findCurrentDate()
    dayOfWeek = datetime.date.today().weekday()

    anomalies = pickle.load(open('schedChanges.txt', 'rb'))

    if isChangeNeeded(currentDate, anomalies):
        todaysSchedule = anomalies[currentDate]
    elif dayOfWeek == 0:
        todaysSchedule = main.TYPICALMONDAY
    elif dayOfWeek == 1:
        todaysSchedule = main.TYPICALTUESDAY
    elif dayOfWeek == 2:
        todaysSchedule = main.TYPICALWEDNESDAY
    elif dayOfWeek == 3:
        todaysSchedule = main.TYPICALTHURSDAY
    elif dayOfWeek == 4:
        todaysSchedule = main.TYPICALFRIDAY
    else:
        todaysSchedule = []

    return todaysSchedule, currentDate

def isTimeBetween(time, beginningTime, endingTime):
    timeMins = numMinutes(time)
    beginningTimeMins = numMinutes(beginningTime)
    endingTimeMins = numMinutes(endingTime)
    if timeMins >= beginningTimeMins and timeMins < endingTimeMins:
        return True
    else:
        return False

def timeDifference(time1, time2): # There is most likley something really bad about this function
    minsDifference = ((time1[0]-time2[0])*60)+(time1[1]-time2[1])
    return abs(minsDifference)

def tupTimeToStr(time):
    ending = ''
    rString = ''
    if time[0] < 13:
        rString += str(time[0])
        ending = 'am'
    else:
        rString += str(time[0]-12)
        ending = 'pm'
    rString += ':'
    if time[1] >= 10:
        mins = str(time[1])
    else:
        mins = '0'+str(time[1])
    rString += mins
    rString += (' '+ending)
    return rString

def dispInfo(currentUser):
    todaysSchedule, currentDate = findCurrentSchedule()
    hasStarted = False
    while True:
        if currentDate != findCurrentDate():
            todaysSchedule, currentDate = findCurrentSchedule()
            hasStarted = False

        if todaysSchedule.order == []:
            print('There is no school today')
            print('Press return to refresh')
            input()
            continue
        
        time = datetime.datetime.now()
        currentHour = time.hour
        currentMinute = time.minute
        currentTime = (currentHour, currentMinute)
        justWent = False
        justJustWent = False
        notGoing = True
        for i in todaysSchedule.order:
            if justJustWent:
                periodNumber = i.periodNum
                nextNextClass = eval('currentUser.sched.p'+str(periodNumber))
                nextNextEndingTime = i.endingTime
                justJustWent = False
            elif justWent:
                periodNumber = i.periodNum
                nextClass = eval('currentUser.sched.p'+str(periodNumber))
                nextEndingTime = i.endingTime
                justWent = False
                justJustWent = True
            elif isTimeBetween(currentTime, i.startingTime, i.endingTime):
                notGoing = False
                periodNumber = i.periodNum
                currentClass = eval('currentUser.sched.p'+str(periodNumber))
                justWent = True
                thisEndingTime = i.endingTime
        
        if notGoing  and len(todaysSchedule.order) > 0:
            if not hasSchoolStarted(currentTime, todaysSchedule):
                periodNumber = todaysSchedule.order[0].periodNum
                st = todaysSchedule.order[0].startingTime
                firstClass = eval('currentUser.sched.p'+str(periodNumber))
                print('School has not started yet, your first class is '+str(firstClass)+' in '+str(timeDifference(st, currentTime))+' minutes at '+tupTimeToStr(st))
            else:
                print('School is over for today')

        if not notGoing:
            timeDif = timeDifference(thisEndingTime, currentTime)
            print('Currently you have '+currentClass+', it ends in '+str(timeDif)+' '+minVsMins(timeDif)+' at '+tupTimeToStr(thisEndingTime))
            try:
                timeDif = timeDifference(nextEndingTime, currentTime)
                print('After that you have '+nextClass+', it ends in '+str(timeDif)+' '+minVsMins(timeDif)+' at '+tupTimeToStr(nextEndingTime))
                try:
                    timeDif = timeDifference(nextNextEndingTime, currentTime)
                    print('After that you have '+nextNextClass+', it ends in '+str(timeDif)+' '+minVsMins(timeDif)+' at '+tupTimeToStr(nextNextEndingTime))
                except:
                    pass
            except:
                pass

        print('Press return to refresh')
        input()
