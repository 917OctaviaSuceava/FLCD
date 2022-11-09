
class Symbols:
    def __init__(self):
        self.separators = []
        self.operators = []
        self.reserved_words = []
        self.classify_symbols()

    def classify_symbols(self):
        f = open("token.in", "r")
        counter = 0
        for line in f:
            if counter <= 11:
                self.separators.append(line.strip())
            if 12 <= counter <= 23:
                self.operators.append(line.strip())
            if counter > 23:
                self.reserved_words.append(line.strip())
            counter += 1

    def print_symbols(self):
        print("SEPARATORS:  ", self.separators)
        print("-----")
        print("OPERATORS:  ", self.operators)
        print("-----")
        print("RESERVED WORDS:  ", self.reserved_words)
