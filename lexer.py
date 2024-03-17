import sys
import keywords, tokens


class Lexer: 
  def __init__(self, file) -> None:
    self.file = file
    self.lexema = []
    self.row = 1
    self.column = 1

  def classifying(self):
    if len(self.lexema) !=0 :
        if self.lexema[0].isdigit():
            print(f"<tk_entero, {self.lexema[0]}, {self.row}, {self.column - len(self.lexema[0])}>")
            self.lexema.pop()  
        elif self.lexema[0] in keywords.keywords:
            print(f"<{self.lexema[0]}, {self.row}, {self.column - len(self.lexema[0])}>")
            self.lexema.pop()
        elif self.lexema[0].isidentifier():
            print(f"<id, {self.lexema[0]}, {self.row}, {self.column - len(self.lexema[0])}>")
            self.lexema.pop()
        else:
            sys.exit(f"Error léxico (línea: {self.row}, posición: {self.column - len(self.lexema[0])})")

  def read_file(self):
    line = self.file.read()
    line += ' '
    counter = 0

    while counter < len(line):     
      if line[counter] in tokens.tokens:
          self.classifying()
          print(f"<{tokens.tokens[line[counter]]}, {self.row}, {self.column - len(line[counter])}>") 
      elif line[counter] == "#":
          while (line[counter] not in keywords.tabs) and counter < len(line) - 1:
              counter += 1
              self.column += 1
      elif line[counter] == '"':
          self.lexema.append(line[counter])
          counter += 1
          self.column += 1
          while (line[counter] != '"') and counter < len(line) - 1:
              self.lexema.append(line[counter])
              counter += 1
              self.column += 1
          self.lexema.append(line[counter])
          counter += 1
          self.column += 1
          print(f"""<tk_cadena, {"".join(self.lexema)}, {self.row}, {self.column - len(self.lexema[0])}>""")
          self.lexema.clear()
      elif line[counter] == "'":
          self.lexema.append(line[counter])
          counter += 1
          self.column += 1
          while (line[counter] != "'") and counter < len(line) - 1:
              self.lexema.append(line[counter])
              counter += 1
              self.column += 1
          self.lexema.append(line[counter])
          counter += 1
          self.column += 1
          print(f"""<tk_cadena, {''.join(self.lexema)}, {self.row}, {self.column - len(self.lexema[0])}>""")
          self.lexema.clear()
      elif len(self.lexema) != 0 and line[counter] in keywords.spaces:
          self.classifying()
      elif len(self.lexema) == 0 and (line[counter] not in keywords.spaces):
          self.lexema.append(line[counter])        
      elif(line[counter] !=0 and (line[counter] not in keywords.spaces)):
            self.lexema[0] = self.lexema[0] + line[counter]
      
      if line[counter] == "\n" and counter < len(line):
          self.row += 1
          self.column = 0
      counter += 1
      self.column += 1




def main():
  if len(sys.argv) < 2:
    sys.exit(1)
  try:
      texto_archivo = open(sys.argv[1], "r")
  except FileNotFoundError:
      sys.exit("Error: Archivo no encontrado.")

  py_lexer = Lexer(texto_archivo)
  py_lexer.read_file()

  
if __name__ == '__main__':
  main()