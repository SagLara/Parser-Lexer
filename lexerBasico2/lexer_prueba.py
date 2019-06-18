import lexer_rules
from ply.lex import lex

lexer = lex(module=lexer_rules)

f= open('operaciones.txt','r')
o=f.read()
f.close()
op=o.splitlines()
cont=0

while(cont<len(op)):
    lexer.input(op[cont])
    token = lexer.token()
    while token is not None:
        print token.type, token.value
        token = lexer.token()
    cont+=1
 
