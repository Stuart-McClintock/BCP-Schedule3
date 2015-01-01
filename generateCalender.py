# by Stuart

def listToStr(ls):
    rList =  ''
    for i in ls:
        rList += i
    return rList

def generate():
    calender = 'calender(['
    
    while True:
        print('to end type "END" now, otherwise hit return')
        if input() == 'END':
            break
        while True:
            print('enter the period number')
            pNum = input()
            try:
                pNum = int(pNum)
                break
            except:
                print('Enter a valid number')

        while True:
            print('enter the starting time (hh:mm) in 24 hour time ')
            sTime = input()
            try:
                if int(sTime[0:2])<=24 and int(sTime[0:2])>=0 and int(sTime[3:5])<60 and int(sTime[3:5])>=0:
                    sHours = int(sTime[0:2])
                    sMins = int(sTime[3:5])
                    break
                else:
                    assert "Hay un problema"
            except:
                print('enter a valid time')

        while True:
            print('enter the ending time (hh:mm) in 24 hour time ')
            eTime = input()
            try:
                if int(eTime[0:2])<=24 and int(eTime[0:2])>=0 and int(eTime[3:5])<60 and int(eTime[3:5])>=0:
                    eHours = int(eTime[0:2])
                    eMins = int(eTime[3:5])
                    break
                else:
                    assert "Hay un problema"
            except:
                print('enter a valid time')

        calender += 'period('+str(pNum)+', ('+str(sHours)+', '+str(sMins)+'), ('+str(eHours)+', '+str(eMins)+')), '

    calender = list(calender)
    calender.pop()
    calender.pop()
    calender = listToStr(calender)
    calender += '])'
    return calender

if __name__ == '__main__':
    generate()
