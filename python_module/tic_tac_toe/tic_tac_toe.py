"""
This module contains Tic Tac Toe Game
"""
from typing import Dict
import logging


# Set logger
logging.basicConfig(filename="winners_game.log", level=logging.INFO, format="%(asctime)s - %(message)s", datefmt='%d-%b-%y %H:%M:%S')
win_logger = logging.getLogger("win_logger")


class Player:
    """
    Class represents Player
    Attributes:
        name: str: name of player
        symbol: str: the symbol that will be placed on the game
                    board as a mark of the player's move (X or O)
        score: int: amount of number of wins
    Methods:
        make_move(self, board: Dict[str, str]): None: changes symbol in dictionary
    """
    def __init__(self, name: str):
        """
        Initializes Player
        :param name: str
        """
        self.name: str = name
        self.symbol: str = " "
        self.score: int = 0

    def __str__(self) -> str:
        """
        String view
        :return: str
        """
        return f"{self.name} has {self.score} win"

    def make_move(self, board: Dict[str, str]) -> None:
        """
        Changes symbol in board
        :param board: Dict[str, str]: the current state of the board
        :return: None
        """
        position: str = str(input(f"{self.name} should make move, enter position: "))
        if position in board.keys() and board[position].isdigit():
            board[position] = self.symbol
        else:
            print("Try again")
            self.make_move(board)


class Game:
    """
    Class represents Game
    Class Attributes:
        game_board:
        count
        match
    Attributes:
        player_1: Player: the first player
        player_2: Player: the second player
        current_moving_player: Player: who must make move
    Static methods:
        display_board(board: Dict[str, str]): None: displays the current state of the board
    Methods:
        play_game(self): None: contains the logic of the game
    """
    game_board: Dict[str, str] = {'1': '1', '2': '2', '3': '3',
                                  '4': '4', '5': '5', '6': '6',
                                  '7': '7', '8': '8', '9': '9'}
    count: int = 0
    match: int = 1

    @staticmethod
    def display_board(board: Dict[str, str]) -> None:
        """
        Displays the current state of the board
        :param board: Dict[str, str]: the current state of the board
        :return: None
        """
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])

    def __init__(self, player_1: Player, player_2: Player):
        """
        Initializes the Game
        :param player_1: the first player
        :param player_2: the second player
        """
        self.player_1: Player = player_1
        self.player_1.symbol = "X"
        self.player_2: Player = player_2
        self.player_2.symbol = "O"
        self.current_moving_player = self.player_2

    def play_game(self) -> None:
        """
        Contains the logic of the game
        The current state of the board appears,
        the make_move method is called from the current player,
        it is checked whether the win condition is met
        :return: None
        """
        for i in range(10):
            Game.display_board(Game.game_board)
            if self.current_moving_player == self.player_2:
                self.player_1.make_move(Game.game_board)
                self.current_moving_player = self.player_1
                Game.count += 1
            else:
                self.player_2.make_move(Game.game_board)
                self.current_moving_player = self.player_2
                Game.count += 1
            if 9 > Game.count >= 5:
                if Game.game_board['1'] == Game.game_board['2'] == Game.game_board['3'] \
                        or Game.game_board['4'] == Game.game_board['5'] == Game.game_board['6'] \
                        or Game.game_board['7'] == Game.game_board['8'] == Game.game_board['9'] \
                        or Game.game_board['1'] == Game.game_board['4'] == Game.game_board['7'] \
                        or Game.game_board['2'] == Game.game_board['5'] == Game.game_board['8'] \
                        or Game.game_board['3'] == Game.game_board['6'] == Game.game_board['9'] \
                        or Game.game_board['7'] == Game.game_board['5'] == Game.game_board['3'] \
                        or Game.game_board['1'] == Game.game_board['5'] == Game.game_board['9']:
                    Game.display_board(Game.game_board)
                    self.current_moving_player.score += 1
                    print(f"Winner: {self.current_moving_player}")
                    print("Game Over")
                    if Game.match == 1:
                        logging.info(f"{self.current_moving_player.name} won")
                    else:
                        logging.info(f"{self.player_1.name} - {self.player_1.score} : "
                                     f"{self.player_2.score} - {self.player_2.name}")

                    break
            if Game.count == 9:
                print("Game Over! Dead heat!")
                break


def main() -> None:
    """
    Main function
    :return: None
    """
    while True:
        choice: int = int(input("Please select the options: \n1 - Start game "
                                "\n2 - See log of win \n3 - Clean log of win \n0 - Exit\n"))
        if choice == 1:
            name_player_1 = str(input("Enter name of first player: "))
            player_1: Player = Player(name_player_1)
            name_player_2 = str(input("Enter name of first player: "))
            player_2: Player = Player(name_player_2)
            current_game = Game(player_1, player_2)
            current_game.play_game()
            while True:
                restart = input("Do want to play Again?(y/n)")
                number_position: int = 1
                for key in Game.game_board:
                    Game.game_board[key] = str(number_position)
                    number_position += 1
                Game.count = 0
                if restart == "y":
                    Game.match += 1
                    current_game.play_game()
                elif restart == "n":
                    Game.match = 1
                    break
                else:
                    print("Try again")
        elif choice == 2:
            with open("winners_game.log", "r") as view_file:
                data = view_file.read()
            print(data)
        elif choice == 3:
            with open("winners_game.log", "r+") as view_file:
                data = view_file.truncate(0)
            print(data)
        elif choice == 0:
            print("Exit")
            break
        else:
            print("Incorrect entering, please, try again ")
            continue


if __name__ == "__main__":
    main()
