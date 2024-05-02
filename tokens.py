

tokens = {
  '=' : 'tk_asig',
  '+' : 'tk_suma',
  '-' : 'tk_resta',
  '/' : 'tk_div',
  '*' : 'tk_mult',
  '<' : 'tk_menor_que',
  '>' : 'tk_mayor_que',
  '!': 'tk_dif' , 
  '%': 'tk_mod', 
  '{': 'tk_cor_izq',
  '}' : 'tk_cor_der',
  '(' : 'tk_par_izq',
  ')': 'tk_par_der', 
  ',': 'tk_coma',
  ';': 'tk_punto_coma',
  ':': 'tk_dos_puntos', 
  '.': 'tk_punto', 
  '&': 'tk_dir',
  '|': 'tk_or_bit',
  '+=': 'tk_aum', 
  '-=': 'tk_decre', 
  '>=': 'tk_mayor_igual', 
  '<=': 'tk_menor_igual',
  '[': 'tk_parc_izq',
  ']': 'tk_parc_der',
  '&&': 'tk_y',
  '||': 'tk_o', 
  '==': 'tk_comparacion',
  '!=': 'tk_distinto',
  '->': 'tk_ejecuta'
}


class TokenizedCode: 
  def __init__(self, tk) -> None:
    self.raw_tokens = tk
    self.tokens = [] 

  def raw_to_token(self):
    for raw_token in self.raw_tokens:
      raw_token = raw_token.replace("<", "").replace(">", "").replace(" ", "")
      obj = raw_token.split(",")
      if len(obj) == 4:
        self.tokens.append(TokenObject(obj[0], int(obj[2]), int(obj[3]), obj[1]))
      elif len(obj) == 3:
        self.tokens.append(TokenObject(obj[0], int(obj[1]), int(obj[2])))
    
    return self.tokens



class TokenObject:
  def __init__(self, name, line, pos, lexema = None) -> None:
    self.name = name
    self.line = line
    self.pos = pos
    self.lexema = lexema
