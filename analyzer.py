import lexer as lex, sys



class Parser:
   def __init__(self, tokens):
      self.tokens = tokens
    
    




def main():
  if len(sys.argv) < 2: 
    sys.exit(1)
  try:
      texto_archivo = open(sys.argv[1], "r")
  except FileNotFoundError:
      sys.exit("Error: Archivo no encontrado.")

  py_lexer = lex.Lexer(texto_archivo)
  py_lexer.read_file()

  
if __name__ == '__main__':
  main()
