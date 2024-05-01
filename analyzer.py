import lexer as lex, sys
import grammar as g



class Parser:
   def __init__(self, tokens, gramatica):
      self.tokens = tokens
      self.grammar = gramatica
  
    
    




def main():
  if len(sys.argv) < 2: 
    sys.exit(1)
  try:
      texto_archivo = open(sys.argv[1], "r")
  except FileNotFoundError:
      sys.exit("Error: Archivo no encontrado.")

  py_lexer = lex.Lexer(texto_archivo)
  py_lexer.read_file()
  for tk in py_lexer.get_tokenized():
     print("Name:", tk.name, "Lex:", tk.lexema, "Line:", tk.line, "Pos:", tk.pos)
  py_parser = Parser(py_lexer.tokens, g.gramatica_python)

  
if __name__ == '__main__':
  main()
