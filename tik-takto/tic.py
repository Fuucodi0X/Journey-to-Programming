# Creating input varibales
inputVars = [0,0,0,0,0,0,0,0,0]
for i in range(9):
    inputVars[i] = {"value":" ", "selectionStatus":False}
    inputVars[i]["value"] = i + 1

# Building the UI component
def UI():
    print(f" {inputVars[0]["value"]} | {inputVars[1]["value"]} | {inputVars[2]["value"]}")
    print( "--- --- ---")
    print(f" {inputVars[3]["value"]} | {inputVars[4]["value"]} | {inputVars[5]["value"]}")
    print( "--- --- ---")
    print(f" {inputVars[6]["value"]} | {inputVars[7]["value"]} | {inputVars[8]["value"]}")

# Input checker
def check(arr):
    if len(arr) != 2:
        print("Input MUST be 2 values, and DON'T forget to separate them by SPACE")
    else:
        counter = 0
        checkStatus = 0
        if not(arr[0].isdigit()):
            print(f"Error first input must be a number")
            checkStatus += 1
        else:
            if not(1<= int(arr[0]) <= 9):
                print(f"Ur first inputs should be from 1-9")
                checkStatus += 1

        X_O = ["x","X","o","O"]
        counter = 0
        for x_o in X_O:
            if arr[1] != x_o:
                counter += 1
                if counter == len(X_O):
                    print(f"Ur moves are {X_O}")
                    checkStatus += 1
        
        if checkStatus > 0:
            return True
        else:
            return False

# Place selection and X/O insertion
def selectionCheck(pos):
    if inputVars[pos]["selectionStatus"] == True:
        return True
    else:
        return False

def draw (arr):
    # Determining the position
    pos = int(arr[0]) - 1

    # Checking selection
    if selectionCheck(pos):
        print("Already selected choose other position")
    else:
        inputVars[pos]["value"] = arr[1]
        inputVars[pos]["selectionStatus"] = True

# Logic of the game
def checkWin (inputVar, checksign):
    a = inputVar[0]['value'] == inputVar[1]['value'] == inputVar[2]['value'] == checksign
    b = inputVar[3]['value'] == inputVar[4]['value'] == inputVar[5]['value'] == checksign
    c = inputVar[6]['value'] == inputVar[7]['value'] == inputVar[8]['value'] == checksign
    d = inputVar[6]['value'] == inputVar[3]['value'] == inputVar[6]['value'] == checksign
    e = inputVar[1]['value'] == inputVar[4]['value'] == inputVar[7]['value'] == checksign
    f = inputVar[2]['value'] == inputVar[5]['value'] == inputVar[8]['value'] == checksign
    g = inputVar[0]['value'] == inputVar[4]['value'] == inputVar[8]['value'] == checksign
    h = inputVar[2]['value'] == inputVar[4]['value'] == inputVar[6]['value'] == checksign
    abc = a or b or c or d or e or f or g or h
    return abc

def checkDraw(inputVar):
    counter = 0
    for i in range(9):
        if inputVar[i]['selectionStatus'] == True:
            counter += 1
        elif counter == 9:
            return True
        else:
            return False

def logic (inputVar):
    if checkWin(inputVar,"x"):
        print("X won!!")
        gameOver = True
        return gameOver
    elif checkWin(inputVar,"o"):
        print("O won!!")
        gameOver = True
        return gameOver
    elif checkDraw(inputVar):
        print("Draw!!!")
        gameOver = True
        return gameOver
    else:
        return False

# Game loop
gameOver = False
while not gameOver:
    UI()
    playerMove = input("Input > ").split()
    inputError = check(playerMove)
    if inputError == False:
        draw(playerMove)
        gameOver = logic(inputVars)
        continue
    print("Error occured!")