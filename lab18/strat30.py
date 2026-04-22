"""
Изначально на доске написано число n. Игрок в свой ход может прибавить к числу на
доске любой его натуральный делитель, стереть старое число и записать новое. (Например,
если на доске написано число 12, то можно его стереть и написать одно из чисел 13, 14, 15, 16,
18, 24.). Побеждает тот, кто получит после своего хода число, не меньшее 60.
"""

import random

class Game:
    def __init__(self, players, start_number=1):
        self.players = players
        self.current_number = start_number
        self.current_player_index = 0
        self.winner = None

    def get_divisors(self, n):
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors

    def make_move(self, divisor):
        self.current_number += divisor
        if self.current_number >= 60:
            self.winner = self.players[self.current_player_index]
            return True
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return False

    def get_current_player(self):
        return self.players[self.current_player_index]

    def is_game_over(self):
        return self.winner is not None


class Player:
    def __init__(self, name):
        self.name = name

    def make_move(self, current_number, game):
        raise NotImplementedError


class HumanPlayer(Player):
    def make_move(self, current_number, game):
        divisors = game.get_divisors(current_number)
        print(f"Текущее число: {current_number}")
        print(f"Доступные делители: {divisors}")
        while True:
            try:
                choice = int(input(f"{self.name}, выберите делитель: "))
                if choice in divisors:
                    return choice
                else:
                    print("Некорректный делитель, попробуйте снова.")
            except ValueError:
                print("Введите число.")


class ComputerPlayer(Player):
    def make_move(self, current_number, game):
        divisors = game.get_divisors(current_number)

        for d in divisors:
            if current_number + d >= 60:
                print(f"Компьютер {self.name} выбирает делитель {d} и побеждает!")
                return d

        choice = random.choice(divisors)
        print(f"Компьютер {self.name} выбирает делитель {choice}")
        return choice


class GameInterface:
    def __init__(self):
        self.mode = None
        self.game = None

    def select_mode(self):
        print("Выберите режим игры:")
        print("1 - Игрок против компьютера")
        print("2 - Игрок против игрока")
        while True:
            mode = input("Введите 1 или 2: ")
            if mode == "1":
                self.mode = "pve"
                break
            elif mode == "2":
                self.mode = "pvp"
                break
            else:
                print("Некорректный ввод.")

    def setup_game(self):
        if self.mode == "pve":
            player1 = HumanPlayer("Игрок 1")
            player2 = ComputerPlayer("Компьютер")
            players = [player1, player2]
        else:
            player1 = HumanPlayer("Игрок 1")
            player2 = HumanPlayer("Игрок 2")
            players = [player1, player2]

        start_number = 1
        self.game = Game(players, start_number)

    def run(self):
        self.select_mode()
        self.setup_game()
        print("Игра началась! Цель: получить число >= 60.")
        while not self.game.is_game_over():
            current_player = self.game.get_current_player()
            print(f"\nХод игрока: {current_player.name}")
            divisor = current_player.make_move(self.game.current_number, self.game)
            self.game.make_move(divisor)
            print(f"Новое число: {self.game.current_number}")
            if self.game.is_game_over():
                print(f"\nПобедитель: {self.game.winner.name}!")
                break


if __name__ == "__main__":
    interface = GameInterface()
    interface.run()