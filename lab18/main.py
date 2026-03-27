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

    def do_turn(self, pack: JuicePack):
        if pack.volume - self.cup.max_volume < 0:
            return False
        self.cup.scoop(pack)

        print(pack.volume)

class Masha:
    def __init__(self):
        self.cups = [Cup(240), Cup(240)]

    def do_turn_with_one_pack(self, pack: JuicePack):
        if pack.volume - self.cups[0].max_volume < 0:
            return False

        self.cups[0].scoop(pack)

        return True

    def do_turn_with_two_packs(self, pack1: JuicePack, pack2: JuicePack):
        if pack1.volume - self.cups[0].max_volume < 0 or pack2.volume - self.cups[1].max_volume < 0:
            return False

        self.cups[0].scoop(pack1)
        self.cups[1].scoop(pack2)
        return True


class GameLogic:
    def __init__(self):
        self.pack1 = JuicePack("Pear")
        self.pack2 = JuicePack("Cherry")

        self.Masha = Masha()
        self.UncleAndrey = UncleAndrey()



class GameInterface:
    def __init__(self):
        self.W_W = 1920
        self.W_H = 1080
        self.IsRunning = True
        self.gameLogic = GameLogic()

        self.game_state = "selecting"

        self.turn_number = 1

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
        if player == "Masha" and move_type == "FP":
            self.gameLogic.Masha.do_turn_with_one_pack(self.gameLogic.pack1)

    def create_buttons(self):
        button_masha_first_pack = Button(
            self.window, 100, 100, 300, 150, text="Scoop from first pack by Masha",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: {
                self.gameLogic.Masha.do_turn_with_one_pack(self.gameLogic.pack1),
                self.resize_pack_visual(self.gameLogic.pack1.volume, self.gameLogic.pack2.volume)
            }
        )

        button_masha_second_pack = Button(
            self.window, 100, 260, 300, 150, text="Scoop from second pack by Masha",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: {
                self.gameLogic.Masha.do_turn_with_one_pack(self.gameLogic.pack2),
                self.resize_pack_visual(self.gameLogic.pack1.volume, self.gameLogic.pack2.volume)
            }
        )

        button_masha_two_pack = Button(
            self.window, 100, 420, 300, 150, text="Scoop from two packs by Masha",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: {
                self.gameLogic.Masha.do_turn_with_two_packs(self.gameLogic.pack1, self.gameLogic.pack2),
                self.resize_pack_visual(self.gameLogic.pack1.volume, self.gameLogic.pack2.volume)
            }
        )

        button_andrey_first_pack = Button(
            self.window, self.W_W - 400, 100, 300, 150, text="Scoop from first pack by Andrey",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: {
                self.gameLogic.UncleAndrey.do_turn(self.gameLogic.pack1),
                self.resize_pack_visual(self.gameLogic.pack1.volume, self.gameLogic.pack2.volume)
            }
        )

        button_andrey_second_pack = Button(
            self.window, self.W_W - 400, 260, 300, 150, text="Scoop from second pack by Andrey",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: {
                self.gameLogic.UncleAndrey.do_turn(self.gameLogic.pack2),
                self.resize_pack_visual(self.gameLogic.pack1.volume, self.gameLogic.pack2.volume)
            }
        )

        button_gamemode_pvp = Button(
            self.window, int(self.W_W / 2 - 50), 900, 100, 100, text="PVP",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: {
                self.gameLogic.UncleAndrey.do_turn(self.gameLogic.pack2),
                self.resize_pack_visual(self.gameLogic.pack1.volume, self.gameLogic.pack2.volume),

            }
        )

        button_gamemode_pvb = Button(
            self.window, int(self.W_W / 2 - 160), 900, 100, 100, text="PVB",
            fontSize=20, margin=20,
            inactiveColour=(169, 169, 169),
            pressedColour=(128, 128, 128),
            onClick=lambda: {
                self.gameLogic.UncleAndrey.do_turn(self.gameLogic.pack2),
                self.resize_pack_visual(self.gameLogic.pack1.volume, self.gameLogic.pack2.volume)
            }
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

            self.window.blit(text_surface_p1, (800, 770 - self.first_pack_height))
            self.window.blit(text_surface_p2, (910, 770 - self.second_pack_height))

            pg.draw.rect(self.window, (0, 255, 0), (800, 800 - self.first_pack_height, 100, self.first_pack_height))
            pg.draw.rect(self.window, (255, 0, 0), (910, 800 - self.second_pack_height, 100, self.second_pack_height))

            pg.display.update()



            pg.time.delay(10)

        pg.quit()

def main():
    game = GameInterface()

if __name__ == '__main__':
    main()
