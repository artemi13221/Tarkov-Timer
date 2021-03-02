import json
import datetime
import os

isAlarm = True
mainTmp = -1
hideoutTmp = -1
traderTmp = -1
optionTmp = -1
skillLevel = 0

maker = []

def saveJsonTime():
    f = open('time.json', 'w')
    json.dump(maker, f)
    f.close()

def initStartProgram(): 
    for _ in range(9):
        maker.append(datetime.datetime.today())
    
    if(os.path.exists('time.json')):
        f = open('time.json', 'r')
        temp = json.load(f)

        if(temp == '') :
            pass
        else :
            maker = temp

        f.close()
    else:
        f = open('time.json', 'w')
        f.close()
    
    
def printMain():
    print("Welcome to Tarkov Timer. Select number \n\
============================================= \n\
1. Hideout \n\
2. Traders \n\
3. Options \n\
4. Github \n\
\n\
0. Exit")

def printHideout():
    print("Select hideout \n\
1. WorkBench \n\
2. Medstation \n\
3. Lavatory \n\
4. Scav Case \n\
5. Booze Generator \n\
6. Water Collector \n\
7. Nutrition Unit \n\
8. Intelligence Center \n\
\n\
0. Go Main")

def printTraders():
    print("Select traders \n\
1. Prapor \n\
2. Therapist \n\
3. Skier \n\
4. Peacekeeper \n\
5. Mechanic \n\
6. Ragman \n\
7. Jaeger \n\
\n\
0. Go Main")

def printOption():
    print("Select Options \n\
1. Alarm \n\
2. Skill Level \n\
\n\
0. Go Main")

def getInputNumber():
    strTmp = input('Input : ')
    if(strTmp.isdigit()):
        tmp = int(strTmp)
        return tmp
    else:
        print('Error! - Please input the correct number.')
        return -1

def funMain(inputNum):
    if(inputNum == -1):
        printMain()
        inputNum = getInputNumber()
    elif(inputNum == 0):
        return 0
    elif(inputNum == 1):
        printHideout()
        hideoutTmp = getInputNumber()
        if(hideoutTmp == 0):
            inputNum = -1
        else:
            funHideout(hideoutTmp)
    elif(inputNum == 2):
        printTraders()
        traderTmp = getInputNumber()
        if(traderTmp == 0):
            inputNum = -1
        else:
            funTrader(traderTmp)
    elif(inputNum == 3):
        printOption()
        optionTmp = getInputNumber()
        if(optionTmp == 0):
            optionTmp = -1
        else:
            funOption(optionTmp)
    elif(inputNum == 4):
        print("Github 주소")
        inputnum = -1
    else:
        print("Error! - Please input the correct number.")
        return -1
    
    return inputNum

def funTrader(inputNum):
    print("아직 미구현 기능입니다. 다음에 이용해주세요. 감사합니다. \n")
    return 0

def funOption(inputNum):
    global isAlarm
    
    if(inputNum == 0):
        return 0
        
    elif(inputNum == 1):
        isAlarm = not isAlarm
        print('Start Alarm' if isAlarm else 'End Alarm')
        
        return 1

    elif(inputNum == 2):
        print("Input Crafting skill level")
        strTmp = input("Input : ")
        if(strTmp.isdigit()):
            skillLevel = int(strTmp)
            if(skillLevel > 51 or skillLevel < 0):
                print("Error! - Please input the correct number.")
                skillLevel = 0
            else: 
                print("Success!")
        else:
            print("Error! - Please input the correct number.")
        
        return 1

def funHideout(inputNum):
    f = open('data.json', 'r')
    temp = json.load(f)
    f.close()

    makingKeys = list(temp.keys())
    makingValues = list(temp[makingKeys[inputNum - 1]].keys())

    print('Select a item.')
    j = 1
    for i in makingValues:
        print(f'{j}. {i}')
        j = j + 1
    
    inputSecondNum = getInputNumber()

    craftingTime = temp[makingKeys[inputNum - 1]][makingValues[inputSecondNum - 1]]

    maker[inputNum] = datetime.datetime.now() + datetime.timedelta(minutes=craftingTime)

    saveJsonTime()
    
###
# Main #
###

initStartProgram()
while(True):
    mainTmp = funMain(mainTmp)
    if(mainTmp == 0):
        break