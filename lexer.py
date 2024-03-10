import sys
import keywords, tokens


class Lexer: 
  def __init__(self, file) -> None:
    self.file = file





def main():
  if len(sys.argv) < 2:
    sys.exit(1)
  try:
      archivo = open(sys.argv[1], "r")
  except FileNotFoundError:
      sys.exit("Error: Archivo no encontrado.")

  py_lexer = Lexer(archivo)

  
if __name__ == '__main__':
  main()