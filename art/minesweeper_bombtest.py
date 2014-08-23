from random import random, randint
from tealight.art import (color, line, spot, circle, box, rectangle, font, image, text, background)
from tealight.art import (screen_width, screen_height)
from tealight.utils import (sleep)

def PlaceBombs(NumberOfBombs):
  BombsPlaced = 0
  while BombsPlaced < NumberOfBombs:
    x = randint(0,HLimit -1)
    y = randint(0,WLimit -1)
    if BombArray[x][y] == 0:
      BombArray[x][y] = -1
      BombsPlaced += 1
  for x in range(0,HLimit):
    for y in range(0,WLimit):
      if BombArray[x][y] > -1:
        BombCheck(x,y)
  
def DrawGrid():
  global OffsetX, OffsetY
  OffsetX = 0
  OffsetY = 0
  color("#cccccc")
  box(StartingX - 2,StartingY - 2,SquareSize * WLimit + 8,SquareSize * HLimit +8)
  for x in range(0,HLimit):
    for y in range(0,WLimit):
      if VisibleArray[x][y]==0:
        DrawCoveredSquare()
      elif VisibleArray[x][y] == 1:
        DrawUncoveredSquare()
        if BombArray[x][y] > 0:
          BombNumber = BombArray[x][y]
          DrawNumber(x,y,BombNumber)
        elif BombArray[x][y] == -1:
          if x == lastx and y == lasty:
            DrawMine(x,y, "red")
          else:
            DrawMine(x,y, "black")
      elif VisibleArray[x][y] == 2:
        DrawFlag(x,y)
      OffsetY += SquareSize
    OffsetX += SquareSize
    OffsetY = 0
   
def DrawCoveredSquare():
  color("#cccccc")
  box(StartingX + OffsetX,StartingY + OffsetY,SquareSize,SquareSize)
  color("#757575")
  box(StartingX + (SquareSize * 0.1)/2 + OffsetX,StartingY + (SquareSize * 0.1)/2 + OffsetY,SquareSize * 0.9,SquareSize * 0.9)

def DrawUncoveredSquare():
  color("#757575")
  box(StartingX + OffsetX,StartingY + OffsetY,SquareSize,SquareSize)
  color("#cccccc")
  box(StartingX + (SquareSize * 0.1)/2 + OffsetX,StartingY + (SquareSize * 0.1)/2 + OffsetY,SquareSize * 0.9,SquareSize * 0.9)

def DrawMine(x,y, colour):
  color(colour)
  x += 0.5
  y += 0.5
  spot(StartingX + SquareSize * x,StartingY + SquareSize * y, SquareSize/5)

def DrawNumber(x,y,NumberOfMines):
  global BombArray
  
  if BombArray[x][y] == 1:
    color("blue")
  elif BombArray[x][y] == 2:
    color("green")
  elif BombArray[x][y] == 3:
    color("red")
  elif BombArray[x][y] == 4:
    color("purple")
  elif BombArray[x][y] == 5:
    color("#940023")
  elif BombArray[x][y] == 6:
    color("black")
  elif BombArray[x][y] == 7:
    color("#878787")
  elif BombArray[x][y] == 8:
    color("#00C19B")

  size = SquareSize /2
  fontsize = str(size)+"px Courier New Bold"
  font(fontsize)
  x += 0.125
  text(StartingX + SquareSize * x +size/2,StartingY + SquareSize * y +size/2, NumberOfMines)
  
def DrawFlag(x,y):
  global SquareSize
  DrawCoveredSquare()
  BoxSize = SquareSize/3
  color("gold")
  box(StartingX + SquareSize * x + SquareSize/2 - BoxSize/2,StartingY + SquareSize * y + SquareSize/2 - BoxSize/2, SquareSize/3,SquareSize/3)
  color("orange")
  rectangle(StartingX + SquareSize * x + SquareSize/2 - BoxSize/2,StartingY + SquareSize * y + SquareSize/2 - BoxSize/2, SquareSize/3,SquareSize/3)
  
def BombCheck(x,y):
  global BombArray
  BombCount = 0
  
  for (i,j) in [(x-1,y-1),(x-1,y), (x-1, y+1), (x,y-1), (x, y+1), (x+1,y-1),(x+1,y), (x+1, y+1)]:
  
    if (i >= 0 and i < WLimit and j >= 0 and j < HLimit):
      if BombArray[i][j] == -1:
        BombCount += 1  
  
  BombArray[x][y]=BombCount

def handle_mousedown(Mx,My, button):
  global lastx, lasty, VisibleArray, BombArray, lost, won, NumberUncovered
  
  Mx = Mx - StartingX
  My = My - StartingY
  if lost == False and won == False:
    if button == "left":
      if 0 < Mx < SquareSize*WLimit: 
        if 0 < My < SquareSize*HLimit:
          i=Mx/SquareSize
          j=My/SquareSize
          lastx = i
          lasty = j
          if VisibleArray[lastx][lasty] == 0:
            VisibleArray[lastx][lasty] = 1
            NumberUncovered += 1
            if BombArray[lastx][lasty] == 0:
              FloodBoard(lastx,lasty)
            else:
              IsBomb(lastx,lasty)
          if lost == True:
           for x in range(0,HLimit):
            for y in range(0,WLimit):
              if BombArray[x][y] == -1:
                VisibleArray[x][y] = 1
          elif HLimit * WLimit - NumberOfBombs == NumberUncovered:
             won = True
          DrawGrid()
          if lost == True:
            image(StartingX,StartingY, "http://www.ezimba.com/work/140822C/ezimba16125715215800.png")
          elif won == True:
            image(StartingX,StartingY,"http://www.ezimba.com/work/140822C/ezimba16125711294800.png")
    elif button == "right": 
      if 0 < Mx < SquareSize*WLimit: 
        if 0 < My < SquareSize*HLimit:
          i=Mx/SquareSize
          j=My/SquareSize
          lastx = i
          lasty = j
          if VisibleArray[lastx][lasty] == 0:
            VisibleArray[lastx][lasty] = 2
          elif VisibleArray[lastx][lasty] == 2:
            VisibleArray[lastx][lasty] = 0
          DrawGrid()

def IsBomb(x,y):
  global lost
  if BombArray[x][y] == -1:
   lost = True
     
def FloodBoard(x,y):
  global BombArray, VisibleArray, NumberUncovered

  for (i,j) in [(x-1,y), (x,y-1), (x, y+1),(x+1,y)]:
    if (i >= 0 and i < WLimit and j >= 0 and j < HLimit):
      if VisibleArray[i][j] == 0 and BombArray[i][j] >= 0:
        NumberUncovered += 1
        VisibleArray[i][j] = 1
        if BombArray[i][j] == 0:
          FloodBoard(i,j)
      
NumberOfBombs = 10
HLimit = 10
WLimit = HLimit
SquareSize = 500/HLimit
StartingX = screen_width /2 - SquareSize * WLimit/2
StartingY = 280
OffsetX = 0
OffsetY = 0
lastx = 0
lasty = 0
lost = False
won = False
NumberUncovered = 0

image(StartingX,50,"http://www.ezimba.com/work/140822C/ezimba16125732408300.png")
image(screen_width/2 - 1000,screen_height -347,"http://i.imgur.com/ofNb09J.png")
BombArray = [[0 for x in range(0,HLimit)] for y in range(0,WLimit)]
VisibleArray = [[0 for x in range(0,HLimit)] for y in range(0,WLimit)]
PlaceBombs(NumberOfBombs)
DrawGrid()