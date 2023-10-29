from MyLexer import MyLexer as Scanner
from MyParser import ParserMatrix

for n in [1,2,3]:
    filename = f"tests/example{n}.m"
    with open(filename, 'r') as f:
        data = f.read()
    parser = ParserMatrix()
    parser.parse(Scanner().tokenize(data))