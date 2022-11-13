class FiniteAutomata:
    def __init__(self):
        self.set_of_states = []
        self.alphabet = []
        self.transitions = {}
        self.initial_state = None
        self.final_states = []
        self.read_FA_from_file()

    def read_FA_from_file(self):
        f = open("FA.in", "r")
        counter = 0
        for line in f:
            if counter == 0:
                for i in line:
                    if i != ',' and i != '\n':
                        self.set_of_states.append(i)
            elif counter == 1:
                for i in line:
                    if i != ',' and i != '\n':
                        self.alphabet.append(i)
            elif counter == 2:
                self.initial_state = line.strip('\n')
            elif counter == 3:
                for i in line:
                    if i != ',' and i != '\n':
                        self.final_states.append(i)
            elif counter > 3 and line != '\n':
                self.transitions[(line[1], line[3])] = line[6]
            counter += 1

    def check_sequence(self, sequence):
        current = self.initial_state
        for item in sequence:
            if (current, item) in self.transitions:
                new = self.transitions[(current, item)]
                current = new
            else:
                return False
        if current in self.final_states:
            return True
        return False

    def dict_to_str(self):
        for item in self.transitions:
            print(item, "=", self.transitions[item])

    def print_everything(self):
        print("\nSET OF STATES:\n")
        print(self.set_of_states)
        print("\nINITIAL STATE:\n")
        print(self.initial_state)
        print("\nFINAL STATES:\n")
        print(self.final_states)
        print("\nALPHABET:\n")
        print(self.alphabet)
        print("\nTRANSITIONS:\n")
        print(self.dict_to_str())

