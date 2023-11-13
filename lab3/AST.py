class Node:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def indentation(self, i):
        print(i * "|\t", end="")


class InstructionsOrEmpty(Node):
    def __init__(self, instructions=None):
        super().__init__(instructions=instructions)
    def printTree(self, i=0):
        self.instructions.printTree(i)

class Instructions(Node):
    def __init__(self, instructions):
        super().__init__(instructions=instructions)
    def printTree(self, i=0):
        for instruction in self.instructions:
            instruction.printTree(i)


class IfStatement(Node):
    def __init__(self, cond, if_body, else_body=None):
        super().__init__(cond=cond, if_body=if_body, else_body=else_body)
    def printTree(self, i):
        self.indentation(i)
        print("IF")
        self.cond.printTree(i+1)
        self.indentation(i)
        print("THEN")
        self.if_body.printTree(i+1)
        if self.else_body is not None:
            self.indentation(i)
            print("ELSE")
            self.else_body.printTree(i+1)

class ReturnStatement(Node):
    def __init__(self, expr=None):
        super().__init__(expr=expr)
    def printTree(self, i):
        self.indentation(i)
        print("RETURN")
        if self.expr is not None:
            self.expr.printTree(i+1)

class BreakStatement(Node):
    def printTree(self, i):
        self.indentation(i)
        print("BREAK")

class ContinueStatement(Node):
    def printTree(self, indent):
        self.indentation(i)
        print("CONTINUE")

class ForLoop(Node):
    def __init__(self, id, cond_start, cond_end, body):
        super().__init__(id=id, cond_start=cond_start, cond_end=cond_end, body=body)
    def printTree(self, i):
        self.indentation(i)
        print("FOR")
        self.id.printTree(i+1)
        self.indentation(i+1)
        print("RANGE")
        self.cond_start.printTree(i+2)
        self.cond_end.printTree(i+2)
        self.body.printTree(i+1)

class WhileLoop(Node):
    def __init__(self, cond, body):
        super().__init__(cond=cond, body=body)
    def printTree(self, i):
        self.indentation(i)
        print("WHILE")
        self.cond.printTree(i+1)
        self.body.printTree(i+1)

class Assignment(Node):
    def __init__(self, left, op, right):
        super().__init__(left=left, op=op, right=right)
    def printTree(self, i):
        self.indentation(i)
        self.left.printTree(i)
        self.indentation(i+1)
        print(self.op)
        self.right.printTree(i+2)

class PrintStatement(Node):
    def __init__(self, printargs):
        super().__init__(printargs=printargs)
    def printTree(self, i):
        self.indentation(i)
        print("PRINT")
        for printarg in self.printargs:
            printarg.printTree(i+1)


class StringLiteral(Node):
    def __init__(self, string):
        super().__init__(string=string)
    def printTree(self, i):
        self.indentation(i)
        print("STRING")
        self.indentation(i+1)
        print(self.string)

class IntNum(Node):
    def __init__(self, intnum):
        super().__init__(intnum=intnum)
    def printTree(self, i ):
        self.indentation(i)
        print(self.intnum)

class Float(Node):
    def __init__(self, floatnum):
        super().__init__(floatnum=floatnum)
    def printTree(self, i ):
        self.indentation(i)
        print("FLOAT")
        self.indentation(i+1)
        print(self.floatnum)

class Variable(Node):
    def __init__(self, id, index=None):
        super().__init__(id=id, index=index)
    def printTree(self, i):
        if self.index is not None:
            self.indentation(i)
            print("REF")
            self.id.printTree(i+1)
            for e in self.index:
                e.printTree(i+1)

class Id(Node):
    def __init__(self, id):
        super().__init__(id=id)
    def printTree(self, i):
        self.indentation(i)
        print(self.id)

class BinaryExpression(Node):
    def __init__(self, left, op, right):
        super().__init__(left=left, op=op, right=right)
    def printTree(self, i):
        self.left.printTree(i)
        self.indentation(i+1)
        print(self.op)
        self.right.printTree(i+2)

class Matrix(Node):
    def __init__(self, matrix):
        super().__init__(matrix=matrix)
    def printTree(self, i):
        self.indentation(i)
        print("VECTOR")
        for row in self.matrix:
            self.indentation(i + 1)
            print("VECTOR")
            for expr in row:
                expr.printTree(i+2)

class MatFun(Node):
    def __init__(self, func, expr):
        super().__init__(func=func, expr=expr)
    def printTree(self, i):
        self.indentation(i)
        print(self.func)
        self.expr.printTree(i+1)

class UnaryExpression(Node):
    def __init__(self, operation, expr):
        super().__init__(operation=operation, expr=expr)
    def printTree(self, i):
        self.indentation(i)
        print(self.operation)
        self.expr.printTree(i+1)