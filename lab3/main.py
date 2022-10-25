import SymbolTable


def test():
    st = SymbolTable.SymbolTable(13)
    st.add('a')
    st.add('test')
    st.to_string()


if __name__ == '__main__':
    test()
