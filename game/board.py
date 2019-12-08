class chess_board():
    """
    Contains the game board logic
    """
    def __init__(self):
        self.board = {}
        letters = "abcdefgh"
        for letter in letters:
            self.board[letter] = {}
            numbers = "12345678"
            for number in numbers:
                self.board[letter][number] = "."

    def __str__(self):
        string = "__________\n"
        for row in self.board:
            string = "{}|".format(string)
            for column in self.board[row]:
                string = "{}{}".format(string, self.board[row][column])
            string = "{}|\n".format(string)
        string = "{}__________".format(string)
        return string
