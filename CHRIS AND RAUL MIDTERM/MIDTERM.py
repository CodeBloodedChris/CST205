import math

def drunkifi():
  setMediaFolder()
  path = getMediaPath("bar.jpg")
  img = makePicture(path)
  path = getMediaPath("beer.jpg")
  beer = makePicture(path)
  
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
  img = blur(img)
    
  img = addBackgroundPattern(img, beer, 100, 100, 50, 50)
  img = addShadowEffect(img, 50, 50, img.height-100, img.width-100)

  show(img)
  
def c():
  setMediaFolder()
  path = getMediaPath("CSUMB KEY.jpg")
  key = makePicture(path)
  path = getMediaPath("CSUMB KEY 2.jpg")
  key2 = makePicture(path)
  path = getMediaPath("2014.jpg")
  img = makePicture(path)
  path = getMediaPath("otter.jpg")
  otter = makePicture(path)

  waterMark(img, key2, 50, 30, .3)
  waterMark(img, key, 50, 30, .7)

  img = addBackgroundPattern(img, otter, 100, 100, 50, 50)
  img = addShadowEffect(img, 50, 50, img.height-100, img.width-100)

  blueUp(img)

  show(img)

#will blur an image
def blur(img):
  pixels = getPixels(img)
  for p in pixels:
    #finds x and y pixels in the image while 
    if p.x < getWidth(img)-1 and p.y < getHeight(img)-1:
      pR=getPixel(img, p.x+1, p.y)#gets pixels right
      pB=getPixel(img, p.x, p.y+1)#gets pixels bottom 
      p2=getPixel(img, p.x+1, p.y+1)#moves next row
      bR = getBlue(pR)
      bB = getBlue(pB)
      b2 = getBlue(p2)
      b = getBlue(p)
      setBlue(p, (bR+bB+b2+b)/4)#sets all blue pixels to a 4th
      gR = getGreen(pR)
      gB = getGreen(pB)
      g2 = getGreen(p2)
      g = getGreen(p)
      setGreen(p, (gR+gB+g2+g)/4)#sets all green pixels to a 4th
      rR = getRed(pR)
      rB = getRed(pB)
      r2 = getRed(p2)
      r = getRed(p)
      setRed(p, (rR+rB+r2+r)/4)#sets all red pixels to a 4th
  return img    

#will take half of the picture and divide it into 4 pieces  
def mirror(pic):
  p1 = getWidth(pic)/2
  p2 = getHeight(pic)/2
  for y in range(0,p2):
    for x in range(0,p1):
      upL = getPixel(pic,x,y)
      upR = getPixel(pic,getWidth(pic)-x-1,y)
      bRt = getPixel(pic,getWidth(pic)-x-1,getHeight(pic)-y-1)
      bLt = getPixel(pic,x,getHeight(pic)-y-1)
      color1 = getColor(upL)
      setColor(upR,color1)
      setColor(bRt,color1)
      setColor(bLt,color1)
#Green screen function from previous assignment modified to take target x and y coordinates
def waterMark(img, key, targetX, targetY, shadow):
  new_y = targetY
  for y in range (0,getHeight(key)):
      new_y += 1
      new_x = targetX
      for x in range (0, getWidth(key)):
        new_x += 1
        original=getPixel(key, x, y)
        pixel=getPixel(img, new_x, new_y)
        color = makeColor(pixel.red * (1 - shadow), pixel.green * (1 - shadow), pixel.blue * (1 - shadow))
        if getRed(original) < (getGreen(original) - 30) and getBlue(original) < (getGreen(original) - 30):
          setColor(pixel, color)
  return img

# function to blue up the image
def blueUp(pic):
  pixels = getPixels(pic)
  for p in pixels:
    b = getBlue(p)
    setBlue(p, b*1.9)
  return pic

#Adds an artificial shading effect to the bottom and right sides of a chosen area inside of a photo.
def addShadowEffect(image, startX, startY, height, width, shadow_depth = 20, shadow_offset = 10, blur_repetitions = 3):
  #image - The image that the effect will be applied to.
  #startX - The starting x-coordinate of the area the effect will be applied to.
  #startY - The starting y-coordinate of the area the effect will be applied to.
  #height - The height of the area the effect will be applied to.
  #width - The width of the area the effect will be applied to.
  #shadow_depth (optional) - The amount of pixels out from the x and y coordinates that will be shaded. Higher value = longer shadow.
  #shadow_offset (optional) - The amount of pixels that the shadow will be offset from the startX and startY coordinates. Creates more angled look.
  #blur_repetitions (optional) - The amount of time the blur effect will be run on the shading values.

  #Creates a matrix to store shading values.
  #Matrix contains x and y coordinates and determines each coordinate's shading value
  #by its right/bottom distance from the area that the effect is being applied to,
  #stopping once it reaches the designated depth.
  #Shading values are from 1.0 to 0.
  shadow_matrix = [[0 for i in xrange(height + shadow_depth)] for i in xrange(width + shadow_depth)]
  for x in range(shadow_offset - 1,width + shadow_depth - 1):
    for y in range(shadow_offset - 1, height + shadow_depth - 1):
      if x <= width and y <= height:
        shadow_matrix[x][y] = 1.0
      elif x > width and y <= height:
        shadow_matrix[x][y] = ((width + shadow_depth) - x) * (1.0 / shadow_depth)
      elif x <= width and y > height:
        shadow_matrix[x][y] = ((height + shadow_depth) - y) * (1.0 / shadow_depth)
      elif x > width and y > height:
        dist = calculateDistance(width, height, x, y)
        if dist > shadow_depth: shadow_matrix[x][y] = 0
        else: shadow_matrix[x][y] = (shadow_depth - dist) * (1.0 / shadow_depth)

  #Create Blur to smooth edges
  #Blur works by taking the average of each coordinate's shadow multiplier and the multipliers of its 8 surrounding neighbors.
  #Repeats multiple times to increase the effect.
  for count in range(blur_repetitions):
    for x in range(1, width + shadow_depth - 1):
      for y in range(1, height + shadow_depth - 1):
        sum = shadow_matrix[x][y]
        for i in range(-1, 2):
          for j in range(-1, 2):
            if i != 0 or j != 0: sum += shadow_matrix[x + i][y + j]
        shadow_matrix[x][y] = sum / 9

  #Applies the shadow effect using the shading matrix to each pixel on the right and bottom side of the selected area.
  #Uses depth and offset values to determine where to shade.
  #Formula for applying the effect is color value * (1 - shading value)
  for x in range(0, width + shadow_depth - 1):
    for y in range(0, height + shadow_depth - 1):
      if x >= width - 1 or y >= height - 1:
        pixel = getPixel(image, startX + x, startY + y)
        color = makeColor(pixel.red * (1 - shadow_matrix[x][y]), pixel.green * (1 - shadow_matrix[x][y]), pixel.blue * (1 - shadow_matrix[x][y]))
        setColor(pixel, color)
  return image

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

#image = get_pic()
#pattern = get_pic()
#border_image = addBackgroundPattern(image, pattern, 200, 200, 100, 150)
#image_with_shadow = addShadowEffect(border_image, 100, 150, image.height, image.width)
#show(image_with_shadow)
