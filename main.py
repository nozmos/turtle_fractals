from turtle import *

# Set the number of iterations and the overall width of the fractal, then Run
N = 5
WIDTH = 500

def hilbert(n: int, width = 200, cw = True, angle = 90):
  step = width / (2 ** n - 1)

  setheading(angle)

  if n == 1:
    forward(step)

    if cw: right(90)
    else: left(90)

    forward(step)
    
    if cw: right(90)
    else: left(90)

    forward(step)

  else:
    new_width = step * (2 ** (n - 1) - 1)
    
    if cw:
      hilbert(n - 1, new_width, not cw, angle - 90)
      right(90)
    else:
      hilbert(n - 1, new_width, not cw, angle + 90)
      left(90)
    
    forward(step)

    hilbert(n - 1, new_width, cw, angle)

    if cw: left(90)
    else: right(90)
    forward(step)
    if cw: left(90)
    else: right(90)

    hilbert(n - 1, new_width, cw, angle)
    
    forward(step)
    
    if cw:
      right(90)
      hilbert(n - 1, new_width, not cw, angle + 90)
    else:
      left(90)
      hilbert(n - 1, new_width, not cw, angle - 90)
    
  setheading(angle - 180)

speed(0)
delay(0)
ht()

OFFSET = WIDTH / 2
setpos(-OFFSET, -OFFSET)
clear()

hilbert(N, WIDTH)

done()