import js
p5 = js.window

program_state = 'START'
font1  = p5.loadFont('Chalkboard.ttf')
short_speed = 5
long_speed = 3
short_speed2 = 5
long_speed2 = 3
short_speed3 = 5
long_speed3 = 3
point_x = 0

print('Press "p" to play sound')



import js
p5 = js.window

sound = p5.loadSound('bgmusic.wav')

program_state = 'START'
font1 = p5.loadFont('Chalkboard.ttf')
short_speed = 8
long_speed = 4
point_x = 0


def Winpoint():
  global point_x
  print('point', point_x)
  p5.fill('#F8D489')
  p5.text(22)
  p5.text(point_x, 425, 25)


class Start():

  def __init__(self):
    self.img = p5.loadImage('data/start.png')
    self.x = 215
    self.y = 160

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width / 3.5,
             -self.img.height / 3.5)
    p5.pop()


class Guide():

  def __init__(self):
    self.img = p5.loadImage('data/guide.png')
    self.x = 225
    self.y = 190

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width / 4.5,
             -self.img.height / 4.5)
    p5.pop()


class Pinocchio():

  def __init__(self):
    self.img = p5.loadImage('data/pinocchio.png')
    self.x = 120
    self.y = 250

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width / 4.5,
             -self.img.height / 4.5)
    p5.pop()


class Point():  
  def __init__(self):
    self.img = p5.loadImage('data/points.png')
    self.x = 500
    self.y = 30
    
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 5, -self.img.width/4, -self.img.height/4)
    p5.pop()


class Bubble():

  def __init__(self):
    self.img = p5.loadImage('data/bubble.png')
    self.x = 215
    self.y = 130

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width / 4,
             -self.img.height / 4)
    p5.pop()


class Short():

  def __init__(self):
    self.img = p5.loadImage('data/short.png')
    self.x = 130
    self.y = 275
    self.width = self.img.width

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, self.img.width / 4, self.img.height / 4)
    p5.pop()
class Short2():

  def __init__(self):
    self.img = p5.loadImage('data/short.png')
    self.x = 130
    self.y = 275
    self.width = self.img.width

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, self.img.width / 4, self.img.height / 4)
    p5.pop()


class Long():

  def __init__(self):
    self.img = p5.loadImage('data/long.png')
    self.x = 130
    self.y = 275
    self.width = self.img.width

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, self.img.width / 4, self.img.height / 4)
    p5.pop()

class Long2():

  def __init__(self):
    self.img = p5.loadImage('data/long.png')
    self.x = 130
    self.y = 275
    self.width = self.img.width

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, self.img.width / 4, self.img.height / 4)
    p5.pop()
    


class Statement1():

  def __init__(self):
    self.x = 215
    self.y = 190

  def draw(self):
    p5.fill(0)
    p5.textSize(16)
    p5.text('Chocolate is made from wood,', self.x, self.y)
    p5.text('since they are all in brown.', self.x, self.y+ 20)


class Statement2():

  def __init__(self):
    self.x = 210
    self.y = 185

  def draw(self):
    p5.fill(0)
    p5.textSize(16)
    p5.text('Cloud is made', self.x + 60, self.y)
    p5.text('from marshmellow', self.x + 45, self.y + 20)


class Statement3():

  def __init__(self):
    self.x = 240
    self.y = 190

  def draw(self):
    p5.fill(0)
    p5.textSize(16)
    p5.text('Dogs cannot fly', self.x, self.y)

class WIN():

  def __init__(self):
    self.x = 256
    self.y = 186

  def draw(self):
    p5.fill(0)
    p5.textSize(16)
    p5.text('You get 1 point!', self.x + 5, self.y)
    p5.text('Click to continue', self.x, self.y + 20)

class LOSE():

  def __init__(self):
    self.x = 256
    self.y = 186

  def draw(self):
    p5.fill(0)
    p5.textSize(16)
    p5.text('It is an wrong nose!', self.x - 26, self.y)
    p5.text('Click to continue', self.x, self.y + 20)


class HE():

  def __init__(self):
    self.img = p5.loadImage('data/win.png')
    self.x = 215
    self.y = 160

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width / 3.5,
             -self.img.height / 3.5)
    p5.pop()


class BE():

  def __init__(self):
    self.img = p5.loadImage('data/lose.png')
    self.x = 215
    self.y = 160

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width / 3.5,
             -self.img.height / 3.5)
    p5.pop()


start = Start()
guide = Guide()
pinocchio = Pinocchio()
point = Point()
bubble = Bubble()
short = Short()
long = Long()
short2 = Short()
long2 = Long()
statement1 = Statement1()
statement2 = Statement2()
statement3 = Statement3()
he = HE()
be = BE()
win = WIN()
lose = LOSE()

  
def setup():
  global font1, sound
  p5.createCanvas(500, 500)
  p5.rectMode(p5.CENTER)
  # p5.imageMode(p5.CENTER)
  p5.textFont(font1)
  p5.textSize(24)
  #sound.loop()


def draw():
  global program_state, font1, start, guide, pinocchio, point, bubble, short, short_speed, long_speed, statement1, statement2, statement3, win, lose, point_x
  p5.background('#64C3EF')
  p5.fill(255)
  p5.textSize(16)
  #print('program_state =' + program_state)
  p5.text('program_state = '+ program_state, 10, 40)
  
  p5.textFont(font1)

  if (program_state == 'START'):
    start.draw()
    p5.fill(255)
    p5.textSize(24)
    p5.text('Click Anywhere To Start', 130, 360)
  elif (program_state == 'GUIDE'):
    guide.draw()
  elif (program_state == 'PLAY' or program_state == 'PLAY2' or program_state == 'PLAY3' or program_state == 'WIN1' or program_state == 'LOSE1' or program_state == 'WIN2' or program_state == 'LOSE2'):
    global short_speed, long_speed, short_speed2, long_speed2, long_speed3, short_speed3
    pinocchio.draw()
    point.draw()
    bubble.draw()
    Winpoint()

  # statement transitions
    if (p5.keyIsPressed == True):
      # long.x = 200
      if (p5.key == ' '):
        if (program_state == 'PLAY'):
          long_speed = 0
          short_speed = 0
          if (long.x > 66 and long.x < 200):
            point_x += 1
            program_state = 'WIN1'
            short.draw()
            long.draw()
          else:
            program_state = 'LOSE1'
          # long.x = 280 
            
        elif (program_state == 'PLAY2'):
          long_speed2 = 0
          short_speed2 = 0
          if (long2.x > 66 and long2.x < 192):
            point_x += 1
            program_state = 'WIN2'
            short2.draw()
            long2.draw()
          else:
            program_state = 'LOSE2'
            
        elif (program_state == 'PLAY3'):
          long_speed3= 0
          short_speed3 = 0
          if (short2.x > 66 and short2.x < 192):
            point_x += 1
            program_state = 'EVAL'
          else:
            program_state = 'EVAL'

    if (p5.mouseIsPressed == True):
      if (p5.mouseButton == p5.LEFT):
            if (program_state == 'WIN1'):
              program_state = 'PLAY2'

            elif (program_state == 'LOSE1'):
              program_state = 'PLAY2'
              
            elif (program_state == 'WIN1'):
              program_state = 'PLAY2'

            elif (program_state == 'LOSE2'):
              program_state = 'PLAY3'

            elif (program_state == 'WIN2'):
              program_state = 'PLAY3'

              
# codes
    if (program_state == 'PLAY'):
      statement1.draw()
      long.x += long_speed
      short.x += short_speed
      # p5.text(('long.x =', long.x), 10, 60)
      # p5.text(('long_speed =', long_speed), 10, 80)
      if(long.x > p5.width - 250) \
      or(long.x < 20):
        long_speed *= -1  # change direction
      long.draw()
      if(short.x > p5.width - 5) \
      or(short.x < 5):
        short_speed *= -1  # change direction
      short.draw()
    

    if (program_state == 'WIN1'):
      global win, lose
      bubble.draw()
      win.draw()
      pinocchio.draw()
      short.draw()
      point.draw()
      Winpoint()
      long.draw()
      short.draw()
      
      
    if (program_state == 'LOSE1'):
      bubble.draw()
      lose.draw()
      pinocchio.draw()
      point.draw()
      Winpoint()
      long.draw()
      short.draw()

      
      # long.x += long_speed
      # #print('long.x =', long.x)
      # #print('long_speed =', long_speed)
      # p5.text(('long.x =', long.x), 10, 60)
      # p5.text(('long_speed =', long_speed), 10, 80)
      # if(long.x > p5.width - 250) \
      # or(long.x < 20):
      #   long_speed *= -1  # change direction
  
      # short.x += short_speed
      # if(short.x > p5.width - 5) \
      # or(short.x < 5):
      #   short_speed *= -1  # change direction
      # if (show_short2 == True and show_long2 == True):
      #   long.draw()
      #   short.draw()
      
    if (program_state == 'PLAY2'):
      bubble.draw()
      pinocchio.draw()
      point.draw()
      Winpoint()
      statement2.draw()
      short_speed = 5
      long_speed = 3

      # p5.text(('long.x =', long.x), 10, 60)
      # p5.text(('long_speed =', long_speed), 10, 80)
      long2.x += long_speed2
      short2.x += short_speed2
      if(long2.x > p5.width - 250) \
      or(long2.x < 20):
        long_speed2 *= -1  # change direction
      
      if(short2.x > p5.width - 5) \
      or(short2.x < 5):
        short_speed2 *= -1  # change direction 
      long2.draw()
      short2.draw()


    if (program_state == 'WIN2'):
      bubble.draw()
      win.draw()
      pinocchio.draw()
      short2.draw()
      long2.draw()
      point.draw()
      Winpoint()
      long_speed = 3
      short_speed = 5  
        
    if (program_state == 'LOSE2'):
      bubble.draw()
      pinocchio.draw()
      point.draw()
      Winpoint()
      lose.draw()
      short2.draw()
      long2.draw()

    if (program_state == 'PLAY3'):
      bubble.draw()
      pinocchio.draw()
      point.draw()
      Winpoint()
      statement3.draw()
      # p5.text(('long.x =', long.x), 10, 60)
      # p5.text(('long_speed =', long_speed), 10, 80)
      long2.x += long_speed3
      short2.x += short_speed3
      if(long2.x > p5.width - 250) \
      or(long2.x < 20):
        long_speed3 *= -1  # change direction
      long2.draw()
      
      if(short2.x > p5.width - 5) \
      or(short2.x < 5):
        short_speed3 *= -1  # change direction  
      short2.draw()
      
  elif (program_state == 'EVAL'):
    if (point_x == 3):
      he.draw()
      p5.fill(255)
      p5.textSize(24)
      p5.text('Click Anywhere To Restart', 100, 360)
    elif (point_x <= 2):
      be.draw()
      p5.fill(255)
      p5.textSize(24)
      p5.text('Click Anywhere To Restart', 100, 360)

  # show cursor coordinates:
  p5.text((int(p5.mouseX), int(p5.mouseY)), 10, 20)
  p5.strokeWeight(1)  # 1-pixel stroke


def keyPressed(event):
  print('key pressed.. ' + p5.key)
  if(p5.key == 'p'):
    print('loop sound..')
    sound.loop()

def keyReleased(event):
  pass


def mousePressed(event):
  global program_state, long_speed, short_speed
  if (program_state == 'START'):
    program_state = 'GUIDE'
    print('program_state = ' + program_state)
  elif (program_state == 'GUIDE'):
    program_state = 'PLAY'
    print('program_state = ' + program_state)
  elif(program_state == 'EVAL'):
    program_state = 'START'


def mouseReleased(event):
  print('program_state = ' + program_state)
