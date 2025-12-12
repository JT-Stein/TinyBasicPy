import input_output
import re
import calc
import ast
import system
import register

"""
Implemented functions:

CHAR
BYTE
WORD
INTEGER
LONG
FLOAT

LOAD
STORE

DO
LOOP

IF..THEN..

DO..
LOOP

FOR..
NEXT

PRINT

INPUT

DEG()
RAD()
SIN()
COST()
TAN()
ATN()
SQR()
EXP()
LOG()
POW()
ABS()


TIME
.SECOND
.MINUTE
.HOUR

DATE
.DAY
.MONTH
.YEAR
"""

verbose = True

class File:
  def __init__(self):
    """The File class handles code file management for the compiler"""
    self.file_name = ""

  def clear_lines(self, lines_list):
    """Removes line end characters, etc. from the lines of a file"""
    self.lines_list = lines_list
    self.lines_clean_list = []

    for line in self.lines_list:
      self.line_clean = line.replace("\n", "")
      self.lines_clean_list.append(self.line_clean)

    return self.lines_clean_list


  def read_file(self, file):
    """read_file reads the code into memory"""

    self.file = file
    self.file_name = file

    self.file = open(file, "r")

    # Converts the file data from a string to a list
    self.read_file_data = list(self.file.readlines())
    self.file.close()

    self.read_file_data = list(self.read_file_data)
    self.read_file_data = self.clear_lines(self.read_file_data)

    return self.read_file_data

class Tokenize:
  def __init__(self, verbose=False):
    """Tokenizes the source code"""
    self.verbose = verbose
    self.init_class = register.Initialize(verbose=self.verbose)

  def variable_type_clean(self, source, var_type):
    """Cleans the type label from the variable statement and returns a list of the variable names"""
    self.source = source
    self.var_type = var_type

    # Removes the variable type label as that has already been identified, any present spaces and commas
    self.variable_names = self.source.split(f"{self.var_type} ")[1]
    self.variable_names = self.variable_names.replace(" ", "")
    self.variable_names = self.variable_names.split(",")

    return self.variable_names

  def code_generate(self, source):
    self.source = source

    if self.verbose:
      print(f"\nemulator.py Tokenize.code_generate(): {self.source}")

    if self.source == "END":
      # Quits the program and does not evaluate and following commands
      if self.verbose:
        print(f"\nemulator.py Tokenize.code_generate(): end")
      quit()

    # These all handle date and time-related commands
    if "TIME" in self.source and "TIME." not in self.source:
      self.source = self.source.replace("TIME", str(system.time()))
    elif "TIME.SECOND" in self.source:
      self.source = self.source.replace("TIME.SECOND", str(system.time_second()))
    elif "TIME.MINUTE" in self.source:
      self.source = self.source.replace("TIME.MINUTE", str(system.time_minute()))
    elif "TIME.HOUR" in self.source:
      self.source = self.source.replace("TIME.HOUR", str(system.time_hour()))

    if "DATE" in self.source and "DATE." not in self.source:
      self.source = self.source.replace("DATE", str(system.date()))
    elif "DATE.DAY" in self.source:
      self.source = self.source.replace("DATE.DAY", str(system.date_day()))
    elif "DATE.MONTH" in self.source:
      self.source = self.source.replace("DATE.MONTH", str(system.date_month()))
    elif "DATE.YEAR" in self.source:
      self.source = self.source.replace("DATE.YEAR", str(system.date_year()))

    if '"' not in self.source and "'" not in self.source:
      # Replaces the variables in self.source with their values
      for item in self.source.split(" "):
        # Replaces variables only after they have been given values, NOT after they have been initialized

        if item in register.integers_dict.keys() and register.integers_dict[item] != None:
          self.source = self.source.replace(item, str(register.integers_dict[item]))

        elif item in register.chars_dict and register.chars_dict[item] != None:
          self.source = self.source.replace(item, str(register.chars_dict[item]))

        elif item in register.words_dict and register.words_dict[item] != None:
          self.source = self.source.replace(item, str(register.words_dict[item]))

        elif item in register.longs_dict and register.longs_dict[item] != None:
          self.source = self.source.replace(item, str(register.longs_dict[item]))

        elif item in register.floats_dict and register.floats_dict[item] != None:
          self.source = self.source.replace(item, str(register.floats_dict[item]))

        elif item in register.bytes_dict and register.bytes_dict[item] != None:
          self.source = self.source.replace(item, str(register.bytes_dict[item]))

      for item in self.source.split(","):
        # This allows variable values to be written to the flash memory. Fixed a problem where the variable name itself was being written

        if item in register.integers_dict.keys() and register.integers_dict[item] != None:
          self.source = self.source.replace(item, str(register.integers_dict[item]))
        
        elif item in register.chars_dict and register.chars_dict[item] != None:
          self.source = self.source.replace(item, str(register.chars_dict[item]))

        elif item in register.words_dict and register.words_dict[item] != None:
          self.source = self.source.replace(item, str(register.words_dict[item]))

        elif item in register.longs_dict and register.longs_dict[item] != None:
          self.source = self.source.replace(item, str(regsiter.longs_dict[item]))

        elif item in register.floats_dict and register.floats_dict[item] != None:
          self.source = self.source.replace(item, str(register.floats_dict[item]))

        elif item in register.bytes_dict and register.bytes_dict[item] != None:
          self.source = self.source.replace(item, str(register.bytes_dict[item]))

      if "DEG(" in self.source:
        # Splits the source code into every word, identifies where DEG is mentioned, and replaces DEG with the evaluated value
        if self.verbose:
          print("\nemulator.py Tokenize.code_generate() DEG detected")

        self.calc_clean = calc.clean(self.source, "DEG")
        self.int_value = self.calc_clean[0]
        self.command_replace = self.calc_clean[1]

        if self.verbose:
          print(f"\nemulator.py Tokenize.code_generate() self.int_value: {self.int_value}")

        self.degree_value = calc.deg(self.int_value)
        self.source = self.source.replace(self.command_replace, str(self.degree_value))

        if self.verbose:
          print(self.source)

      if "RAD(" in self.source:
        # Splits the source code into every word, identifies where RAD is mentioned, and replaces RAD with the evaluated value
        if self.verbose:
          print("\nemulator.py Tokenize.code_generate() RAD detected")
          
        self.calc_clean = calc.clean(self.source, "RAD")
        self.int_value = self.calc_clean[0]
        self.command_replace = self.calc_clean[1]

        if self.verbose:
          print(f"\nemulator.py Tokenize.code_generate() self.int_value: {self.int_value}")

        self.rad_value = calc.rad(self.int_value)
        self.source = self.source.replace(self.command_replace, str(self.rad_value))

        if self.verbose:
          print(self.source)

      if "SIN(" in self.source:
        # Splits the source code into every word, identifies where SIN is mentioned, and replaces SIN with the evaluated value
        if self.verbose:
          print("\nemulator.py Tokenize.code_generate() SIN detected")

        self.calc_clean = calc.clean(self.source, "SIN")
        self.int_value = self.calc_clean[0]
        self.command_replace = self.calc_clean[1]

        if self.verbose:
          print(f"\nemulator.py Tokenize.code_generate self.int_value: {self.int_value}")

        self.sin_value = calc.sin(self.int_value)
        self.source = self.source.replace(self.command_replace, str(self.rad_value))

      if "ABS(" in self.source:
        # Splits the source code into every word, identifies where ABS is mentioned, and replaces ABS with the evaluated value
        if self.verbose:
          print(f"\nemulator.py Tokenize.code_generate() ABS detected")

        self.calc_clean = calc.clean(self.source, "ABS")
        self.int_value = self.calc_clean[0]
        self.command_replace = self.calc_clean[1]

        if self.verbose:
          print(f"\nemulator.py Tokenize.code_generate self.int_value: {self.int_value}")

        self.abs_value = calc.abs(self.int_value)
        self.source = self.source.replace(self.command_replace, str(self.abs_value))

    if "INPUT " in self.source:
      # Finds the text shown to the user and the variable the user input will be stored in
      self.input_text = self.source.split("INPUT ")[1].split(", ")[0]
      self.input_variable = self.source.split("INPUT ")[1].split(", ")[1]

      self.user_input = input_output.io_input(self.input_text)
      register.words_dict[self.input_variable] = self.user_input

    elif "IF " in self.source:
      # Replaces the variables in self.source with their values
      for item in self.source.split(" "):
        # Replaces variables only after they have been given values, NOT after they have been initialized
        if item in register.integers_dict.keys() and register.integers_dict[item] != None:
          self.source = self.source.replace(item, str(register.integers_dict[item]))

        elif item in register.chars_dict.keys() and register.chars_dict[item] != None:
          self.source = self.source.replace(item, str(register.chars_dict[item]))

        elif item in register.words_dict.keys() and register.words_dict[item] != None:
          # These quotes are inserted so that the conditional will properly execute. A == A != "A" == "A". A == A will not execute in the eval() function
          self.source = self.source.replace(item, str('"' + register.words_dict[item]) + '"')

        elif item in register.longs_dict.keys() and register.longs_dict[item] != None:
          self.source = self.source.replace(item, str(register.longs_dict[item]))

        elif item in register.floats_dict.keys() and register.floats_dict[item] != None:
          self.source = self.source.replace(item, str(register.floats_dict[item]))

        elif item in register.bytes_dict.keys() and register.bytes_dict[item] != None:
          self.source = self.source.replace(item, str(register.bytes_dict[item]))

      # Now that variables have been replaced with their values, the conditional can be evaluated
      self.condition = self.source.split("IF ")[1].split(" THEN")[0]
      if self.verbose:
        print(f"\nemulator.py Tokenize.code_generate() self.condition: {self.condition}")
      
      if eval(self.condition):
        print(eval(self.condition))
        # Replaces the source with the action and proceeds as normal iff the condition is satisfied
        self.action = self.source.split("THEN ")[1]
        self.source = self.action

      elif not eval(self.condition):
        # Replaces the source with empty code so that nothing executes
        self.source = ""

    elif "PRINT" in self.source:
      self.print_output = self.source.split("PRINT ")[1]
      # Determines if the item to be printed is a string or a variable reference

      if "'" in self.print_output or '"' in self.print_output:
        if "'" in self.print_output:
          self.string_to_print = re.findall(r"'(.*?)'", self.print_output)[0]

        elif '"' in self.print_output:
          self.string_to_print = re.findall(r'"(.*?)"', self.print_output)[0]
 
        # Identify is set to False because the value being printed is known
        input_output.io_print(self.string_to_print, identify=False)

      else:
        # Identify is set to false because the emulator needs to identify what it is printing
        input_output.io_print(self.source, identify=True)

    # This determines if a single variable or multiple variables is being initialzied
    if "INTEGER" in self.source or "CHAR" in self.source or "WORD" in self.source or "LONG" in self.source or "FLOAT" in self.source or "BYTE" in self.source:
      if self.verbose:
        print("\nA variable is being initialized")
      if "," not in self.source:
        if self.verbose:
          print("\nemulator.py Tokenize.code_generate() a single variable is being initialized")
        if "INTEGER" in self.source:
          # Finds the name of the variable and places it in the integer regsiter
          if self.verbose:
            print(f"\nemulator.py Tokenize.code_generate() INTEGER initializing...")

          self.integer_var_name = self.source.split("INTEGER ")[1]
          self.init_class.init_integer(self.integer_var_name)

        elif "CHAR" in self.source:
          # Finds the name of the variable and places it in the character register
          if self.verbose:
            print(f"\nemulator.py Tokenize.code_generate() CHAR initializing...")
          self.char_var_name = self.source.split("CHAR ")[1]
          self.init_class.init_char(self.char_var_name)

        elif "WORD" in self.source:
          # Finds the name of the variable and places it in the word register
          if self.verbose:
            print(f"\nemulator.py Tokenize.code_generate() WORD initializing...")
          self.word_var_name = self.source.split("WORD ")[1]
          self.init_class.init_word(self.word_var_name)

        elif "LONG" in self.source:
          # Finds the name of the variable and places it in the long register
          if self.verbose:
            print(f"\nemulator.py Tokenize.code_generate() LONG initializing...")
          self.long_var_name = self.source.split("LONG ")[1]
          self.init_class.init_long(self.long_var_name)

        elif "FLOAT" in self.source:
          # Finds the name of the variable and places it in the float register
          if self.verbose:
            print(f"\nemulator.py Tokenize.code_generate() FLOAT initializing...")
          self.float_var_name = self.source.split("FLOAT ")[1]
          self.init_class.init_float(self.float_var_name)

        elif "BYTE" in self.source:
          # Finds the name of the variable and places it in the byte register
          if self.verbose:
            print(f"\nemulator.py Tokenize.code_generate() BYTE initializing...")
          self.byte_var_name = self.source.split("BYTE ")[1]
          self.init_class.init_byte(self.byte_var_name)

      elif "," in self.source: 
        self.variable_type = self.source.split(" ")[0]
        if self.variable_type == "INTEGER":
          self.variable_names = self.variable_type_clean(self.source, "INTEGER")
    
          # Loops through the variable names and places them in integer memory
          for self.variable_name in self.variable_names:
            self.init_class.init_integer(self.variable_name)

        elif self.variable_type == "CHAR":
          self.variable_names = self.variable_type_clean(self.source, "CHAR")

          # Loops through the variable names and places them in char memory
          for self.variable_name in self.variable_names:
            self.init_class.init_char(self.variable_name)

        elif self.variable_type == "WORD":
          self.variable_names = self.variable_type_clean(self.source, "WORD")

          # Loops through the variable names and places them in word memory
          for self.variable_name in self.variable_names:
            self.init_class.init_word(self.variable_name)
        
        elif self.variable_type == "LONG":
          self.variable_names = self.variable_type_clean(self.source, "LONG")

          # Loops through the variable names and places them in long memory
          for self.variable_name in self.variable_names:
            self.init_class.init_word(self.variable_name)

        elif self.variable_type == "FLOAT":
          self.variable_names = self.variable_type_clean(self.source, "FLOAT")

          # Loops through the variable names and places them in float memory
          for self.variable_name in self.variable_names:
            self.init_class.init_float(self.variable_name)

        elif self.variable_type == "BYTE":
          self.variable_names = self.variable_type_clean(self.source, "BYTE")

          # Loops through the variable names and places them in byte memory
          for self.variable_name in self.variable_names:
            self.init_class.init_byte(self.variable_name)

    elif " = " in self.source:
      # Assumes the form A = 0, for example
      if self.verbose:
        print("Variable is being assigned a value...")
        print(self.source)
      self.variable_name = self.source.split(" = ")[0]
      if self.verbose:
        print(self.source.split("="))
        print(f"emulator.py Tokenize.code_generate() self.variable_name: {self.variable_name}")
      self.variable_value = self.source.split(" = ")[1]
      if self.verbose:
        print(f"emulator.py Tokenize.code_generate() self.variable_value: {self.variable_value}")

      if self.variable_name in register.integers_dict.keys():
        register.integers_dict[self.variable_name] = self.variable_value
        if self.verbose:
          print(f"\nemulator.py Tokenize.code_generate() registers.integers_dict: {register.integers_dict}")

      elif self.variable_name in register.chars_dict.keys():
        register.chars_dict[self.variable_name] = self.variable_value
        if self.verbose:
          print(f"\nemulator.py Tokenize.code_generate() registers.chars_dict: {register.chars_dict}")

      elif self.variable_name in register.words_dict.keys():
        register.words_dict[self.variable_name] = self.variable_value
        if self.verbose:
          print(f"\nemulator.py Tokenize.code_generate() register.words_dict: {register.words_dict}")

      elif self.variable_name in register.longs_dict.keys():
        register.longs_dict[self.variable_name] = self.variable_value
        if self.verbose:
          print(f"\nemulator.py Tokenize.code_generate() register.longs_dict: {register.longs_dict}")

      elif self.variable_name in register.bytes_dict.keys():
        register.bytes_dict[self.variable_name] = self.variable_value
        if self.verbose:
          print(f"\nemulator.py Tokenize.code_generate() register.bytes_dict: {register.bytes_dict}")

    if "STORE " in self.source:
      self.store_address = self.source.split("STORE ")[1].split(",")[0]
      self.variables = self.source.split("STORE ")[1].replace(" ", "").split(",")[1:]

      print(self.variables)

      # Writes to the memory as $F000: 1,2,3, for example
      self.flash_file = open("flash_memory.txt", "w")
      self.flash_file.write(f"{str(self.store_address)}: {str(self.variables)}")

      self.flash_file.close()

    elif "LOAD " in self.source:
      self.load_address = self.source.split("LOAD ")[1].split(",")[0]
      self.load_variables = self.source.split("LOAD ")[1].split(",")[1:]

      print(self.load_variables)

      # Reads from the memory as $F000, for example
      self.flash_file = open("flash_memory.txt", "r")
      self.flash_data = self.flash_file.readlines()

      self.flash_file.close()

      # This code finds the line that contains the address being loaded. It loads the variables into memory using the aliases the user has provided. However, they are stored in memory as their actual values without reference to their name(s)
      for line in self.flash_data:
        if self.load_address in line:
          self.read_variables = line.split(": ")[1]

          # self.read_variables is read from the file as a string. ast converts this to a Python list
          self.read_variables = ast.literal_eval(self.read_variables)

          num = 0
          for item in self.load_variables:
            if item in register.integers_dict.keys():
              register.integers_dict[item] = self.read_variables[num]

            num += 1


file_load = File()
user_code = file_load.read_file("io_test.bas")

if verbose:
  print(f"\nRead {file_load.file_name}: {user_code}")

tokenizer = Tokenize(verbose=verbose)

while_loop_code = []
while_loop_run = False
while_loop_write = False

for_loop_code = []
for_loop_runs = 0
for_loop_run = False
for_loop_write = False
 
for line in user_code:
  if for_loop_write:
    if line != "NEXT":
      for_loop_code.append(line)

    if line == "NEXT":
      for_loop_write = False
      for_loop_run = True

  if "FOR " in line:
    for_loop_write = True

    # Extracts when the for loop should stop
    if verbose:
      print(f'emulator.py for line in user_code line.split(" = ")[1]: {line.split(" = ")[1]}')
      print(f'emulator.py for line in user_code line.split(" = ")[1].split(" TO "): {line.split(" = ")[1].split(" TO ")})')
    for_loop_runs = int(line.split(" = ")[1].split(" TO ")[1])

    # This extracts the variable that the loop is stepping by, what its initial value is, and initializes it in the register
    step_info = line.split("FOR ")[1].split(" TO")[0].split(" = ")
    step_variable = step_info[0]
    step_start = int(step_info[1])
  
    # Adds the defined step variable into the register as an int
    register.integers_dict[step_variable] = step_start

  if for_loop_run:
    for x in range(for_loop_runs - step_start):
      for line in for_loop_code:
        tokenizer.code_generate(line)

      register.integers_dict[step_variable] += 1

    for_loop_code = []
    for_loop_runs = 0
    for_loop_run = False
    for_loop_write = False

  if not while_loop_write and not while_loop_run and not for_loop_write and not for_loop_run:
    tokenizer.code_generate(line)

  if while_loop_write:
    if line != "LOOP":
      while_loop_code.append(line)

    if line == "LOOP":
      while_loop_write = False
      while_loop_run = True

  if line == "DO" and not while_loop_write:
    while_loop_write = True

  if while_loop_run:
    while True:
      for line in while_loop_code:
        tokenizer.code_generate(line)





