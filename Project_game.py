import os
import random
import pygame


def main():
    class Tile(pygame.sprite.Sprite):
        def __init__(self, filename, x, y):
            super().__init__()

            self.name = filename.split(".")[0]

            self.original_image = pygame.image.load(
                'Images/object/' + filename)

            self.original_image = pygame.transform.scale(
                (self.original_image), (100, 100))

            self.image_back = pygame.image.load(
                'Images/object/' + filename)

            self.image_back = pygame.transform.scale(
                (self.image_back), (100, 100))

            pygame.draw.rect(
                self.image_back, WHITE, self.image_back.get_rect())

            self.image = self.image_back
            self.rect = self.image.get_rect(topleft=(x, y))
            self.shown = False

        def update(self):
            self.image = self.original_image if self.shown else self.image_back

        def show(self):
            self.shown = True

        def hide(self):
            self.shown = False

    class Game():
        def __init__(self):
            self.level = 1
            self.level_complete = False

            self.all_cards = [f for f in os.listdir(
                "Images/object") if os.path.join("Images/object", f)]
            del(self.all_cards[0])

            self.img_width, self.img_height = (128, 128)
            self.padding = 20
            self.margin_top = 160
            self.cols = 4
            self.rows = 2
            self.width = 1280

            self.tile_groups = pygame.sprite.Group()

            self.flipped = []
            self.frame_count = 0
            self.block_game = False

            self.generate_level(self.level)

            self.back_image = True
            self.background = pygame.transform.scale(
                pygame.image.load("Images/board.jpg"), (1280, 860))
            self.background_toggle = self.background
            self.background_toggle_rect = self.background_toggle.get_rect(
                midtop=(WINDOW_WIDTH - 650, 110))

            self.playing_music = True

            self.sound_on = pygame.transform.scale(pygame.image.load(
                "Images/speaker.png").convert_alpha(), (50, 50))
            self.sound_off = pygame.transform.scale(pygame.image.load(
                "Images/speaker (1).png").convert_alpha(), (50, 50))
            self.music_toggle = self.sound_on
            self.music_toggle_rect = self.music_toggle.get_rect(
                topright=(WINDOW_WIDTH - 10, 10))

            pygame.mixer.music.load("Sounds/song.mp3")
            pygame.mixer.music.set_volume(.3)
            pygame.mixer.music.play()

        def update(self, event_list):
            self.user_input(event_list)
            self.draw()
            self.check_level_complete(event_list)

        def check_level_complete(self, event_list):
            if not self.block_game:
                for event in event_list:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for tile in self.tile_groups:
                            if tile.rect.collidepoint(event.pos):
                                self.flipped.append(tile.name)
                                tile.show()
                                if len(self.flipped) == 2:
                                    if self.flipped[0] != self.flipped[1]:
                                        self.block_game = True
                                    else:
                                        self.flipped = []
                                        for tile in self.tile_groups:
                                            if tile.shown:
                                                self.level_complete = True
                                            else:
                                                self.level_complete = False
                                                break
            else:
                self.frame_count += 1
                if self.frame_count == FPS:
                    self.frame_count = 0
                    self.block_game = False

                    for tile in self.tile_groups:
                        if tile.name in self.flipped:
                            tile.hide()
                    self.flipped = []

        def generate_level(self, level):
            self.cards = self.select_random_cards(self.level)
            self.level_complete = False
            self.rows = self.level + 1
            self.cols = 4
            self.generate_tileset(self.cards)

        def generate_tileset(self, cards):
            self.cols = self.rows = self.cols if self.cols >= self.rows else self.rows
            TILES_WIDTH = (self.img_width * self.cols + self.padding * 3)
            LEFT_MARING = RIGHT_MARGIN = (self.width - TILES_WIDTH) // 2
            self.tile_groups.empty()

            for i in range(len(cards)):
                x = LEFT_MARING + \
                    ((self.img_width + self.padding) * (i % self.cols))
                y = self.margin_top + \
                    (i // self.rows * (self.img_height + self.padding))
                tile = Tile(cards[i], x, y)
                self.tile_groups.add(tile)

        def select_random_cards(self, level):
            cards = random.sample(
                self.all_cards, (self.level + self.level + 2))
            cards_copy = cards.copy()
            cards.extend(cards_copy)
            random.shuffle(cards)
            return cards

        def user_input(self, event_list):
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.music_toggle_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.playing_music:
                            self.playing_music = False
                            self.music_toggle = self.sound_off
                            pygame.mixer.music.pause()
                        else:
                            self.playing_music = True
                            self.music_toggle = self.sound_on
                            pygame.mixer.music.unpause()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.level_complete:
                        self.level += 1
                        if self.level >= 6:
                            self.level = 1
                        self.generate_level(self.level)

        def draw(self):
            screen.fill(BLACK)

            title_font = pygame.font.Font('Gray Skin.otf', 45)
            content_font = pygame.font.Font('Gray Skin.otf', 40)

            title_text = title_font.render(
                "Simple Memory Game", True, WHITE)
            title_rect = title_text.get_rect(midtop=(WINDOW_WIDTH // 2, 10))

            level_text = content_font.render(
                'Level ' + str(self.level), True, WHITE)
            level_rect = level_text.get_rect(midtop=(WINDOW_WIDTH // 2, 80))

            info_text = content_font.render(
                'Find 2 that are matching', True, WHITE)
            info_rect = info_text.get_rect(midtop=(WINDOW_WIDTH // 2, 120))

            instruction_text = content_font.render(
                'click here to mute the music', True, WHITE)
            instruction_rect = instruction_text.get_rect(
                topleft=(WINDOW_WIDTH - 300, 69))

            if not self.level == 5:
                next_text = content_font.render("Congratulations! Level Complete. Please press space to proceed to next level",
                                                True, WHITE)
            else:
                next_text = content_font.render("Congratulations! You finished the game! Presss space to play again or click red button to quit the game.",
                                                True, WHITE)
            next_rect = next_text.get_rect(midbottom=(
                WINDOW_WIDTH // 2, WINDOW_HEIGHT - 90))

            screen.blit(title_text, title_rect)
            screen.blit(level_text, level_rect)
            screen.blit(info_text, info_rect)
            screen.blit(instruction_text, instruction_rect)
            screen.blit(self.music_toggle, self.music_toggle_rect)
            screen.blit(self.background_toggle, self.background_toggle_rect)

            self.tile_groups.draw(screen)
            self.tile_groups.update()

            if self.level_complete:
                screen.blit(next_text, next_rect)

    pygame.init()

    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 860
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Memory Game for Assessing your Brain Age")

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    count = 0
    frame_rate = 60
    start_time = 90
    FPS = 60
    clock = pygame.time.Clock()

    game = Game()

    run = True

    while run:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
        total_seconds = count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        font = pygame.font.Font(None, 25)
        text = font.render(output_string, True, WHITE)
        text_rect = text.get_rect(midtop=(1280 // 6, 20))
        screen.blit(text, text_rect)

        total_seconds = start_time - (count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0

        minutes = total_seconds // 60

        seconds = total_seconds % 60

        count += 1

        clock.tick(frame_rate)

        pygame.display.flip()

        game.update(event_list)

        clock.tick(FPS)

    pygame.quit()
