from lex import *

def main():
    # input = "LET foobar = 123"
    input = "+- 23 9.8654 foo*THEN # This is a comment!\n+- */ >>= = !="
    lexer = Lexer(input)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()
main()