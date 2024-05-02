gramatica_python = {
  "CONTENT": ["CLASS", "ID", "IMPORT", "FROM", "IF", "FOR", "WHILE", "PRINT", "DEF", "PASS"],
  "CLASS": ["class id tk_dos_puntos"],
  "ID": ["id ASIGN VALOR_CON",  "id ASIGN VAR_SENTENCE"],
  "ASIGN": ["tk_asig", "tk_aum", "tk_decre"],
  "IMPORT": ["import id", "import id tk_punto id"],
  "FROM": ["from id IMPORT", "from id import tk_mult"],
  "IF": ["if IF_SENTENCE tk_dos_puntos", "if id tk_dos_puntos", "if not id tk_dos_puntos", "if True tk_dos_puntos", "if False tk_dos_puntos", "if id in id tk_dos_puntos"],
  "FOR": ["for id in id tk_dos_puntos", "for id in FUNCTION tk_dos_puntos"],
  "WHILE": ["while tk_par_izq IF_SENTENCE tk_par_der tk_dos_puntos", "while tk_par_izq id tk_par_der tk_dos_puntos"],
  "PRINT": ["print tk_par_izq PARAMS tk_par_der"],
  "DEF": ["def id tk_par_izq DEF_PARAMS tk_par_der tk_dos_puntos", "def id tk_par_izq DEF_PARAMS tk_par_der tk_ejecuta DATA_TYPE tk_dos_puntos"],

  "VAR_SENTENCE": ["OPERACIONES", "FUNCTION"],
  "OPERACIONES": ["VALOR_CON OPERADORES_ARIT OPERACIONES", "FUNCTION OPERADORES_ARIT OPERACIONES", "VALOR_CON", "FUNCTION"],
  "OPERADORES_ARIT": ["tk_suma", "tk_resta", "tk_div", "tk_mult", "tk_mod"],

  "IF_SENTENCE": ["CONDICION and IF_SENTENCE", "CONDICION or IF_SENTENCE", "CONDICION", "not IF_SENTENCE"],
  "CONDICION": ["VALOR_CON OPERADOR VALOR_CON", "FUNCTION"],
  "VALOR_CON": ["id", "tk_entero tk_punto tk_entero", "False", "True", "tk_cadena", "tk_entero"],
  "OPERADOR": ["tk_mayor_que", "tk_menor_que", "tk_distinto", "tk_comparacion", "tk_mayor_igual", "tk_menor_igual"],

  "OBJ_ARRAY": ["tk_parc_izq PARAMS tk_parc_der", "tk_parc_izq tk_parc_der", "tk_cor_izq tk_cor_der", "tk_cor_izq PARAMS tk_cor_der", "tk_par_izq PARAMS tk_par_der", "tk_par_izq tk_par_der"],

  "FUNCTION": ["id tk_par_izq PARAMS tk_par_der", "id tk_par_izq tk_par_der", "id tk_punto FUNCTION"],
  "PARAMS": ["FUNC_PARAMS", "FUNC_PARAMS tk_coma PARAMS"],
  "FUNC_PARAMS": ["VALOR_CON", "OBJ_ARRAY", "FUNCTION"],

  "DEF_PARAMS": ["id", "id tk_dos_puntos DATA_OBJ", "id tk_coma DEF_PARAMS", "id tk_dos_puntos DATA_OBJ tk_coma DEF_PARAMS"],
  "DATA_TYPE": ["str", "int", "bool", "float", "None", "id", "self"],
  "DATA_OBJ": ["tk_parc_izq DATA_TYPE tk_parc_der", "DATA_TYPE"]

}



def get_rule(rule):
  return gramatica_python[rule]