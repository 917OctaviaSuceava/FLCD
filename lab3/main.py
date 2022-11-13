import FiniteAutomata
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
    scanner.read_from_file("perr.txt")
    scanner.print_symbols()


def test_FA():
    FA = FiniteAutomata.FiniteAutomata()
    print(FA.final_states)


def options_FA():
    print("Choose an option:\n"
          "     0 - exit\n"
          "     1 - see the initial state\n"
          "     2 - see the final states\n"
          "     3 - see the set of states\n"
          "     4 - see the alphabet\n"
          "     5 - see the transitions set\n"
          "     6 - see all\n"
          "     7 - check if a sequence is accepted by the FA\n")

def menu_FA():
    FA = FiniteAutomata.FiniteAutomata()
    while True:
        options_FA()
        option = int(input("Your option is:\n"))
        if option == 0:
            return
        elif option == 1:
            print(FA.initial_state)
        elif option == 2:
            print(FA.final_states)
        elif option == 3:
            print(FA.set_of_states)
        elif option == 4:
            print(FA.alphabet)
        elif option == 5:
            print(FA.dict_to_str())
        elif option == 6:
            print(FA.print_everything())
        elif option == 7:
            seq = input("Your sequence is:\n")
            if FA.check_sequence(seq) is True:
                print("The sequence is valid!\n")
            else:
                print("The sequence is not valid!\n")


if __name__ == '__main__':
    # test_scanner()
    menu_FA()
