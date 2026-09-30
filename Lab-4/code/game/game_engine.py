import pygame

from .obstacle import Obstacle
from .player import Player
from .sound import load_sounds

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (120, 80, 40)
DARK_GREEN = (30, 100, 30)

MENU = "menu"
PLAYING = "playing"
GAME_OVER = "game_over"

# A frame can never move an obstacle further than the narrowest hitbox,
# so no obstacle can ever skip past the player between two frames.
MAX_SPEED = 22.0
SPEED_RAMP = 0.003

DIFFICULTIES = (
    ("Easy", 5.0, 95),
    ("Medium", 6.0, 70),
    ("Hard", 9.0, 48),
)
OPTION_LINES = [f"{index + 1}  {name}" for index, (name, _, _) in enumerate(DIFFICULTIES)] + ["Q / Esc  Quit"]


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ground_y = height - 40
        self.player = Player(80, self.ground_y)
        self.font = pygame.font.SysFont("Arial", 30)
        self.title_font = pygame.font.SysFont("Arial", 48, bold=True)
        self.sounds = load_sounds()

        self.running = True
        self.start_game(*DIFFICULTIES[1])
        self.state = MENU

    def start_game(self, name, speed, spawn_interval):
        self.difficulty = name
        self.speed = speed
        self.spawn_interval = spawn_interval
        self._spawn_timer = 0
        self.obstacles = []
        self.score = 0
        self.distance = 0
        self.player.reset()
        self.state = PLAYING

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key in (pygame.K_ESCAPE, pygame.K_q):
            self.running = False
        elif self.state == PLAYING:
            if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w) and self.player.jump():
                self._play("jump")
        elif pygame.K_1 <= event.key <= pygame.K_3:
            self.start_game(*DIFFICULTIES[event.key - pygame.K_1])

    def update(self):
        if self.state != PLAYING:
            return

        self.speed = min(self.speed + SPEED_RAMP, MAX_SPEED)
        self.player.update()

        self._spawn_timer += 1
        if self._spawn_timer >= self.spawn_interval:
            self._spawn_timer = 0
            self.obstacles.append(Obstacle(self.width, self.ground_y))

        for obstacle in self.obstacles:
            obstacle.move(self.speed)

        if any(obstacle.hits(self.player.rect()) for obstacle in self.obstacles):
            self.state = GAME_OVER
            self._play("game_over")
            return

        for obstacle in self.obstacles:
            if not obstacle.scored and obstacle.x + obstacle.width < self.player.x:
                obstacle.scored = True
                self.score += 1
                self._play("score")

        self.obstacles = [o for o in self.obstacles if not o.off_screen()]
        self.distance += self.speed

    def render(self, screen):
        pygame.draw.line(screen, BROWN, (0, self.ground_y), (self.width, self.ground_y), 4)

        pygame.draw.rect(screen, WHITE, self.player.rect())
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, DARK_GREEN, obstacle.rect())

        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        if self.state == MENU:
            self._draw_overlay(screen, ["ENDLESS RUNNER", *OPTION_LINES])
        elif self.state == GAME_OVER:
            self._draw_overlay(screen, ["GAME OVER", f"Final score: {self.score}", *OPTION_LINES])

    def _draw_overlay(self, screen, lines):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))

        y = 90
        for index, line in enumerate(lines):
            font = self.title_font if index == 0 else self.font
            text = font.render(line, True, WHITE)
            screen.blit(text, (self.width // 2 - text.get_width() // 2, y))
            y += 46 if index == 0 else 30

    def _play(self, name):
        if name in self.sounds:
            self.sounds[name].play()
