from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["orange", "yellow", "purple"]

for i in range(0,100):
  move(i)
  turn(104)
  color(colors[i%3])