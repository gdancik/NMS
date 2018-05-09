# MusicalCircles - this is a modification of "simpleCircleInstrument" by GD
 
from gui import *
from music import *
from math import sqrt
import time
import random
  
### initialize variables ######################
minPitch = C1  # instrument pitch range
maxPitch = C8
 
# create display
d = Display("Musical Circles")    # default dimensions (600 x 400)
#d.setColor( Color(51, 204, 255) )   # set background to turquoise
 
beginX = 0   # holds starting x coordinate for next circle
beginY = 0   # holds starting y coordinate
 

# maximum circle diameter - same as diagonal of display
maxDiameter = sqrt(d.getWidth()**2 + d.getHeight()**2) # calculate it

maxX = 600
 

### define callback functions ######################
def beginCircle(x, y):   # for when mouse is pressed
 
   global beginX, beginY
   
   beginX = x   # remember new circle's coordinates
   beginY = y
 
def endCircle(endX, endY):  # for when mouse is released
 
   global beginX, beginY, d, maxDiameter, minPitch, maxPitch
   
   # calculate circle parameters 
   # first, calculate distance between begin and end points
   diameter = sqrt( (beginX-endX)**2 + (beginY-endY)**2 )
   diameter = int(diameter)     # in pixels - make it an integer
   radius = diameter/2          # get radius 
   centerX = (beginX + endX)/2  # circle center is halfway between...
   centerY = (beginY + endY)/2  # ...begin and end points
 
   
   # get random color (RGB)
   red = random.randint(0, 255)               # random R (0-255)
   green = random.randint(0, 255)             # random G (0-255)
   blue = random.randint(0, 255)              # random B (0-255)
   color = Color(red, green, blue)     # build color from random RGB

   # draw circle with random color, filled, and 3 pixels thick
   circle = d.drawCircle(centerX, centerY, radius, color, True, 3)
    
   pitch = mapScale(centerX, 0, maxX, minPitch, maxPitch, MAJOR_SCALE)
    
   # need to play note - Play.note(pitch, start, duration in ms) 
 
def clearOnSpacebar(key):  # for when a key is pressed
    
  # if they pressed space, clear display and stop the music
  if key == VK_SPACE:  
     d.removeAll()        # remove all shapes
     Play.allNotesOff()   # stop all notes
          

def MakeCircle(x,y, width, pause) :
    beginCircle(x,y)    
    endCircle(x+width, y+width)
    time.sleep(pause)


def across () :
   for x in range(0,590,10) :
         y =20
         MakeCircle(x,y,10,.1)         
     
   
def randomCircles() :
   for i in range(20) :
      x = random.randint(10,600)
      y = random.randint(10,400)
      w = random.randint(10,50)
      MakeCircle(x,y,w,.2)

### assign callback functions to display event handlers #############
d.onMouseDown( beginCircle )
d.onMouseUp( endCircle )
d.onKeyDown( clearOnSpacebar )


# FIX ME: can you make random circles


# FIX ME: can you draw circles across the screen



