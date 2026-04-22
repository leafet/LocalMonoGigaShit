"""
 Дядя Андрей и девочка Маша играют в игру. У них имеются две упаковки сока по 24
литра: один грушевый, другой вишнёвый. Кроме того, у Андрея есть кружка в 500 мл, а у
Маши — две кружки по 240 мл. Игроки пьют сок по очереди по следующим правилам: они
наполняют все свои кружки до краёв, а затем выпивают налитое до дна. При этом запрещается
смешивать два вида сока в одной ёмкости. Если кто-то не может сделать ход, то ходит его
соперник. Игра заканчивается, когда никто не может сделать ход. Побеждает тот, кто выпил
больше сока.
"""

import pygame as pg
import pygame_widgets as pw
from pygame_widgets.button import Button

class JuicePack:
    def __init__(self, juice_type):
        self.volume = 24000
        self.juice_type = juice_type

class Cup:
    def __init__(self, max_volume):
        self.max_volume = max_volume

    def scoop(self, pack: JuicePack):
        pack.volume -= self.max_volume

class UncleAndrey:
    def __init__(self):
        self.cup = Cup(500)
        self.score = 0

    def check_available_turns(self, packs: list[JuicePack]):
        available_count = 0

        for pack in packs:
            if pack.volume - self.cup.max_volume >= 0:
                available_count += 1

        return available_count

    def do_turn(self, pack: JuicePack):
        if pack.volume - self.cup.max_volume < 0:
            return False

        self.cup.scoop(pack)

        self.score += self.cup.max_volume

        return True

class Masha:
    def __init__(self):
        self.cups = [Cup(240), Cup(240)]
        self.score = 0

    def check_available_turns(self, packs: list[JuicePack]):
        available_turns = []

        if packs[0].volume - (self.cups[0].max_volume + self.cups[1].max_volume) >= 0:
            available_turns.append("FIRST_PACK")

        if packs[1].volume - (self.cups[1].max_volume + self.cups[0].max_volume) >= 0:
            available_turns.append("SECOND_PACK")

        if packs[0].volume - self.cups[0].max_volume >= 0 and packs[1].volume - self.cups[1].max_volume >= 0:
            available_turns.append("BOUGHT_PACKS")

        return available_turns

    def do_turn_with_one_pack(self, pack: JuicePack):
        if pack.volume - (self.cups[0].max_volume + self.cups[1].max_volume) < 0:
            return False

        for cup in self.cups:
            cup.scoop(pack)

        self.cups[0].scoop(pack)

        self.score += self.cups[0].max_volume + self.cups[1].max_volume

        return True

    def do_turn_with_two_packs(self, pack1: JuicePack, pack2: JuicePack):
        if pack1.volume - self.cups[0].max_volume < 0 or pack2.volume - self.cups[1].max_volume < 0:
            return False

        self.cups[0].scoop(pack1)
        self.cups[1].scoop(pack2)

        self.score += self.cups[0].max_volume + self.cups[1].max_volume

        return True


class GameLogic:
    def __init__(self):
        self.pack1 = JuicePack("Pear")
        self.pack2 = JuicePack("Cherry")

        self.Masha = Masha()
        self.UncleAndrey = UncleAndrey()

    def do_bot_move(self):
        available_moves = self.Masha.check_available_turns([self.pack1, self.pack2])

        last_1 = self.pack1.volume - self.Masha.cups[0].max_volume * 2
        last_2 = self.pack2.volume - self.Masha.cups[1].max_volume * 2

        print(f"{last_1}, {last_2}")

        if last_1 > last_2 and "FIRST_PACK" in available_moves:
            self.Masha.do_turn_with_one_pack(self.pack1)
        elif last_1 < last_2 and "SECOND_PACK" in available_moves:
            self.Masha.do_turn_with_one_pack(self.pack2)
        elif "BOUGHT_PACKS" in available_moves:
            self.Masha.do_turn_with_two_packs(self.pack1, self.pack2)




class GameInterface:
    def __init__(self):
        self.W_W = 1600
        self.W_H = 900
        self.IsRunning = True
        self.gameLogic = GameLogic()

        self.game_state_text = "SELECT MODE"

        self.game_state = "selecting"

        self.players = ["Masha", "Andrey"]

        self.current_player = None

        self.first_pack_height = 400
        self.second_pack_height = 400

        self.clock, self.window = self.initialize()

        self.text_font = pg.font.SysFont("Courier", 25)

        self.setup_main_loop()

    def initialize(self):
        pg.init()
        pg.font.init()
        return pg.time.Clock(), pg.display.set_mode((self.W_W, self.W_H))

    def setup_start_scene(self):
        self.window.fill((255, 255, 255))

    def resize_pack_visual(self, new_first_volume, new_second_volume):
        self.first_pack_height = (new_first_volume / 24000) * 400
        self.second_pack_height = (new_second_volume / 24000) * 400

    def process_move(self, player, move_type):
        if self.game_state == "selecting" or self.game_state == "end":
            return False

        if player != self.current_player:
            return False

        turn_state = False

        if player == "Masha" and move_type == "FP":
            turn_state = self.gameLogic.Masha.do_turn_with_one_pack(self.gameLogic.pack1)
        if player == "Masha" and move_type == "SP":
            turn_state = self.gameLogic.Masha.do_turn_with_one_pack(self.gameLogic.pack2)
        if player == "Masha" and move_type == "TP":
            turn_state = self.gameLogic.Masha.do_turn_with_two_packs(self.gameLogic.pack1, self.gameLogic.pack2)
        if player == "Andrey" and move_type == "FP":
            turn_state = self.gameLogic.UncleAndrey.do_turn(self.gameLogic.pack1)
        if player == "Andrey" and move_type == "SP":
            turn_state = self.gameLogic.UncleAndrey.do_turn(self.gameLogic.pack2)

        if turn_state:
            self.current_player = next(x for x in self.players if x != player)

        self.resize_pack_visual(self.gameLogic.pack1.volume, self.gameLogic.pack2.volume)
        return None

    def select_gamemode(self, mode):
        if mode == "PVP":
            self.game_state = "playing_vs_player"
            self.current_player = "Masha"
            self.game_state_text = "MASHA TURN"

        if mode == "PVB":
            self.game_state = "playing_vs_bot"
            self.current_player = "Masha"
            self.game_state_text = "BOT TURN"

    def create_buttons(self):
        button_masha_first_pack = Button(
            self.window, 100, 100, 300, 150, text="Scoop from first pack by Masha",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: self.process_move("Masha", "FP")
        )

        button_masha_second_pack = Button(
            self.window, 100, 260, 300, 150, text="Scoop from second pack by Masha",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: self.process_move("Masha", "SP")
        )

        button_masha_two_pack = Button(
            self.window, 100, 420, 300, 150, text="Scoop from two packs by Masha",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: self.process_move("Masha", "TP")
        )

        button_andrey_first_pack = Button(
            self.window, self.W_W - 400, 100, 300, 150, text="Scoop from first pack by Andrey",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: self.process_move("Andrey", "FP")
        )

        button_andrey_second_pack = Button(
            self.window, self.W_W - 400, 260, 300, 150, text="Scoop from second pack by Andrey",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: self.process_move("Andrey", "SP")
        )

        button_gamemode_pvp = Button(
            self.window, int(self.W_W / 2 - 55), int(self.W_H / 2 + 110), 100, 100, text="PVP",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: self.select_gamemode("PVP")
        )

        button_gamemode_pvb = Button(
            self.window, int(self.W_W / 2 + 55), int(self.W_H / 2 + 110), 100, 100, text="PVB",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: self.select_gamemode("PVB")
        )

        return {
            button_masha_two_pack,
            button_masha_second_pack,
            button_andrey_second_pack,
            button_andrey_first_pack,
            button_masha_first_pack,
            button_gamemode_pvp,
            button_gamemode_pvb
        }

    def process_game_logic(self):
        if (len(self.gameLogic.Masha.check_available_turns([self.gameLogic.pack1, self.gameLogic.pack2])) == 0 and
                self.gameLogic.UncleAndrey.check_available_turns([self.gameLogic.pack1, self.gameLogic.pack2]) == 0) :

            self.current_player = None
            if self.gameLogic.Masha.score < self.gameLogic.UncleAndrey.score:
                self.game_state_text = f"ANDREY WIN"
                return
            self.game_state_text = f"MASHA WIN"

            self.game_state = "end"
            return


        if self.game_state == "playing_vs_bot" and self.current_player == "Masha":
            self.game_state_text = "BOT PLAYING"
            self.gameLogic.do_bot_move()
            self.current_player = next(x for x in self.players if x != "Masha")
            return

        if self.current_player is not None:
            self.game_state_text = f"{str.upper(self.current_player)} PLAYING"
            return

    def setup_main_loop(self):
        buttons = self.create_buttons()

        while self.IsRunning:
            self.clock.tick(60)
            self.window.fill((255, 255, 255))

            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.IsRunning = False

            pw.update(events)

            for btn in buttons:
                btn.draw()

            text_surface_p1 = self.text_font.render(f"{self.gameLogic.pack1.volume}", False, (0, 0, 0))
            text_surface_p2 = self.text_font.render(f"{self.gameLogic.pack2.volume}", False, (0, 0, 0))
            text_surface_state = self.text_font.render(f"{self.game_state_text}", False, (0, 0, 0))
            text_surface_p1_score = self.text_font.render(
                f"Masha - {self.gameLogic.Masha.score}", False, (0, 0, 0)
            )
            text_surface_p2_score = self.text_font.render(
                f"Andrey - {self.gameLogic.UncleAndrey.score}", False, (0, 0, 0)
            )

            center_x = self.W_W / 2
            center_y = self.W_H / 2 + 100

            self.window.blit(text_surface_p1, (center_x - 55, center_y - 30 - self.first_pack_height))
            self.window.blit(text_surface_p2, (center_x + 55, center_y - 30 - self.second_pack_height))
            self.window.blit(text_surface_state, (center_x, 50))
            self.window.blit(text_surface_p1_score, (0 + 100, self.W_H - 50))
            self.window.blit(text_surface_p2_score, (self.W_W - 400, self.W_H - 50))

            pg.draw.rect(self.window,
                         (0, 255, 0),
                         (center_x - 55, center_y - self.first_pack_height, 100, self.first_pack_height))

            pg.draw.rect(self.window,
                         (255, 0, 0),
                         (center_x + 55, center_y - self.second_pack_height, 100, self.second_pack_height))

            pg.display.update()

            self.process_game_logic()

        pg.quit()

def main():
    GameInterface()

if __name__ == '__main__':
    main()
