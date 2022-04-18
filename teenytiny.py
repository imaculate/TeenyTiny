from lex import *
from parse import *
import sys

def main():
    print("Teeny Tiny Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")

    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()
    

    # input = "LET foobar = 123"
    # input = "+- 23 9.8654 foo*THEN # This is a comment!\n+- */ >>= = !="
    lexer = Lexer(input)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program()
    emitter.writeFile()
    print("Compiling completed.")

    """token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()"""

main()