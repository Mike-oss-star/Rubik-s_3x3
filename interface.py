import pygame
import sys
from dataclasses import dataclass
from main import new_cube, apply_moves, scramble, is_solve


WINDOW_W, WINDOW_H = 1280, 700
BG = (28, 28, 32)
PANEL_BG = (45, 45, 52)
PANEL_BORDER = (80, 80, 90)
FG = (230, 230, 230)
MUTED = (160, 160, 170)
ACCENT = (255, 200, 80)
OK_GREEN = (120, 220, 120)
BORDER = (0, 0, 0)

CUBE_DX = 50
CUBE_DY = 50


@dataclass
class FrontView:
    x: int
    y: int
    width: int
    height: int
    d: int
    face: int
    i: int
    j: int

    def points(self):
        return [
            (self.x, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height + self.d),
            (self.x + self.width, self.y + self.d),
        ]

    def draw(self, screen, cube):
        color = cube[self.face][self.i][self.j]
        pts = self.points()
        pygame.draw.polygon(screen, color, pts)
        pygame.draw.polygon(screen, BORDER, pts, 2)


@dataclass
class LeftView:
    x: int
    y: int
    width: int
    height: int
    d: int
    face: int
    i: int
    j: int

    def points(self):
        return [
            (self.x, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height - self.d),
            (self.x + self.width, self.y - self.d),
        ]

    def draw(self, screen, cube):
        color = cube[self.face][self.i][self.j]
        pts = self.points()
        pygame.draw.polygon(screen, color, pts)
        pygame.draw.polygon(screen, BORDER, pts, 2)


@dataclass
class TopView:
    x: int
    y: int
    width: int
    height: int
    d: int
    face: int
    i: int
    j: int

    def points(self):
        return [
            (self.x, self.y),
            (self.x + self.width, self.y + self.height),
            (self.x + 2 * self.width, self.y),
            (self.x + self.width, self.y - self.height),
        ]

    def draw(self, screen, cube):
        color = cube[self.face][self.i][self.j]
        pts = self.points()
        pygame.draw.polygon(screen, color, pts)
        pygame.draw.polygon(screen, BORDER, pts, 2)


KEY_MAP = {
    pygame.K_u: "U", pygame.K_d: "D",
    pygame.K_f: "F", pygame.K_b: "B",
    pygame.K_l: "L", pygame.K_r: "R",
}

HELP_ROWS = [
    ("MOUVEMENTS", None),
    ("u", "rotation haut (U)"),
    ("d", "rotation bas (D)"),
    ("f", "rotation avant (F)"),
    ("b", "rotation arriere (B)"),
    ("l", "rotation gauche (L)"),
    ("r", "rotation droite (R)"),
    ("Shift + touche", "rotation inverse (')"),
    ("", None),
    ("OUTILS", None),
    ("Espace", "melanger"),
    ("N", "nouveau cube"),
    ("Echap", "quitter"),
]


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Rubik's Cube 3x3")
        self.screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        self.title_font = pygame.font.SysFont("arial", 42, bold=True)
        self.section_font = pygame.font.SysFont("arial", 20, bold=True)
        self.label_font = pygame.font.SysFont("arial", 18, italic=True)
        self.mono_font = pygame.font.SysFont("consolas,courier new,monospace", 18)
        self.status_font = pygame.font.SysFont("arial", 22)

        self.cube = new_cube()
        self.last_action = ""

        dx, dy = CUBE_DX, CUBE_DY
        self.front_view = [
            FrontView(120 + 35*i + dx, 150 + 13*i + 45*j + dy, 28, 40, 10, 2, j, i)
            for i in range(3) for j in range(3)
        ]
        self.left_view = [
            LeftView(235 + 33*j + dx, 185 + 46*i - 13*j + dy, 28, 40, 10, 4, i, j)
            for i in range(3) for j in range(3)
        ]
        self.top_view = [
            TopView(120 + 36*i + 40*j + dx, 140 + 12*i - 12*j + dy, 28, 10, 20, 0, j, i)
            for i in range(3) for j in range(3)
        ]
        self.back_view = [
            FrontView(420 + 35*i + dx, 150 - 13*i + 45*j + dy, 28, 40, -10, 3, j, 2-i)
            for i in range(3) for j in range(3)
        ]
        self.right_view = [
            LeftView(535 + 33*j + dx, 115 + 46*i + 13*j + dy, 28, 40, -10, 5, i, 2-j)
            for i in range(3) for j in range(3)
        ]
        self.bottom_view = [
            TopView(420 + 36*i + 40*j + dx, 290 + 12*i - 12*j + dy, 28, 10, 20, 1, i, 2-j)
            for i in range(3) for j in range(3)
        ]

    def process_events(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        shift = bool(event.mod & pygame.KMOD_SHIFT)
        if event.key in KEY_MAP:
            base = KEY_MAP[event.key]
            token = base + "'" if shift else base
            apply_moves(self.cube, token)
            self.last_action = token
        elif event.key == pygame.K_SPACE:
            seq = scramble(self.cube)
            self.last_action = "melange (" + str(len(seq.split())) + " mouvements)"
        elif event.key == pygame.K_n:
            self.cube = new_cube()
            self.last_action = "nouveau cube"

    def draw_title(self):
        title = self.title_font.render("Rubik's Cube 3x3", True, FG)
        rect = title.get_rect(center=(WINDOW_W // 2, 40))
        self.screen.blit(title, rect)
        pygame.draw.line(self.screen, PANEL_BORDER,
                         (60, 75), (WINDOW_W - 60, 75), 1)

    def draw_cubes(self):
        for view in self.top_view + self.left_view + self.front_view:
            view.draw(self.screen, self.cube)
        for view in self.bottom_view + self.right_view + self.back_view:
            view.draw(self.screen, self.cube)

        front_label = self.label_font.render("vue avant", True, MUTED)
        back_label = self.label_font.render("vue arriere", True, MUTED)
        self.screen.blit(front_label,
                         front_label.get_rect(center=(CUBE_DX + 225, CUBE_DY + 380)))
        self.screen.blit(back_label,
                         back_label.get_rect(center=(CUBE_DX + 525, CUBE_DY + 380)))

    def draw_help(self):
        panel_x, panel_y = WINDOW_W - 470, 100
        panel_w, panel_h = 400, 450
        panel = pygame.Rect(panel_x, panel_y, panel_w, panel_h)
        pygame.draw.rect(self.screen, PANEL_BG, panel, border_radius=10)
        pygame.draw.rect(self.screen, PANEL_BORDER, panel, width=1, border_radius=10)

        x = panel_x + 20
        y = panel_y + 20
        for label, desc in HELP_ROWS:
            if desc is None:
                if label:
                    surf = self.section_font.render(label, True, ACCENT)
                    self.screen.blit(surf, (x, y))
                    y += 30
                else:
                    y += 12
            else:
                k = self.mono_font.render(label, True, FG)
                d = self.mono_font.render(desc, True, MUTED)
                self.screen.blit(k, (x, y))
                self.screen.blit(d, (x + 150, y))
                y += 26

    def draw_status(self):
        if is_solve(self.cube):
            text = "cube resolu"
            color = OK_GREEN
        elif self.last_action:
            text = "derniere action : " + self.last_action
            color = FG
        else:
            text = "pret"
            color = MUTED
        surf = self.status_font.render(text, True, color)
        rect = surf.get_rect(center=(WINDOW_W // 2, WINDOW_H - 40))
        self.screen.blit(surf, rect)

    def draw(self):
        self.screen.fill(BG)
        self.draw_title()
        self.draw_cubes()
        self.draw_help()
        self.draw_status()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.process_events(event)
            self.draw()
            pygame.display.flip()


App().run()
