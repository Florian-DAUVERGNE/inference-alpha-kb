from ply import lex
from ply import yacc

"""
Definition de la grammaire et des tokens pour l'analyseur syntaxique
"""

tokens = (
    'ATOM',
    'NOT', 'AND', 'OR', 'IF', 'THEN', 'ELSE', 'IFF',
    'LPAREN', 'RPAREN',
)

t_ATOM = r'[a-zA-Z_0-9][a-zA-Z_0-9]*'
t_NOT = r'¬'
t_AND = r'∧'
t_OR = r'∨'
t_THEN = r'→'
t_IFF = r'↔'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t\n'


def p_expression_atom(p):
    'expression : ATOM'
    p[0] = p[1]


def p_expression_not(p):
    'expression : NOT expression'
    p[0] = ('NOT', p[2])


def p_expression_and(p):
    'expression : expression AND expression'
    p[0] = ('AND', p[1], p[3])


def p_expression_or(p):
    'expression : expression OR expression'
    p[0] = ('OR', p[1], p[3])


def p_expression_iff(p):
    'expression : expression IFF expression'
    p[0] = ('IFF', p[1], p[3])


def p_expression_then(p):
    'expression : expression THEN expression'
    p[0] = ('IF', p[2], p[3])


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_error(p):
    p[0] = "ERROR"


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")


parser = yacc.yacc()
lexer = lex.lex()
