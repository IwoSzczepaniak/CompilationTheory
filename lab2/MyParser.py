from sly import Parser
import sys
sys.path.append('c:/Users/iwosz/PythonProjects/CompilationTheory/') 
from lab1.MyLexer import MyLexer as Scanner

class ParserMatrix(Parser):

    tokens = Scanner.tokens

    precedence = (
        ('right', 'IFX'),
        ('right', 'ELSE'),

        ('nonassoc', 'LT', 'GT', 'EQ', 'NE', 'GE', 'LE'),
        ('left', 'DOTADD', 'DOTSUB',  '+', '-'),
        ('left', 'DOTMUL', 'DOTDIV', '*', '/'),

        ('left', 'TRANSPOSE'),
        ('left', 'UMINUS'),
    )

    @_('instructions_or_empty')
    def program(self, p):
        return p

    @_('instructions')
    def instructions_or_empty(self, p):
        return p

    @_('')
    def instructions_or_empty(self, p):
        return p

    @_('instructions instruction',
       'instruction')
    def instructions(self, p):
        return p

    @_('if_i',
       'return_i ";"',
       'BREAK ";"',
       'CONTINUE ";"',
       'for_l',
       'while_l',
       'assign ";"',
       'print_i ";"',
       '"{" instructions "}"')
    def instruction(self, p):
        return p

    @_('IF "(" expr ")" instruction %prec IFX',
       'IF "(" expr ")" instruction ELSE instruction')
    def if_i(self, p):
        return p

    @_('WHILE "(" expr ")" instruction' )
    def while_l(self, p):
        return p

    @_('FOR ID "=" expr ":" expr instruction')
    def for_l(self, p):
        return p

    @_('RETURN',
       'RETURN expr')
    def return_i(self, p):
        return p

    @_('PRINT printargs')
    def print_i(self, p):
        return p

    @_('expr "," printargs',
       'expr')
    def printargs(self, p):
        return p


    @_('var',
       '"(" expr ")"',
       'INTNUM',
       'FLOAT',
       'STRING')
    def expr(self, p):
        return p

    @_('ID', 'lists')
    def var(self, p):
        return p

    @_('ID "[" expr "," expr "]"')
    def lists(self, p):
        return p

    @_('var "=" expr',
       'var ADDASSIGN expr',
       'var SUBASSIGN expr',
       'var MULASSIGN expr',
       'var DIVASSIGN expr')
    def assign(self, p):
        return p


    @_('"-" expr %prec UMINUS',
        '''expr "'" %prec TRANSPOSE''')
    def expr(self, p):
        return p  

    @_('expr "+" expr',
       'expr "-" expr',
       'expr "*" expr',
       'expr "/" expr',

       'expr EQ expr',
       'expr NE expr',
       'expr LT expr',
       'expr GT expr',
       'expr LE expr',
       'expr GE expr',

       'expr DOTMUL expr',
       'expr DOTDIV expr',
       'expr DOTADD expr',
       'expr DOTSUB expr',
       )
    def expr(self, p):
        return p

    @_('matrix')
    def expr(self, p):
        return p

    @_('"[" vectors "]"')
    def matrix(self, p):
        return p

    @_('vectors "," vector',
       'vector')
    def vectors(self, p):
        return p

    @_('"[" variables "]"')
    def vector(self, p):
        return p

    @_('variables "," variable',
       'variable')
    def variables(self, p):
        return p

    @_('expr')
    def variable(self, p):
        return p

    @_('mat_fun "(" expr ")"')
    def expr(self, p):
        return p

    @_('ZEROS',
       'EYE',
       'ONES')
    def mat_fun(self, p):
        return p

    def error(self, p):
        if p:
            print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        else:
            print("Unexpected end of input")


