import math

def clean(source, function):
  split = source.split(" ")
  for item in split:
    if function in item:
      clean_item = item.split(function)[1].strip("(").strip(")")
      int_item = int(clean_item)

      return int_item, item

def deg(radians):
  # Returns the given angle in radians in degrees
  return math.degrees(radians)

def rad(degrees):
  # Returns the given angle in degrees in radians
  return math.radians(degrees)

def sin(radians):
  # Returns the sin of the given angle in radians
  return math.sin(radians)

def cos(radians):
  # Returns the cos of the given angle in radians
  return math.cos(radians)

def tan(radians):
  # Returns the tan of the given angle in radians
  return math.tan(radians)

def atan(ratio):
  # Returns the inverse tangent of the given ratio of sides
  return math.atan(ratio)

def sqr(number):
  # Returns the square root of the given number
  return math.sqrt(number)

def exp(number):
  # Returns e ^ number
  return math.e ^ number

def log(number):
  # Returns log base e of the given number
  return math.log(number)

def pow(base, exponent):
  # Returns base ^ exponent
  return base ^ exponent
