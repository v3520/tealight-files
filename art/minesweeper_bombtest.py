from random import random, randint
from tealight.art import (color, line, spot, circle, box, image, text, background)
from tealight.art import (screen_width, screen_height)
from tealight.utils import (sleep)

def PlaceBombs(NumberOfBombs):
  BombsPlaced = 0
  while BombsPlaced < NumberOfBombs:
    x = randint(0,9)
    y = randint(0,9)
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
  color("red")
  x += 0.35
  y += 0.25
  text(StartingX + SquareSize * x,StartingY + SquareSize * y, NumberOfMines)
  
def DrawFlag(x,y):
  image(StartingX + SquareSize * x,StartingY + SquareSize * y,"http://www.ezimba.com/work/140822C/ezimba16125759306700.gif")

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
            print NumberUncovered
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
  global BombArray
  BombCount = 0
  
  for (i,j) in [(x-1,y-1),(x-1,y), (x-1, y+1), (x,y-1), (x, y+1), (x+1,y-1),(x+1,y), (x+1, y+1)]:
  
    if (i >= 0 and i < WLimit and j >= 0 and j < HLimit):



NumberOfBombs = 1
NumberUncovered = 0
HLimit = 10
WLimit = 10
SquareSize = 50
StartingX = screen_width /2 - SquareSize * WLimit/2
StartingY = 100
OffsetX = 0
OffsetY = 0
lastx = 0
lasty = 0
lost = False
won = False

BombArray = [[0 for x in range(0,HLimit)] for y in range(0,WLimit)]
VisibleArray = [[0 for x in range(0,HLimit)] for y in range(0,WLimit)]
PlaceBombs(NumberOfBombs)
DrawGrid()



