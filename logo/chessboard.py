from tealight.logo import move, turn

def colouredsquare(size):
  
  if size > 50:
    return
  
  square(size)
  colouredsquare(size + 1)
 
def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

colouredsquare(0)