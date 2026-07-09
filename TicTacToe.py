import random
#Tic Tac Toe Game 
print("Welcome to AS.Developer's \n Tic Tac Toe Game \n")
symbolP1= "X"
symbolP2= "O"

gameMatrix=[
[" "," "," "],
[" "," "," "],
[" "," "," "],
]

validVals= (1,2,3)

def matrixChecker(matrix):
    
    WinTest=[]
    # Row Test
    if  matrix[0][0]!= " " and  matrix[0][0]== matrix[0][1]and  matrix[0][1]==  matrix[0][2]: 
        WinTest.append(True)
    if  matrix[1][0]!= " " and  matrix[1][0]== matrix[1][1]and  matrix[1][1]==  matrix[1][2]: 
        WinTest.append(True)
    if  matrix[2][0]!= " " and  matrix[2][0]== matrix[2][1]and  matrix[2][1]==  matrix[2][2]:
        WinTest.append(True)
    
    # Column Test
    if  matrix[0][0]!= " " and  matrix[0][0]== matrix[1][0]and  matrix[1][0]==  matrix[2][0]: 
        WinTest.append(True)
    if  matrix[0][1]!= " " and  matrix[0][1]== matrix[1][1]and  matrix[1][1]==  matrix[2][1]: 
        WinTest.append(True)
    if  matrix[0][2]!= " " and  matrix[0][2]== matrix[1][2]and  matrix[1][2]==  matrix[2][2]: 
        WinTest.append(True)
    
    # Diagonal Test
    if  matrix[0][0]!= " " and  matrix[0][0]== matrix[1][1]and  matrix[1][1]==  matrix[2][2]: 
        WinTest.append(True)
    if  matrix[2][0]!= " " and  matrix[2][0]== matrix[1][1]and  matrix[1][1]==  matrix[0][2]: 
        WinTest.append(True)
    return(WinTest)

def rowInpValFunc():
    
    try:
        rowInp= int(input("Type the row value : "))
        if rowInp not in validVals :
            raise Exception("Type a valid value.")
    except Exception:
        print("Type a valid integer value in [1,3] ")
        rowInp= int(input("Type the row value : "))
    return rowInp

def columnInpValFunc():
    
    try:
        columnInp= int(input("Type the column value : "))
        if columnInp not in validVals:
            raise Exception("Type a valid value.")
    except Exception:
        print("Type a valid integer value in [1,3] ")
        columnInp= int(input("Type the column value : "))
    return columnInp

def rndRow():
    rowVal = random.randint(0,2)
    return rowVal

def rndCol():
    colVal = random.randint(0,2)
    return colVal

loopCntVal= 0

while True:
# PLAYER 1 CODE
    if loopCntVal%2 ==0 :
        # Player 1 Turn
        winnerCheck = matrixChecker(gameMatrix)
        if True in winnerCheck:
            print("The winner is : Player 2")
            break
        elif True not in winnerCheck:
            print("Player 1 Turn")
            player1Row = rowInpValFunc()
            player1Col = columnInpValFunc()
            if gameMatrix[player1Row-1][player1Col-1] != " ": 
                print("This combination is already equipped")
                print("You loose your chance to play.")
            elif gameMatrix[player1Row-1][player1Col-1] == " ":
                gameMatrix[player1Row-1][player1Col-1]= symbolP1
                [print(*cntrGame, sep=" | ")for cntrGame in gameMatrix]
 
        elif " "not in gameMatrix[0] and " "not in gameMatrix[1] and " "not in gameMatrix[2] and True not in winnerCheck():
            print("It is draw \nno one WON.")
            break
        loopCntVal +=1


# PLAYER 2 CODE
    elif loopCntVal%2==1:
        
        winnerCheck = matrixChecker(gameMatrix)

        if True in winnerCheck:
            print("The winner is : Player 1")
            break
        elif True not in winnerCheck:
            print("Player 2 Turn")
            player2Row = rowInpValFunc()
            player2Col = columnInpValFunc()
            if gameMatrix[player2Row-1][player2Col-1] != " ": 
                print("This combination is already equipped")
                print("You loose your chance to play.")
            elif gameMatrix[player2Row-1][player2Col-1] == " ":
                gameMatrix[player2Row-1][player2Col-1]= symbolP2
                [print(*cntrGame, sep=" | ")for cntrGame in gameMatrix]
        elif " "not in gameMatrix[0] and " "not in gameMatrix[1] and " "not in gameMatrix[2] and True not in winnerCheck():
            print("It is draw \nno one WON.")
            break
        loopCntVal+=1

#  Bot Chances
    elif loopCntVal%2==23423421:
        if True in winnerCheck:
            print("The winner is : Player 1")
            break
        elif True not in winnerCheck:
            print("Bot's Turn")
            botRow = rndRow()
            botCol = rndCol()
            if gameMatrix[botRow][botCol] == " ":
                gameMatrix[botRow][botCol]= symbolP2
                [print(*cntrGame, sep=" | ")for cntrGame in gameMatrix]

            else:
                while gameMatrix[botRow][botCol] != " ":
                    botRow = rndRow()
                    botCol = rndCol()
                gameMatrix[botRow][botCol]= symbolP2
                [print(*cntrGame, sep=" | ")for cntrGame in gameMatrix]

        elif " "not in gameMatrix[0] and " "not in gameMatrix[1] and " "not in gameMatrix[2] and True not in winnerCheck():
            print("It is draw \nno one WON.")
            break
        loopCntVal+=1