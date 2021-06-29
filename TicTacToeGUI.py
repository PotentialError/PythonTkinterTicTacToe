import tkinter as tk
isXTurn = True
#0 = Nothing, 1 = X, 2 = O
grid = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
def changeMessage(self: tk.Button):
    global isXTurn
    global grid
    if grid[self.grid_info()['row']][self.grid_info()['column']] == 1 or grid[self.grid_info()['row']][self.grid_info()['column']] == 2:
        return
    if isXTurn:
        isXTurn = False
        grid[self.grid_info()['row']][self.grid_info()['column']] = 1
        self.config(text = "X")
    else:
        isXTurn = True
        grid[self.grid_info()['row']][self.grid_info()['column']] = 2
        self.config(text = "O")
    winCondition = checkWin()
    if winCondition == 1:
        print("X Wins!")
        exit()
    elif winCondition == 2:
        print("O Wins!")
        exit()
    elif winCondition == 0:
        print("Tie!")
        exit()
#0 = Tie, 1 = X wins, 2 = O wins, -1 = keep playing
def checkWin():
    global button
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    allSpotsPicked = True
    XWins = False
    OWins = False
    #Check if all spots full AND if horizontal/vertical win
    for i in range(3):
        XSpotsHor = 0
        OSpotsHor = 0
        XSpotsVer = 0
        OSpotsVer = 0
        for j in range(3):
            if grid[i][j] == 0:
                allSpotsPicked = False
            elif grid[i][j] == 1:
                XSpotsHor+=1
            else:
                OSpotsHor+=1
            if grid[j][i] == 1:
                XSpotsVer+=1
            elif grid[j][i] == 2:
                OSpotsVer+=1
        if XSpotsHor == 3 or XSpotsVer == 3:
            XWins = True
        elif OSpotsHor == 3 or OSpotsVer == 3:
            OWins = True
    #Checking Diagonal wins
    if grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1:
        XWins = True
    if grid[0][2] == 1 and grid[1][1] == 1 and grid[2][0] == 1:
        XWins = True
    if grid[0][0] == 2 and grid[1][1] == 2 and grid[2][2] == 2:
        OWins = True
    if grid[0][2] == 2 and grid[1][1] == 2 and grid[2][0] == 2:
        OWins = True
    if XWins :
        return 1
    elif OWins :
        return 2
    elif allSpotsPicked:
        return 0
    else:
        return -1

window = tk.Tk()
window.geometry("510x550")
window.title("Tic-Tac-Toe")
button = tk.Button(text="TopLeft", height=5,width=10,font=("Arial", 20), command=lambda: changeMessage(button))
button2=tk.Button(text="TopMid", height=5,width=10,font=("Arial", 20), command=lambda: changeMessage(button2))
button3 = tk.Button(text="TopRight", height=5,width=10,font=("Arial", 20), command=lambda: changeMessage(button3))
button4=tk.Button(text="MidLeft", height=5,width=10,font=("Arial", 20), command=lambda: changeMessage(button4))
button5 = tk.Button(text="Middle", height=5,width=10,font=("Arial", 20), command=lambda: changeMessage(button5))
button6=tk.Button(text="MidRight", height=5,width=10,font=("Arial", 20), command=lambda: changeMessage(button6))
button7 = tk.Button(text="BotLeft", height=5,width=10,font=("Arial", 20), command=lambda: changeMessage(button7))
button8=tk.Button(text="BotMid", height=5,width=10,font=("Arial", 20), command=lambda: changeMessage(button8))
button9 = tk.Button(text="BotRight", height=5,width=10,font=("Arial", 20), command=lambda: changeMessage(button9))
button.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
window.mainloop()
