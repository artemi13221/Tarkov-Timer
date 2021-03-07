import json
import datetime
import os
import threading
import time
#from win10toast import ToastNotifier

hideout = ["tmp", "WorkBench", "MedStation", "Lavatory", "Scav Case", "Booze Generator", "Water Collector", "Nutrition Unit", "Intelligence Center"]

isAlarm = True
mainTmp = -1
hideoutTmp = -1
traderTmp = -1
optionTmp = -1
skillLevel = 1


maker = []
userDataSave = []
userDataSave.append(maker)
userDataSave.append(skillLevel)

def getNowTime():
    now_time = datetime.datetime.now()
    
    return now_time

def toastAlarm():
    while True:
        for i in range(len(maker)):
            if(getNowTime() > maker[i]):
                maker[i] = datetime.datetime(2099, 12, 31, 0, 0, 0)
                saveJsonData()
                #toaster = ToastNotifier()
                #toaster.show_toast(f'{Hideout[i]} is done!!', duration=10)

                print(f'{hideout[i]} is done!!')

        time.sleep(5)

def saveJsonData():
    f = open('save.json', 'w')
    json_data = {}
    time_tmp = []
    for i in maker:
        time_tmp.append(i.strftime('%Y-%m-%d-%H-%M-%S'))
    
    json_data['time'] = time_tmp
    json_data['level'] = skillLevel

    json.dump(json_data, f)
    f.close()

def loadUserData():
    if(os.path.exists('save.json')):
        f = open('save.json', 'r')
        data_tmp = f.read()

        if(data_tmp != ''):
            json_data = json.loads(data_tmp)

            skillLevel = json_data['level']
            loadJsonData(json_data['time'])
            
        f.close()
    else:
        f = open('save.json', 'w')
        f.close()

def loadJsonData(data_tmp):
    global maker

    j = 0
    for i in data_tmp:
        maker_tmp = list(map(int,i.split('-')))
        maker[j] = datetime.datetime(maker_tmp[0], maker_tmp[1], maker_tmp[2], maker_tmp[3], maker_tmp[4], maker_tmp[5])
        j = j + 1

def initStartProgram(): 
    global maker

    for _ in range(9):
        maker.append(datetime.datetime(2099, 12, 31, 0, 0, 0))
    
    loadUserData()
    t = threading.Thread(target=toastAlarm)
    t.start()

def skillTimeSet(time):
    decresedTimePersent = skillLevel * 0.75

    return time - (time * (decresedTimePersent / 100.0))

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
            inputNum = -1
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
    global skillLevel
    
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
            if(skillLevel > 51 or skillLevel < 1):
                print("Error! - Please input the correct number.")
                skillLevel = 0
            else: 
                print("Success!")
                saveJsonData()
        else:
            print("Error! - Please input the correct number.")
        
        return 1

def funHideout(inputNum):
    global maker

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

    maker[inputNum] = getNowTime() + datetime.timedelta(minutes=skillTimeSet(craftingTime))

    saveJsonData()
    
###
# Main #
###

initStartProgram()
while(True):
    mainTmp = funMain(mainTmp)
    if(mainTmp == 0):
        os._exit(0)