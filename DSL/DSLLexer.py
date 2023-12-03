import ply.lex as lex

# Reserved Tokens
reserved = {
    'contains' : 'CONTAIN',
    'connects_to' : 'CONNECT',
    'throws' : 'THROW',
}

# List of token names.
tokens = ["VAR", "TYPE", "DEFINE"] + list(reserved.values())


# Regular expression rules for simple tokens
t_DEFINE = r"="

def t_TYPE(t):
    r"AZDT|Ditto"
    return t
    
def t_VAR(t):
    r"\w+(\.\w+)*"
    t.type = reserved.get(t.value, "VAR")
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = " \t"

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


##########################################################

# Test it out
data = '''
twinB.low_battery throws twinA.power_save
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
