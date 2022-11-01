import sys


class Table:
    # Declarations
    table = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]   # Create table as an array so later can use join() to print as string in a nested loop
    available_positions = {(x, y): True for x in range(1, 4) for y in range(1, 4)}
    p1_selected, p2_selected = set(), set()
    player_turn = "p1"
    players = ["p1", "p2"]
    player_symbol = {"p1": "X", "p2": "0"}
    position = tuple()
    win_cases = [{(1, y) for y in range(1, 4)},  # horizontal lines
                 {(2, y) for y in range(1, 4)},
                 {(3, y) for y in range(1, 4)},
                 {(x, 1) for x in range(1, 4)},  # vertical lines
                 {(x, 2) for x in range(1, 4)},
                 {(x, 3) for x in range(1, 4)},
                 {(1, 1), (2, 2), (3, 3)},  # diagonals
                 {(1, 3), (2, 2), (3, 1)}]
    PLAYING = True

    def main(self):
        while self.PLAYING:
            # self.__show_info()
            self.check_win()
            self.show_table()
            self.enter_value()
            self.update_table()
            self.check_draw()
            self.check_win()
        sys.exit()

    def __show_info(self):
        print(self.available_positions, self.players, self.p1_selected, self.p2_selected)

    def show_table(self):
        # Format output and show table
        rc = cc = 2  # row and column counter
        _cc = 1
        print("    1   2   3")
        for column in self.table:
            for row in column:
                if rc == 2:
                    print(f"{_cc}", end='')
                    print("  ", end='')
                print(f" {row} ", end='')
                if rc:
                    print("|", end='')
                    rc -= 1
            rc = 2
            _cc += 1
            if cc:
                print("\n   ---+---+---")
                cc -= 1

    def enter_value(self):  # User input
        try:
            print("\nPlayer {} turn".format(self.player_turn))
            position = tuple(map(lambda x: int(x), input("Enter coordinates x y (i.e 2 3): ").split(" ")))
            self.check_position(position)
        except Exception as e:
            print(e)
            self.error()

    def check_position(self, p):
        try:
            if self.available_positions[p]:
                self.available_positions[p] = False  # Change availability of selected position

                if self.player_turn == "p1":    # Add to player's selections
                    self.p1_selected.add(p)
                else:
                    self.p2_selected.add(p)

                self.player_turn = self.players[1]  # Change player turn
                self.players.append(self.players[0])
                del self.players[0]
                self.position = p

            else:
                self.error()
        except KeyError:
            self.error()

    def error(self):
        print("[!] Enter a valid option... ")
        self.enter_value()

    def update_table(self):
        self.table[self.position[0]-1][self.position[1]-1] = self.player_symbol.get(self.player_turn)

    def check_win(self):
        for case in self.win_cases:
            if self.p1_selected == case or case in self.p1_selected:
                print("p1 won")
                self.PLAYING = False
            elif self.p2_selected == case or case in self.p2_selected:
                print("p2 won")
                self.PLAYING = False

    def check_draw(self):
        finished = True
        for x in self.table:
            for j in x:
                if j == " ":
                    finished = False

        if finished:
            print("[*] Draw")
            self.PLAYING = False


if __name__ == '__main__':
    try:
        Table().main()
    except KeyboardInterrupt:
        sys.exit()
