from sly import Lexer

class MyLexer(Lexer):
    literals = { '+','-','*','/', "=", ";", ":", ",","(", ")", "'", "{", "}", "[", "]"}
    
    tokens = [
        # Macierzowe operatory binarne
        DOTADD, DOTSUB, DOTMUL, DOTDIV,
        # Operatory przypisania
        ADDASSIGN, SUBASSIGN, MULASSIGN, DIVASSIGN,
        # Operatory relacyjne
        LT, GT, LE, GE, NE, EQ,  
        # Słowa kluczowe
        IF, ELSE, FOR, WHILE,
        BREAK, CONTINUE, RETURN,
        EYE, ZEROS, ONES,
        PRINT,
        ID, INTNUM, FLOAT, STRING  # Identyfikatory, liczby, stringi
    ]


    ignore = ' \t'
    # \n jest również ignorowane, ale uwzględnione osobno, by liczyć linie

    @_(r'#.*')
    def ignore_comment(self, t):
        pass

    DOTADD = r'\.\+'
    DOTSUB = r'\.-'
    DOTMUL = r'\.\*'
    DOTDIV = r'\./'
    ADDASSIGN = r'\+='
    SUBASSIGN = r'-='
    MULASSIGN = r'\*='
    DIVASSIGN = r'/='
    LE = r'<='
    GE = r'>='
    NE = r'!='
    EQ = r'=='
    LT = r'<'
    GT = r'>'

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    ID['if'] = IF
    ID['else'] = ELSE
    ID['for'] = FOR
    ID['while'] = WHILE
    ID['break'] = BREAK
    ID['continue'] = CONTINUE
    ID['return'] = RETURN
    ID['eye'] = EYE
    ID['zeros'] = ZEROS
    ID['ones'] = ONES
    ID['print'] = PRINT


    @_(r'((\d+\.\d*)|(\.\d+))([eE][-+]?\d+)?')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def INTNUM(self, t):
        t.value = int(t.value)
        return t

    @_(r'"[^"]*"')
    def STRING(self, t):
        t.value = t.value[1:-1] 
        return t
    
    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')


    def error(self, t):
        print(f'Incorrect sign: {t.value[0]} in line: {self.lineno}')
        self.index += 1