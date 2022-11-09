import SymbolTable
import Symbols
import Scanner


def test():
    st = SymbolTable.SymbolTable(13)
    st.add('a')
    st.add('test')
    st.to_string()


def test_classifier():
    symbols = Symbols.Symbols()
    symbols.print_symbols()


def test_scanner():
    scanner = Scanner.Scanner()
    scanner.read_from_file("p3.txt")
    scanner.print_symbols()


if __name__ == '__main__':
    test_scanner()
