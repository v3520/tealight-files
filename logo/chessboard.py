from tealight.logo import move, turn

def colouredsquare(size):
  
  if size > 50:
    return
  
  move(size)
  turn(90)
  colouredsquare(size + 1)
  
colouredsquare(0)