import sys

""" expectative: 

     1   2   3

1    0 | x | x 
    ---+---+---
2    X | 0 | X
    ---+---+---
3      |   | 
"""


class Table:
    # Declarations
    available_positions = {(x, y): True for x in range(1, 4) for y in range(1, 4)}
    table = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]   # Create table as an array so later can use join() to print as string in a nested loop
    p1_selected, p2_selected = list(), list()
    player_turn = "p1"
    players = ["p1", "p2"]
    player_symbol = {"p1": "X", "p2": "0"}
    PLAYING = True

    def __show_info(self):
        print(self.available_positions, self.players, self.p1_selected, self.p2_selected)

    def check_position(self, p):
        try:
            if self.available_positions[p]:
                self.available_positions[p] = False  # Change availability of selected position

                if self.player_turn == "p1":    # Add to player's selections
                    self.p1_selected.append(p)
                else:
                    self.p2_selected.append(p)

                self.player_turn = self.players[1]  # Change player turn
                self.players.append(self.players[0])
                del self.players[0]

            else:
                self.error()
        except KeyError:
            self.error()

    def check_win(self):
        pass

    def update_table(self, position):
        self.table[position[0]-1][position[1]-1] = self.player_symbol.get(self.player_turn)

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

    def error(self):
        print("[!] Enter a valid option... ")
        self.enter_value()

    def enter_value(self):
        try:
            print("\nPlayer {} turn".format(self.player_turn))
            position = tuple(map(lambda x: int(x), input("Enter coordinates x y (i.e 2 3): ").split(" ")))
            self.check_position(position)
            return position
        except Exception as e:
            print(e)
            self.error()

    def main(self):
        while self.PLAYING:
            self.__show_info()
            self.show_table()
            position = self.enter_value()
            self.update_table(position)
        sys.exit()


if __name__ == '__main__':
    try:
        Table().main()
    except KeyboardInterrupt:
        sys.exit()