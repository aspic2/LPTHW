#Command line tic tac toe

'''
Problem: create an entertaining game that will push my knowledge of programming

Analysis and Design:
  App must be able to:
      1) Render board (3x3) on screen with placed markers
      2) Allow user to input commands to place markers
      3) Have AI place markers, alternating with user
      4) Keep score over multiple games


Use Case:
    Play tic-tac-toe
    User on command line
    1. User runs script from command line, specifying no. of rounds to play
    2. Game initializes, board is assembled and printed
    3. User is asked to pick a turn, either first (x) or second (o)
    4. First player places marker (X) in desired spot.
        Spot is removed as playable area
    5. Second player (AI) does same with available spots.
    6. Players continue alternating play until one gets 3-in-a-row or all spots are occupied.
    7. Game score is presented.

User Story
    As a Tic-Tac-Toe player,
    I want an AI system to play against
    So that I can improve my logic skills

Player
    Command line inputs

Nouns:
    Player
    No. of rounds
    board
    game
    markers
    AI (Player2)
    Score




AI


Board
    3x3 board
    Mutable with symbols (X or O)


Scoring:

    1 pt per mark on screen
    3 pts for three in row

'''

class Board(object):
    def __init__(self, rows):
        self.gameboard = []
        self.rows = rows
        for row in range (self.rows):
            self.gameboard.append("|_|" * self.rows)


    def print_board(self):
        for row in self.gameboard:
            print("".join(row))
        #return self.gameboard


class Player(object):
    score = 0

    def getPossibleMoves():
        possiblemoves = None
        for x in Board.gameboard:
            if x == "|_|":
                possiblemoves.append(x)
        return possiblemoves


class AI(Player):
    pass

class Gameplay(object):
    pass


class AI(Player):
    pass



tictactoe = Board(3)
#tictactoe.print_board()

print(type(tictactoe.gameboard))
