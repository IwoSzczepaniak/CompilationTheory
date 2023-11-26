from __future__ import print_function
import sys
sys.path.append('c:/Users/iwosz/PythonProjects/CompilationTheory/') 
import lab3.AST as AST

def addToClass(cls):
    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(AST.InstructionsOrEmpty)
    def printTree(self, i=0):
        self.instructions.printTree(i)


    @addToClass(AST.Instructions)
    def printTree(self, i=0):
        for instruction in self.instructions:
            instruction.printTree(i)

    @addToClass(AST.IfStatement)
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

    @addToClass(AST.ReturnStatement)
    def printTree(self, i):
        self.indentation(i)
        print("RETURN")
        if self.expr is not None:
            self.expr.printTree(i+1)

    @addToClass(AST.BreakStatement)
    def printTree(self, i):
        self.indentation(i)
        print("BREAK")
    
    @addToClass(AST.ContinueStatement)
    def printTree(self, i):
        self.indentation(i)
        print("CONTINUE")

    @addToClass(AST.ForLoop)
    def printTree(self, i):
        self.indentation(i)
        print("FOR")
        self.id.printTree(i+1)
        self.indentation(i+1)
        print("RANGE")
        self.cond_start.printTree(i+2)
        self.cond_end.printTree(i+2)
        self.body.printTree(i+1)
    
    @addToClass(AST.WhileLoop)
    def printTree(self, i):
        self.indentation(i)
        print("WHILE")
        self.cond.printTree(i+1)
        self.body.printTree(i+1)

    @addToClass(AST.Assignment)
    def printTree(self, i):
        self.indentation(i)
        self.left.printTree(i)
        self.indentation(i+1)
        print(self.op)
        self.right.printTree(i+2)    

    @addToClass(AST.PrintStatement)
    def printTree(self, i):
        self.indentation(i)
        print("PRINT")
        for printarg in self.printargs:
            printarg.printTree(i+1)
    
    @addToClass(AST.StringLiteral)
    def printTree(self, i):
        self.indentation(i)
        print("STRING")
        self.indentation(i+1)
        print(self.string)

    @addToClass(AST.IntNum)
    def printTree(self, i ):
        self.indentation(i)
        print(self.intnum)

    @addToClass(AST.Float)
    def printTree(self, i ):
        self.indentation(i)
        print("FLOAT")
        self.indentation(i+1)
        print(self.floatnum)

    @addToClass(AST.Variable)
    def printTree(self, i):
        if self.index is not None:
            self.indentation(i)
            print("REF")
            self.id.printTree(i+1)
            for e in self.index:
                e.printTree(i+1)
    
    @addToClass(AST.Id)
    def printTree(self, i):
        self.indentation(i)
        print(self.id)

    @addToClass(AST.BinaryExpression)
    def printTree(self, i):
        self.left.printTree(i)
        self.indentation(i+1)
        print(self.op)
        self.right.printTree(i+2)

    @addToClass(AST.Matrix)
    def printTree(self, i):
        self.indentation(i)
        print("VECTOR")
        for row in self.matrix:
            self.indentation(i + 1)
            print("VECTOR")
            for expr in row:
                expr.printTree(i+2)

    @addToClass(AST.MatFun)
    def printTree(self, i):
        self.indentation(i)
        print(self.func)
        for dim in self.dims:
            dim.printTree(i+1)

    @addToClass(AST.UnaryExpression)
    def printTree(self, i):
        self.indentation(i)
        print(self.operation)
        self.expr.printTree(i+1)
    
    @addToClass(AST.Vector)
    def printTree(self, i):
        self.indentation(i)
        print("VECTOR")
        for expr in self.vector:
            expr.printTree(i + 1)