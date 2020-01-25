#!/usr/bin/env python3
import random

moves = ['rock', 'paper', 'scissors']


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def tie(one, two):
    return (one == two)


def random_oppenent():
    funtions_list = [HumanPlayer, RandomPlayer, CyclePlayer, ReflectPlayer]
    return random.choice(funtions_list)()


class Player:
    def __init__(self):
        self.score = 0
        self.next_move = ""
        self.last_move = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.next_move = their_move
        self.last_move = my_move

    def count(self):
        self.score += 1


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input('Rock, Paper, Scissors? > ').lower()
            if choice in moves:
                return choice


class ReflectPlayer(Player):
    def move(self):
        if self.next_move in moves:
            return self.next_move
        else:
            return random.choice(moves)


class CyclePlayer(Player):
    def move(self):
        if self.last_move in moves:
            if self.last_move == "rock":
                return "paper"
            elif self.last_move == "paper":
                return "scissors"
            else:
                return "rock"
        else:
            return random.choice(moves)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if tie(move1, move2) is True:
            print("It's a tie!")
        elif beats(move1, move2) is True:
            print("*** Player 1 Wins! ***")
            self.p1.count()
        else:
            print("*** Player 2 Wins! ***")
            self.p2.count()

    def play_game(self):
        print("Game start!")
        round_number = 0
        while True:
            print(f"Round {round_number}:")
            round_number += 1
            self.play_round()
            print(f"Score: Player One, {self.p1.score} | "
                  f"Player Two, {self.p2.score}")
            if self.p1.score == 2:
                print(f'>>>> Player 1 Wins 2 to {self.p2.score}! <<<<')
                break
            if self.p2.score == 2:
                print(f'>>>> Player 2 Wins 2 to {self.p1.score}! <<<<')
                break


if __name__ == '__main__':
    game = Game(HumanPlayer(), random_oppenent())
    game.play_game()
