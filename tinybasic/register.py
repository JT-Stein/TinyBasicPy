integers_dict = {}
chars_dict = {}
words_dict = {}
longs_dict = {}
floats_dict = {}
bytes_dict = {}

class Initialize:
  def __init__(self, verbose=False):
    """Initializes variable(s) of a specified type into memory"""
    global integers_dict, chars_dict, words_dict, longs_dict, floats_dict, bytes_dict
    self.verbose = verbose

  def init_integer(self, identifier):
    integers_dict[identifier] = None
    if self.verbose:
      print(f"\nregister.py Initialize.init_integer() integers_dict: {integers_dict}")

  def init_char(self, identifier):
    chars_dict[identifier] = None
    if self.verbose:
      print(f"\nregister.py Initialize.init_char() chars_dict: {chars_dict}")

  def init_word(self, identifier):
    words_dict[identifier] = None
    if self.verbose:
      print(f"\nregister.py Initialize.init_word() words_dict: {words_dict}")

  def init_long(self, identifier):
    longs_dict[identifier] = None
    if self.verbose:
      print(f"\nregister.py Initialize.init_long() longs_dict: {longs_dict}")

  def init_float(self, identifier):
    floats_dict[identifier] = None
    if self.verbose:
      print(f"\nregister.py Initialize.init_float() floats_dict: {floats_dict}")

  def init_byte(self, identifier):
    bytes_dict[identifier] = None
    if self.verbose:
      print(f"\nregister.py Initialize.init_byte() bytes_dict: {bytes_dict}")

class Assign:
  def __init__(self, verbose=False):
    """Assigns specified values to a variable"""
    self.verbose = verbose

  def assign_variable(self, name, value):
    # Assigns the given value to the given variable in memory

    global integers_dict, chars_dict, words_dict, longs_dict, floats_dict, bytes_dict

    self.name = name
    self.value = value

    if self.name in integers_dict.keys():
      self.integers_dict[self.name] = self.value
      if self.verbose:
        print(f"\nregister.py Assign.assign_variable() {self.name} is an integer")

    elif self.name in chars_dict.keys():
      self.chars_dict[self.name] = self.value
      if self.verbose:
        print(f"\nregister.py Assign.assign_variable() {self.name} is a char")

    elif self.name in words_dict.keys():
      self.words_dict[self.name] = self.value
      if self.verbose:
        print(f"\nregister.py Assign.assign_variable() {self.name} is a word")

    elif self.name in longs_dict.keys():
      self.longs_dict[self.name] = self.value
      if self.verbose:
        print(f"\nregister.py Assign.assign_variable() {self.name} is a long")

    elif self.name in floats_dict.keys():
      self.floats_dict[self.name] = self.value
      if self.verbose:
        print(f"\nregister.py Assign.assign_variable {self.name} is a float")
    
    elif self.name in bytes_dict.keys():
      self.bytes_dict[self.name] = self.value
      if self.verbose:
        print(f"\nregister.py Assign.assign_variable {self.name} is a byte")




