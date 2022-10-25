class SymbolTable:
    def __init__(self, length):
        self.__elements = [[] for _ in range(length)]
        self.__length = length

    def to_string(self):
        for element in self.__elements:
            print(str(element), '\n')

    def hash(self, key):
        key_ascii = 0
        for char in key:
            key_ascii += ord(char)
        return key_ascii % self.__length

    def get_position(self, key):
        hash_key = self.hash(key)
        hash_list_index = 0
        for element in self.__elements[hash_key]:
            if element == key:
                break
            else:
                hash_list_index += 1
        return hash_key, hash_list_index

    def add(self, key):
        hash_key = self.hash(key)
        if key not in self.__elements[hash_key]:
            self.__elements[hash_key].append(key)
        return self.get_position(key)


