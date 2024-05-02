import lexer as lex, sys
import grammar as g
from keywords import keywords as kwd
from tokens import tokens as tkn_symbols



class Parser:
  def __init__(self, tokens, gramatica):
    self.tokens = tokens
    self.grammar = gramatica
    self.current_block_column = 0
    self.last_token_to_del = None
  

  def error(self, line, pos, msg = ''):
    print('<'+ str(line) + ','+ str(pos)+'>', 'Error sintactico: '+ msg)
    sys.exit()

  def parse(self):
    return self.parsing(self.tokens)

  def parsing(self, tokens_remaining):
    print("Tokens", [tk.name for tk in tokens_remaining])
    if len(tokens_remaining) == 0: 
      return print("El analisis sintactico ha finalizado exitosamente.")
      
    
    token = tokens_remaining[0]
    current_rule = token.name.upper() 
    
    if current_rule in self.grammar:
      if current_rule == "CLASS":
        self.parse_class(tokens_remaining)
      elif current_rule == "ID":
        self.parse_id(tokens_remaining)
      elif current_rule == "IMPORT":
        self.parse_import(tokens_remaining)
      elif current_rule == "FROM":
        self.parse_from(tokens_remaining)
      elif current_rule == "IF":
        self.parse_if(tokens_remaining)
      elif current_rule == "FOR":
        self.parse_for(tokens_remaining)
      elif current_rule == "WHILE":
        self.parse_while(tokens_remaining)
      elif current_rule == "PRINT":
        self.parse_print(tokens_remaining)
      elif current_rule == "DEF":
        self.parse_id(tokens_remaining)
    else:
      return self.error(token.line, token.pos)
      

  def parse_class(self, tks_rem):
    block_indent = tks_rem[0].pos
    if self.validate_rule(tks_rem[0:3], g.get_rule('CLASS'), True):
      del tks_rem[0:3]
      if len(tks_rem) >= 1:
        start_indent = tks_rem[0].pos
        content = []
        if start_indent > block_indent:
          for tk in tks_rem[:]:
            if tk.pos >= start_indent:
              content.append(tk)
              tks_rem.remove(tk)
            else: break
          if self.parse_content(content):
            self.parsing(tks_rem)
        else:
          self.error(tks_rem[3].line, start_indent, "falla de identacion")



  def parse_id(self, tks_rem):
    if self.validate_rule(tks_rem, g.get_rule('ID'), True, True):
      self.parsing(self.delete_tokens(tks_rem))


  def parse_import(self, tks_rem):
    if self.validate_rule(tks_rem, g.get_rule('IMPORT'), True, True):
      self.parsing(self.delete_tokens(tks_rem))

  def parse_from(self, tks_rem):
    if self.validate_rule(tks_rem, g.get_rule('FROM'), True, True):
      self.parsing(self.delete_tokens(tks_rem))

  def parse_if(self, tks_rem):
    if self.validate_rule(tks_rem, g.get_rule('IF'), True, True):
      self.parsing(self.delete_tokens(tks_rem))

  def parse_for(self, tks_rem):
    if self.validate_rule(tks_rem, g.get_rule('FOR'), True, True):
      self.parsing(self.delete_tokens(tks_rem))

  def parse_while(self, tks_rem):
    if self.validate_rule(tks_rem, g.get_rule('WHILE'), True, True):
      self.parsing(self.delete_tokens(tks_rem))

  def parse_print(self, tks_rem):
    if self.validate_rule(tks_rem, g.get_rule('PRINT'), True, True):
      self.parsing(self.delete_tokens(tks_rem))

  def parse_def(self, tks_rem):
    if self.validate_rule(tks_rem, g.get_rule('DEF'), True, True):
      self.parsing(self.delete_tokens(tks_rem))

  def parse_content(self, tks_cont):
    return True

  def validate_rule(self, tks_rem, rules, same_line = False, check_last_token = False):
    current_line = tks_rem[0].line
    last_pos = (1, 1)
    last_error = []
    last_token = None
    valid = True
    for rule in rules:
      rule_array = rule.split(" ")
      valid = True
      print("Rules: ", rule_array)
      for i, (token, valor) in enumerate(zip(tks_rem, rule_array)):
        last_token = token
        if(valor.isupper()):
          valid = self.validate_rule(tks_rem[i:], g.get_rule(valor), same_line, False)
        else: 
          print("Rule:", valor)
          print("Token: ", token.name, token.line, token.pos)
          if same_line and current_line != token.line:
            self.error(last_pos[0], last_pos[1], "Se encontro: ' '; Se esperaba: '"+str(self.token_symbol(valor))+"'.")
            valid = False

          if token.name != valor:
            last_error = [token.line, token.pos, "Se encontro: '"+str(self.token_symbol(token.name))+"'; Se esperaba: '"+str(self.token_symbol(valor))+"'."]
            valid = False
        
        last_pos = (token.line, token.pos)
      
      if valid:
        if len(tks_rem) >= len(rule_array):
          if check_last_token: self.last_token_to_del = last_token
          return True
        else: self.error(last_pos[0], last_pos[1], "Se encontro: ' '; Se esperaba: '"+str(self.token_symbol(rule_array[-1]))+"'.")

    if not valid:
      self.error(last_error[0], last_error[1], last_error[2])
    if check_last_token: self.last_token_to_del = last_token
    return False
  
  def token_symbol(self, token):
    if token in kwd:
      return token
    elif token.isupper():
      return "Valor"
    else:
      for clave, val in tkn_symbols.items():
        if val == token:
            return clave
    
        
  def delete_tokens(self, curr_tokens):
    if self.last_token_to_del != None:
      for tk in curr_tokens[:]:
        if tk != self.last_token_to_del:          
          curr_tokens.remove(tk)
        else:
          curr_tokens.remove(tk)
          self.last_token_to_del = None
          break
      return curr_tokens

    

       
    




def main():
  if len(sys.argv) < 2: 
    sys.exit(1)
  try:
      texto_archivo = open(sys.argv[1], "r")
  except FileNotFoundError:
      sys.exit("Error: Archivo no encontrado.")

  py_lexer = lex.Lexer(texto_archivo)
  py_lexer.read_file() 
  py_parser = Parser(py_lexer.get_tokenized(), g.gramatica_python)
  py_parser.parse()

  
if __name__ == '__main__':
  main()
