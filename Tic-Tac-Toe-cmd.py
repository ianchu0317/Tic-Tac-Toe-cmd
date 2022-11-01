from time import sleep
import pprint
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
    available_positions = {(x, y): True for x in range(1, 4) for y in range(1, 4)}
    p1_selected = []
    p2_selected = []
    player_turn = "p1"
    players = ["p1", "p2"]
    PLAYING = True

    def check_position(self, p):
        try:
            if self.available_positions[p]:
                self.available_positions[p] = False  # Change availability

                if self.player_turn == "p1":    # Add to done list
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

    def show_table(self):
        print("""
             1   2   3

        1    0 | x | x 
            ---+---+---
        2    X | 0 | X
            ---+---+---
        3      |   | 
        """)

    def error(self):
        print("[!] Enter a valid option... ")
        self.enter_value()

    def enter_value(self):
        try:
            print("Player {} turn".format(self.player_turn))
            position = tuple(map(lambda x: int(x), input("Enter coordinates x y (i.e 2 3): ").split(" ")))
            self.check_position(position)
        except Exception as e:
            print(e)
            self.error()

    def main(self):
        while self.PLAYING:
            self.show_table()
            self.enter_value()


if __name__ == '__main__':
    try:
        Table().main()
    except KeyboardInterrupt:
        sys.exit()
