from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

  dir = 1

  turn(dir)

  dir = -dir

  turn(dir)

for n in range(0,3):
  move()