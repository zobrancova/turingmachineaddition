class TuringMachine:
    def __init__(self, tape, blank='#'):
        self.tape = tape  #user_input je to co dame na vstupe/resp v kóde
        self.blank = blank  #mriezka je blank symbol
        self.head = self.find_first_number()  #nastavenie hlavy na prvom neprazdom symbole
        self.state = 'zaciatok'  #zaciatocnz stav je zaciatok

    def find_first_number(self):
        #tuto funkciu aplikujem aby som zacinala na zaciatku slova, teda binarneho cisla
        for i, symbol in enumerate(self.tape):
            if symbol in '01':
                return i
        return 0

    def changestate(self):
        symbol = self.tape[self.head] if self.head < len(self.tape) else self.blank

        #printovanie kazdeho kroku pasky
        print(f"State: {self.state}, Head Position: {self.head}, Symbol: {symbol}")

        #na zaklade stavov ktore som si vytvorila v turingmachine.io tak som si napisala nieto podmienky
        #tento cely princip je vysvetleny v readme na gite
        if self.state == 'zaciatok':
            #
            if symbol in '01':
                self.move('L')
            elif symbol == '#':
                self.write('z')
                self.transition('najdikoniec', 'R')

        elif self.state == 'najdikoniec':
            if symbol in '01':
                self.move('R')
            elif symbol == '#':
                self.transition('mriezkakoniec', 'R')

        elif self.state == 'mriezkakoniec':
            if symbol in '01':
                self.transition('najdikoniec', 'R')
            elif symbol == '#':
                self.write('k')
                self.transition('idemnazaciatok', 'L')

        elif self.state == 'idemnazaciatok':
            if symbol in '01#':
                self.move('L')
            elif symbol == 'z':
                self.transition('doprava', 'R')

        elif self.state == 'doprava':
            if symbol in '01':
                self.move('R')
            elif symbol == '#':
                self.write('+')
                self.transition('mriezka', 'R')
            elif symbol == ' ':
                self.move('R')

        elif self.state == 'mriezka':
            if symbol == '#':
                self.transition('citaj', 'L')
            elif symbol in '01':
                self.move('R')
            elif symbol == 'k':
                self.transition('done', 'R')

        elif self.state == 'citaj':
            if symbol == '1':
                self.write('c')
                self.transition('mam1', 'L')
            elif symbol == '0':
                self.write('c')
                self.transition('mam0', 'L')
            elif symbol == '+':
                self.write(' ')
                self.transition('prepis', 'L')

        elif self.state == 'mam1':
            if symbol in '01':
                self.move('L')
            elif symbol == '+':
                self.transition('pripocitaj1', 'L')

        elif self.state == 'mam0':
            if symbol in '01':
                self.move('L')
            elif symbol == '+':
                self.transition('pripocitaj0', 'L')

        elif self.state == 'pripocitaj1':
            if symbol == '0' or symbol == '#':
                self.write('I')
                self.transition('vymaz1', 'R')
            elif symbol == '1':
                self.write('O')
                self.transition('prenasam', 'L')
            elif symbol in 'OI':
                self.move('L')
            elif symbol == ' ':
                self.move('L')

        elif self.state == 'pripocitaj0':
            if symbol == '0':
                self.write('O')
                self.transition('vymaz0', 'R')
            elif symbol == '1':
                self.write('I')
                self.transition('vymaz0', 'R')
            elif symbol in 'OI':
                self.move('L')
            elif symbol == ' ':
                self.move('L')

        elif self.state == 'vymaz1':
            if symbol in '01OI+ ':
                self.move('R')
            elif symbol == 'c':
                self.write(' ')
                self.transition('citaj', 'L')

        elif self.state == 'vymaz0':
            if symbol in '01OI+ ':
                self.move('R')
            elif symbol == 'c':
                self.write(' ')
                self.transition('citaj', 'L')

        elif self.state == 'prenasam':
            if symbol == '0' or symbol == 'z':
                self.write('1')
                self.transition('vymaz1', 'R')
            elif symbol == '1':
                self.write('0')
                self.move('L')

        elif self.state == 'prepis':
            if symbol == 'I':
                self.write('1')
                self.move('L')
            elif symbol == 'O':
                self.write('0')
                self.move('L')
            elif symbol == 'z':
                self.transition('doprava', 'R')
            elif symbol in '01':
                self.move('L')
            elif symbol == ' ':
                self.move('L')
            elif symbol == '#':
                self.write('z')
                self.transition('doprava', 'R')

        elif self.state == 'done':
            print("Machine has reached the 'done' state.")
            return True  # Halting condition

        return False  # Continue execution

    def write(self, symbol):
        if self.head >= len(self.tape):
            self.tape.append(self.blank)
        self.tape[self.head] = symbol

    def move(self, direction):
        if direction == 'R':
            self.head += 1
            if self.head >= len(self.tape):
                self.tape.append(self.blank)
        elif direction == 'L':
            self.head = max(0, self.head - 1)

    def transition(self, state, direction):
        self.state = state
        self.move(direction)

    def run(self):
        step = 0
        while True:
            print(f"Step {step}: {''.join(self.tape)} (Head at {self.head}, State {self.state})")
            stopped = self.changestate()
            step += 1
            if stopped:
                break
        return ''.join(self.tape)

while True:
    tape = ["#"] * 100
    # user_input
    user_input = list(input())
    #danie vstupu na stred pasky
    start_tape = (100-len(user_input))//2
    tape[start_tape:start_tape+len(user_input)] = user_input
    #zavolanie turingovho stroja
    turingmachine = TuringMachine(tape)
    final_tape = turingmachine.run()
    print("Final tape:", final_tape)
    choice = input("Would you like to enter another input? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Exit.")
        break
#


