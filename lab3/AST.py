class Node:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def indentation(self, i):
        print(i * "|\t", end="")
    
    def accept(self, visitor):
        return visitor.visit(self)


class InstructionsOrEmpty(Node):
    def __init__(self, instructions=None, lineno=None):
        super().__init__(instructions=instructions, lineno=lineno)


class Instructions(Node):
    def __init__(self, instructions, lineno=None):
        super().__init__(instructions=instructions, lineno=lineno)


class IfStatement(Node):
    def __init__(self, cond, if_body, else_body=None, lineno=None):
        super().__init__(cond=cond, if_body=if_body, else_body=else_body, lineno=lineno)


class ReturnStatement(Node):
    def __init__(self, expr=None, lineno=None):
        super().__init__(expr=expr, lineno=lineno)


class BreakStatement(Node):
    def __init__(self, lineno=None):
        super().__init__(lineno=lineno)


class ContinueStatement(Node):
    def __init__(self, lineno=None):
        super().__init__(lineno=lineno)


class ForLoop(Node):
    def __init__(self, id, cond_start, cond_end, body, lineno=None):
        super().__init__(id=id, cond_start=cond_start, cond_end=cond_end, body=body, lineno=lineno)


class WhileLoop(Node):
    def __init__(self, cond, body, lineno=None):
        super().__init__(cond=cond, body=body, lineno=lineno)


class Assignment(Node):
    def __init__(self, left, op, right, lineno=None):
        super().__init__(left=left, op=op, right=right, lineno=lineno)


class PrintStatement(Node):
    def __init__(self, printargs, lineno=None):
        super().__init__(printargs=printargs, lineno=lineno)


class StringLiteral(Node):
    def __init__(self, string, lineno=None):
        super().__init__(string=string, lineno=lineno)


class IntNum(Node):
    def __init__(self, intnum, lineno=None):
        super().__init__(intnum=intnum, lineno=lineno)


class Float(Node):
    def __init__(self, floatnum, lineno=None):
        super().__init__(floatnum=floatnum, lineno=lineno)


class Variable(Node):
    def __init__(self, id, index=None, lineno=None):
        super().__init__(id=id, index=index, lineno=lineno)


class Id(Node):
    def __init__(self, id, lineno=None):
        super().__init__(id=id, lineno=lineno)


class BinaryExpression(Node):
    def __init__(self, left, op, right, lineno=None):
        super().__init__(left=left, op=op, right=right, lineno=lineno)


class Matrix(Node):
    def __init__(self, matrix, lineno=None):
        super().__init__(matrix=matrix, lineno=lineno)


class MatFun(Node):
    def __init__(self, func, dims, v_type='int', lineno=None):
        super().__init__(func=func, dims=dims, v_type=v_type, lineno=lineno)


class UnaryExpression(Node):
    def __init__(self, operation, expr, lineno=None):
        super().__init__(operation=operation, expr=expr, lineno=lineno)


class Vector(Node):
    def __init__(self, vector, lineno=None):
        self.vector = vector
        self.lineno = lineno
        self.dims = [len(vector)]
        self.v_type = None

        if isinstance(vector[0], Vector):
            self.dims += vector[0].dims
        elif isinstance(vector[0], list):
            self.dims += [len(vector[0])]

        cd = vector
        while isinstance(cd, list) or isinstance(cd, Vector):
            if isinstance(cd, list):
                cd = cd[0]
            else:
                cd = cd.vector[0]

        if isinstance(cd, IntNum):
            self.v_type = 'int'
        if isinstance(cd, Float):
            self.v_type = 'float'
        if isinstance(cd, StringLiteral):
            self.v_type = 'str'
