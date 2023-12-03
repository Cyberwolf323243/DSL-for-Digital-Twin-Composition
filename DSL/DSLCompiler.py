import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from BALexer import tokens

def p_expression_define(p):
    'expression : VAR DEFINE TYPE VAR'
    print("DT of", p[4], "is of type", p[3])
    p[0] = p[1]

def p_expression_contains(p):
    'expression : VAR CONTAIN VAR'
    print("DT of", p[1], "contains", p[3])

def p_expression_connects(p):
    'expression : VAR CONNECT VAR'
    print(p[1], "connects to", p[3])

def p_expression_throws(p):
    'expression : VAR THROW VAR'
    print(p[1], "throws event", p[3])
    
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('exec > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
