import SymbolTable
import Symbols
import re


class Scanner:
    def __init__(self):
        self.__operators = []
        self.__separators = []
        self.__reserved_words = []
        self.PIF = []
        self.ST = SymbolTable.SymbolTable(13)
        self.symbols = Symbols.Symbols()

    def check_if_identifier(self, token):
        return re.search('^[a-z]([a-zA-Z])*$', token) is not None

    def is_constant(self, token):
        return re.search('^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    def get_string_token_from_line(self, line, index):
        token = ''
        quotes = 0
        while index < len(line) and quotes < 2:
            if line[index] == '\'' or line[index] == '\"':
                quotes += 1
            token += line[index]
            index += 1
        return token, index

    def is_operator(self, c):
        for operator in self.symbols.operators:
            if c in operator:
                return True
        return False

    def get_operator_from_token(self, line, index):
        token = ''
        while index < len(line) and self.is_operator(line[index]):
            token += line[index]
            index += 1
        return token, index

    def get_tokens(self, line):
        token = ''
        tokens = []
        i = 0
        while i < len(line):
            if self.is_operator(line[i]):
                if token:
                    tokens.append(token)
                token, i = self.get_operator_from_token(line, i)
                tokens.append(token)
                token = ''
            elif line[i] == '\'' or line[i] == '\"':
                if token:
                    tokens.append(token)
                token, i = self.get_string_token_from_line(line, i)
                tokens.append(token)
                token = ''
            elif line[i] in self.symbols.separators or line[i] == ' ':
                if token:
                    tokens.append(token)
                token = line[i]
                i += 1
                tokens.append(token)
                token = ''
            else:
                token += line[i]
                i += 1
        if token:
            tokens.append(token)
        return tokens

    def read_from_file(self, file):
        f = open(file, "r")
        error = ""
        line_counter = 0
        for line in f:
            line_counter += 1
            tokens = self.get_tokens(line.strip())
            # print(tokens)
            for i in range(len(tokens)):
                if tokens[i][0] == "\'" and tokens[i][len(tokens[i]) - 1] == "\'":
                    self.PIF.append(("string", 0))
                elif tokens[i][0] == "\"" and tokens[i][len(tokens[i]) - 1] == "\"":
                    self.PIF.append(("string", 0))
                elif tokens[i] in self.symbols.reserved_words + self.symbols.separators + self.symbols.operators or \
                        tokens[i] == ' ':
                    if tokens[i] == ' ':
                        continue
                    self.PIF.append((tokens[i], 0))
                elif self.check_if_identifier(tokens[i]):
                    id1 = self.ST.add(tokens[i])
                    self.PIF.append(("id", id1))
                elif self.is_constant(tokens[i]):
                    const = self.ST.add(str(tokens[i]))
                    self.PIF.append(("const", const))
                else:
                    error += 'Lexical error at line ' + str(line_counter) + " -> " + tokens[i] + "\n"
        wpif = open("PIF.out", "a")
        wpif.write(self.PIF_string())
        wst = open("ST.out", "a")
        wst.write(str(self.ST))
        if error == '':
            print("The program is lexically correct!")
        else:
            print(error)

    def PIF_string(self):
        s = ""
        for i in self.PIF:
            s += str(i[0]) + "   " + str(i[1]) + '\n'
        return s

    def print_symbols(self):
        print("SEPARATORS:  ", self.symbols.separators)
        print("-----")
        print("OPERATORS:  ", self.symbols.operators)
        print("-----")
        print("RESERVED WORDS:  ", self.symbols.reserved_words)
