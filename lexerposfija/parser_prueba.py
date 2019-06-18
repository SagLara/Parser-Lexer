import lexer_rules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc

lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)

f= open('operaciones.txt','r')
o=f.read()
f.close()

op=o.splitlines()
cont=0
while(cont<len(op)):
    print(parser.parse(op[cont], lexer))
    cont+=1


