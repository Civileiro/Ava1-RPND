# Grupo:
# Bea Zardo
# Gabriel Prost

import sys

def elem_to_str(e):
  if type(e) is tuple:
    return "(" + ", ".join(e) + ")"
  return str(e)

def set_to_str(s):
  return "{" + ", ".join(elem_to_str(a) for a in s) + "}"

if len(sys.argv) < 2:
  file_path = "input.txt"
else:
  file_path = sys.argv[1] or "input.txt"

try:
    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read all lines from the file and store them in a list
        lines = file.readlines()

    # Now, 'lines' contains an array of lines from the file
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    # Get the amount of operations
    cnt = int(lines[0])
    lines = lines[1:]

    for i in range(cnt):
      op = lines[i * 3 + 0]
      a = set(lines[i * 3 + 1].split(", "))
      b = set(lines[i * 3 + 2].split(", "))
      op_name = None
      res = None
      match op:
        case "U":
          op_name = "União"
          res = a | b
        case "I":
          op_name = "Interseção"
          res = a & b
        case "D":
          op_name = "Diferença"
          res = a - b
        case "C":
          op_name = "Produto Cartesiano"
          res = {(x, y) for x in a for y in b}
        
      ra = set_to_str(a)
      rb = set_to_str(b)
      rr = set_to_str(res)
      print(f"{op_name}: conjunto 1 {ra}, conjunto 2 {rb}. Resultado: {rr}")
      
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
