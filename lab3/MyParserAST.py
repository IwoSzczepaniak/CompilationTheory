from sly import Parser
import sys
sys.path.append('c:/Users/iwosz/PythonProjects/CompilationTheory/') 
from lab1.MyLexer import MyLexer as Scanner
from AST import *

class ParserMatrixAST(Parser):

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
        return InstructionsOrEmpty(p[0])

    @_('instructions')
    def instructions_or_empty(self, p):
        return Instructions(p[0])

    @_('')
    def instructions_or_empty(self, p):
        return Instructions()

    @_('instructions instruction',
       'instruction')
    def instructions(self, p):
        return p[0] + p[1] if len(p) == 2 else p[0]

    @_('if_i',
       'return_i ";"',
       'BREAK ";"',
       'CONTINUE ";"',
       'for_l',
       'while_l',
       'assign ";"',
       'print_i ";"')
    def instruction(self, p):
        return [p[0]]
    
    @_('"{" instructions "}"')
    def instruction(self, p):
        return p[1]

    @_('IF "(" expr ")" instruction %prec IFX',
       'IF "(" expr ")" instruction ELSE instruction')
    def if_i(self, p):
        return IfStatement(p[2], Instructions(p[4])) if len(p) == 5 else IfStatement(p[2], Instructions(p[4]), Instructions(p[6]))

    @_('WHILE "(" expr ")" instruction' )
    def while_l(self, p):
        return WhileLoop(p[2], Instructions(p[4]))

    @_('FOR ID "=" expr ":" expr instruction')
    def for_l(self, p):
        return ForLoop(Id(p[1]), p[3], p[5], Instructions(p[6]))

    @_('RETURN',
       'RETURN expr')
    def return_i(self, p):
        return ReturnStatement(p[1]) if len(p) == 2 else ReturnStatement()

    @_('PRINT printargs')
    def print_i(self, p):
        return PrintStatement(p[1])

    @_('expr "," printargs',
        'expr')
    def printargs(self, p):
        return [p[0]] + p[2] if len(p) == 3 else [p[0]]

    @_('STRING')
    def expr(self, p):
        return StringLiteral(p[0])

    @_('INTNUM')
    def expr(self, p):
        return IntNum(p[0])

    @_('FLOAT')
    def expr(self, p):
        return Float(p[0])

    @_('var')
    def expr(self, p):
        return p[0]
    @_('"(" expr ")"')
    def expr(self, p):
        return p[1]

    @_('arg')
    def var(self, p):
        return p[0]

    @_('ID')
    def var(self, p):
        return Id(p[0])

    @_('ID "[" expr "," expr "]"')
    def arg(self, p):
        return Variable(Id(p[0]), (p[2], p[4]))

    @_('var "=" expr',
       'var ADDASSIGN expr',
       'var SUBASSIGN expr',
       'var MULASSIGN expr',
       'var DIVASSIGN expr')
    def assign(self, p):
        return Assignment(p[0], p[1], p[2])

    @_('"-" expr %prec UMINUS',
        '''expr "'" %prec TRANSPOSE''')
    def expr(self, p):
        return UnaryExpression(p[1], p[0])

    @_('matrix')
    def expr(self, p):
        return p[0]

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
        return BinaryExpression(p[0], p[1], p[2])



    @_('"[" vectors "]"')
    def matrix(self, p):
        return Matrix(p[1])

    @_('vectors "," vector',
       'vector')
    def vectors(self, p):
        return p[0] + [p[2]] if len(p) == 3 else [p[0]]

    @_('"[" variables "]"')
    def vector(self, p):
        return p[1]


    @_('variables "," variable',
       'variable')
    def variables(self, p):
        return  p[0] + [p[2]] if len(p) == 3 else [p[0]]

    @_('expr')
    def variable(self, p):
        return p[0]


    @_('mat_fun "(" expr ")"')
    def expr(self, p):
        return MatFun(p[0], p[2])


    @_('ZEROS',
       'EYE',
       'ONES')
    def mat_fun(self, p):
        return p[0]


    def error(self, p):
        if p:
            print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        else:
            print("Unexpected end of input")


