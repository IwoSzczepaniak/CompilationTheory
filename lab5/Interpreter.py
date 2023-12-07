import sys
sys.path.append('c:/Users/iwosz/PythonProjects/CompilationTheory/') 

from lab3.MyParserAST import *
from lab4.SymbolTable import SymbolTable
from lab5.visit import *
from lab5.Memory import *
from lab5.Exceptions import *
import numpy as np

sys.setrecursionlimit(10000)

class Interpreter(object):
    def dot_mult(self, x, y):
        if isinstance(x, list) and isinstance(y, list):
            if isinstance(x[0], list) and isinstance(y[0], list):
                return [[sum(a * b for a, b in zip(row, col)) for col in zip(*y)] for row in x]
            elif isinstance(x[0], list):
                return [[sum(a * b for a, b in zip(row, y)) for row in x]]
            elif isinstance(y[0], list):
                return [[sum(a * b for a, b in zip(x, col))] for col in zip(*y)]
            
    def dot_op(self, x, y, op):
        n = len(x)
        if not isinstance(x[0], list): return
        m = len(x[0])
        if n == len(y):
            if m == len(y[0]):
                return [[self.operations[op](x[row][col], y[row][col]) for col in range(m)] for row in range(n)]
            

    def __init__(self):
        super().__init__()

        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '<': lambda x, y: x < y,
            '>': lambda x, y: x > y,
            '<=': lambda x, y: x <= y,
            '>=': lambda x, y: x >= y,
            '==': lambda x, y: x == y,
            '!=': lambda x, y: x != y,
            '.+': lambda x, y: self.dot_op(x, y, "+"),
            '.-': lambda x, y: self.dot_op(x, y, "-"),
            '.*': lambda x, y: self.dot_mult(x, y),
            './': lambda x, y: self.dot_mult(x, np.linalg.inv(y).tolist())
        }        


    @on('node')
    def visit(self, node):
        pass

    @when(InstructionsOrEmpty)
    def visit(self, node: Instructions):
        self.memory = MemoryStack()
        self.memory.push('global')
        node.instructions.accept(self)

    @when(Instructions)
    def visit(self, node: Instructions):
        for instruction in node.instructions:
            instruction.accept(self)

    @when(BinaryExpression)
    def visit(self, node: BinaryExpression):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)

        return self.operations[node.op](r1, r2)

    @when(UnaryExpression)
    def visit(self, node: UnaryExpression):
        r1 = node.expr.accept(self)
        if node.operation == "TRANSPOSE":
            return zip(*r1)
        else:
            return [[-x for x in row] for row in r1]

    @when(Id)
    def visit(self, node: Id):

        return self.memory.get(node.id)

    @when(IntNum)
    def visit(self, node: IntNum):
        return int(node.intnum)

    @when(Float)
    def visit(self, node: Float):
        return float(node.floatnum)

    @when(StringLiteral)
    def visit(self, node: StringLiteral):
        return str(node.string)

    @when(IfStatement)
    def visit(self, node: IfStatement):
        condition = node.cond.accept(self)
        if condition:
            self.memory.push('if')
            if isinstance(node.if_body, Instructions):
                node.if_body.accept(self)
            else:
                for instruction in node.if_body:
                    instruction.accept(self)
            self.memory.pop()
        else:
            if node.else_body is not None:
                self.memory.push('else')
                node.else_body.accept(self)
                self.memory.pop()

    @when(WhileLoop)
    def visit(self, node: WhileLoop):
        self.memory.push("while")
        while node.cond.accept(self):
            try:
                if isinstance(node.body, list):
                    for instruction in node.body:
                        instruction.accept(self)
                else:
                    node.body.accept(self)
            except ContinueException:
                continue
            except BreakException:
                break
        self.memory.pop()

    @when(ForLoop)
    def visit(self, node: ForLoop):
        iterator = node.id
        start = node.cond_start.accept(self)
        end = node.cond_end.accept(self)
        self.memory.push("for")
        self.memory.set(iterator.id, start)
        while self.memory.get(iterator.id) <= end:
            try:
                if isinstance(node.body, list):
                    for instruction in node.body:
                        instruction.accept(self)
                else:
                    node.body.accept(self)
            except ContinueException:
                continue
            except BreakException:
                break
            finally:
                self.memory.set(iterator.id, self.memory.get(iterator.id) + 1)
        self.memory.pop()

    @when(ReturnStatement)
    def visit(self, node: ReturnStatement):
        raise ReturnValueException(node.expr.accept(self))

    @when(BreakStatement)
    def visit(self, node: BreakStatement):
        raise BreakException()

    @when(ContinueStatement)
    def visit(self, node: ContinueStatement):
        raise ContinueException

    @when(PrintStatement)
    def visit(self, node: PrintStatement):
        to_print = [element.accept(self) for element in node.printargs]
        print(*to_print, sep=' ')

    @when(Assignment)
    def visit(self, node: Assignment):
        if not isinstance(node.left, Variable):
            if node.op == '=':
                self.memory.set(node.left.id, node.right.accept(self))
            else:
                self.memory.set(node.left.id, self.operations[node.op[0]](self.memory.get(node.left.id), node.right.accept(self)))
        else:
            matrix = self.memory.get(node.left.id.id)
            if isinstance(node.left.index[0], tuple):
                x = [i for i in range(node.left.index[0][0].accept(self), node.left.index[0][1].accept(self))]
            else:
                x = [node.left.index[0].accept(self)]
            if isinstance(node.left.index[1], tuple):
                y = [i for i in range(node.left.index[1][0].accept(self), node.left.index[1][1].accept(self))]
            else:
                y = [node.left.index[1].accept(self)]
            if node.op == '=':
                for i in x:
                    for j in y:
                        matrix[j][i] = node.right.accept(self)
            else:
                for i in x:
                    for j in y:
                        matrix[j][i] = self.operations[node.op[0]](matrix[j][i], node.right.accept(self))

            self.memory.set(node.left.id.id, matrix)

    @when(Vector)
    def visit(self, node: Vector):
        return [element.accept(self) for element in node.vector]

    @when(Matrix)
    def visit(self, node: Variable):
        matrix = self.memory.get(node.id.id)

        x = node.index[0].accept(self)
        y = node.index[1].accept(self)

        return matrix[x][y]

    @when(MatFun)
    def visit(self, node: MatFun):
        func = node.func
        args = [dim.accept(self) for dim in node.dims]
        if func == 'zeros':
            if len(args) == 2:
                return [[0 for _ in range(args[0])] for _ in range(args[1])]
            else:
                return [0 for _ in range(args[0])]
        elif func == 'ones':
            if len(args) == 2:
                return [[1 for _ in range(args[0])] for _ in range(args[1])]
            else:
                return [1 for _ in range(args[0])]
        elif func == 'eye':
            if len(args) == 2:
                return [[1 if i == j else 0 for i in range(args[0])] for j in range(args[0])]
            else:
                return [1 for _ in range(args[0])]


