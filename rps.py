#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
"""The Player class is the parent class for all of the Players
in this game"""
import time
import random


moves = ['rock', 'paper', 'scissors']


def print_timer(message):
    print(message)
    time.sleep(2)


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.PrevStep = None

    def move(self):
        if self.PrevStep is None:
            return Player.move(self)
        return self.PrevStep

    def learn(self, PrevStep):
        # Save the move made by the opponent on the last round.
        self.PrevStep = PrevStep


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.forward = 0

    def move(self):
        move = 0
        if self.forward == 0:
            move = moves[0]
            self.forward = self.forward + 1
        elif self.forward == 1:
            move = moves[1]
            self.forward = self.forward + 1
        else:
            move = moves[2]
            self.forward = self.forward + 1
        return move


class HumanPlayer(Player):
    def move(self):
        self.my_move = Gamer("rock, paper, scissors >\n", moves)
        if self.my_move in moves:
            return self.my_move
        elif self.my_move not in moves:
            print_timer("Invalid input, please try again")
        else:
            endGame()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p2.learn(move1)

        if move1 == move2:
            print_timer(f"Player_One: {move1}, Player_Two: {move2}")
            print_timer(f"Player_One: {self.p1.score},"
                        f"Player_Two: {self.p2.score}")
            print_timer("We have a tie!\n")

        elif beats(move1, move2):
            print_timer(f"Player_One: {move1}, Player_Two: {move2}")
            self.p1.score += 1
            print_timer(f"Player_One: {self.p1.score},"
                        f"Player_Two: {self.p2.score}")
            print_timer("**** Player_One Wins this round ****!!\n")

        elif beats(move2, move1):
            print_timer(f"Player_One: {move1}, Player_Two: {move2}")
            self.p2.score += 1
            print_timer(f"Player_One: {self.p1.score},"
                        f"Player_Two: {self.p2.score}")
            print_timer("**** Player_Two Wins this round ****!\n")

    def play_game(self):
        print_timer("You are Welcome to Play the Famous rock, paper, scissors")
        print_timer("You have Four rounds of this game to play")
        print_timer("Please kindly choose between rock, paper, or scissors\n")
        print_timer("Let the best player Win!\n")
        print_timer("Game Start!!!")
        for round in range(4):
            print_timer(f"Round {round + 1}:")
            round += 1
            self.play_round()
        self.winner()
        print_timer("Game over!\n")
        endGame()

    def winner(self):
        print_timer(" End score:")
        print_timer(f"Player_One: {self.p1.score},Player_Two: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print_timer("**** Player_One WON!!! ****!!\n")
        elif self.p2.score > self.p1.score:
            print_timer("**** Player_Two WON!!!!****!\n")
        else:
            print_timer("*** Is a Draw! Player_One"
                        "and Player_Two are Both WInners\n")


def Gamer(ask, Pmove):
    while True:
        choice = input(ask).lower()
        if choice in Pmove:
            return choice


def endGame():
    print_timer("This is the end Thank you for playing.")


def Start_game():
    cpu = []
    cpu.append(Player())
    cpu.append(RandomPlayer())
    cpu.append(CyclePlayer())
    cpu.append(ReflectPlayer())

    while True:
        randomGame = random.randint(0, 3)
        game = Game(HumanPlayer(), cpu[randomGame])
        game.play_game()
        break


if __name__ == '__main__':
    Start_game()

# reference :Youtube, stackoverflow, programize website, GitHub, udacity
