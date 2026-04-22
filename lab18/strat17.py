"""
На окружности отмечено 9 точек, делящих эту окружность на 9 равных дуг. Петя и
Вася играют в игру, делая ходы по очереди. Первым ходит Петя; своим первым ходом он
окрашивает в красный или синий цвет любую отмеченную точку. Затем каждый из игроков
своим ходом может окрасить в красный или синий цвет любую неокрашенную отмеченную
точку, соседнюю с уже окрашенной. Вася выигрывает, если после окрашивания всех точек
найдётся равносторонний треугольник, все три вершины которого окрашены, причём в один и
тот же цвет.
"""

import random

class GameState:
    def __init__(self):
        self.colors = [None] * 9
        self.current_player = 0
        self.first_move_done = False

    def get_available_points(self):
        if not self.first_move_done:
            return [i for i in range(9) if self.colors[i] is None]
        available = set()
        for i in range(9):
            if self.colors[i] is not None:
                left = (i - 1) % 9
                right = (i + 1) % 9
                if self.colors[left] is None:
                    available.add(left)
                if self.colors[right] is None:
                    available.add(right)
        return list(available)

    def is_full(self):
        return all(c is not None for c in self.colors)

    def make_move(self, point, color):
        if point not in self.get_available_points():
            return False
        self.colors[point] = color
        self.first_move_done = True
        self.current_player = 1 - self.current_player
        return True

    def check_winner(self):
        triangles = [(0,3,6), (1,4,7), (2,5,8)]
        for t in triangles:
            c1 = self.colors[t[0]]
            c2 = self.colors[t[1]]
            c3 = self.colors[t[2]]
            if c1 is not None and c1 == c2 == c3:
                return True
        return False

    def get_winning_moves(self):
        winning_moves = []
        triangles = [(0,3,6), (1,4,7), (2,5,8)]
        for t in triangles:
            points = list(t)
            colors = [self.colors[p] for p in points]
            none_count = colors.count(None)
            if none_count == 1:
                none_idx = colors.index(None)
                color1 = colors[(none_idx + 1) % 3]
                color2 = colors[(none_idx + 2) % 3]
                if color1 == color2 and color1 is not None:
                    winning_moves.append((points[none_idx], color1))
        return winning_moves

    def display(self):
        print("\nТекущее состояние (точки на окружности пронумерованы 0..8):")
        for i in range(3):
            row = []
            for j in range(3):
                idx = i * 3 + j
                color_char = '.'
                if self.colors[idx] == 'R':
                    color_char = 'R'
                elif self.colors[idx] == 'B':
                    color_char = 'B'
                row.append(f"{idx}:{color_char}")
            print("  " + "   ".join(row))
        print("\nЛегенда: R - красный, B - синий, . - не окрашена")
        available = self.get_available_points()
        print(f"Доступные для хода точки: {available}\n")


class Player:
    def __init__(self, name):
        self.name = name

    def make_move(self, state):
        raise NotImplementedError


class HumanPlayer(Player):
    def make_move(self, state):
        available = state.get_available_points()
        while True:
            try:
                point = int(input(f"{self.name}, выберите точку (0-8): "))
                if point not in available:
                    print("Точка недоступна, попробуйте снова.")
                    continue
                color = input("Выберите цвет (R - красный, B - синий): ").upper()
                if color not in ('R', 'B'):
                    print("Некорректный цвет, введите R или B.")
                    continue
                return point, color
            except ValueError:
                print("Введите число.")


class ComputerPlayer(Player):
    def make_move(self, state):
        available = state.get_available_points()
        winning_moves = state.get_winning_moves()
        for point, color in winning_moves:
            if point in available:
                return point, color
        point = random.choice(available)
        color = random.choice(['R', 'B'])
        print(f"Компьютер {self.name} выбирает точку {point} и цвет {color}")
        return point, color


class Game:
    def __init__(self, player1, player2):
        self.state = GameState()
        self.players = [player1, player2]

    def run(self):
        print("Игра началась! Цель: после заполнения всех точек, если есть одноцветный равносторонний треугольник, выигрывает Вася, иначе Петя.")
        print("Первый ход делает Петя (игрок 1).")
        self.state.display()

        while not self.state.is_full():
            current_player = self.players[self.state.current_player]
            print(f"\nХод: {current_player.name}")
            point, color = current_player.make_move(self.state)
            if self.state.make_move(point, color):
                self.state.display()
            else:
                print("Ошибка хода, попробуйте еще раз.")
                continue

        if self.state.check_winner():
            print("Побеждает Вася! (найден одноцветный равносторонний треугольник)")
        else:
            print("Побеждает Петя! (нет одноцветного равностороннего треугольника)")


class GameInterface:
    def __init__(self):
        self.mode = None

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

    def setup_players(self):
        if self.mode == "pvp":
            player1 = HumanPlayer("Петя")
            player2 = HumanPlayer("Вася")
        else:
            player1 = HumanPlayer("Петя")
            player2 = ComputerPlayer("Вася")
        return player1, player2

    def run(self):
        self.select_mode()
        p1, p2 = self.setup_players()
        game = Game(p1, p2)
        game.run()


if __name__ == "__main__":
    interface = GameInterface()
    interface.run()