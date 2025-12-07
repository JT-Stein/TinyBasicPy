import register

def io_print(string, identify=False):
  if not identify:
    # Only a string is being printed, so the value does not have to be identified
    print(string)

  elif identify:
    # A variable or otherwise is being printed, so the value has to be identified
    print_statement = string.split("PRINT ")[1]

    for item in print_statement.split(" "):
      if item in register.integers_dict.keys():
        print_statement = print_statement.replace(item, str(register.integers_dict[item]))
 
      elif item in register.chars_dict.keys():
        print_statement = print_statement.replace(item, str(register.chars_dict[item]))

      elif item in register.words_dict.keys():
        print_statement = print_statement.replace(item, str(register.words_dict[item]))

      elif item in register.longs_dict.keys():
        print_statement = print_statement.replace(item, str(register.longs_dict[item]))

      elif item in register.floats_dict.keys():
        print_statement = print_statement.replace(item, str(register.floats_dict[item]))

      elif item in register.bytes_dict.keys():
        print_statement = print_statement.replace(item, str(register.bytes_dict[item]))

    # Evaluates mathematical statements
    if "+" in print_statement or "-" in print_statement or "*" in print_statement or "/" in print_statement:
      print(eval(print_statement))

    else:
      print(print_statement)


