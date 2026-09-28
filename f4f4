import sys
import random
import math
import json
import os
import pygame

IS_ANDROID = (
    "ANDROID_ARGUMENT" in os.environ
    or "ANDROID_PRIVATE" in os.environ
)

pygame.init()

# ============================================================
# ОСНОВНЫЕ НАСТРОЙКИ
# ============================================================

BASE_W = 600
BASE_H = 750

RESOLUTIONS = [
    (600, 750),
    (720, 900),
    (800, 1000),
    (1024, 768),
    (1280, 720),
    (1600, 900),
    (1920, 1080),
    (2560, 1440),
    (3840, 2160),
]

TURN_TIME_LIMIT = 7.0

if IS_ANDROID:
    # SDL2 chooses the real device size; our 600x750 canvas is scaled
    # proportionally by the existing adaptive renderer below.
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(
        RESOLUTIONS[0],
        pygame.RESIZABLE
    )

pygame.display.set_caption("Tic-Tac-Toe")
try:
    pygame.display.set_minimum_size((400, 500))
except (AttributeError, pygame.error):
    pass

clock = pygame.time.Clock()

# Базовый canvas существует ДО всех функций
canvas = pygame.Surface((BASE_W, BASE_H), pygame.SRCALPHA)

fullscreen = False


# ============================================================
# ЦВЕТА
# ============================================================

THEMES = {
    "DARK": {
        "bg": (8, 8, 8),
        "panel": (15, 15, 15),
        "panel2": (23, 23, 23),
        "hover": (38, 38, 38),
        "pressed": (52, 52, 52),
        "text": (250, 250, 250),
        "muted": (145, 145, 145),
        "line": (58, 58, 58),
        "x": (250, 250, 250),
        "o": (175, 175, 175),
        "accent": (250, 250, 250),
    },

    "LIGHT": {
        "bg": (248, 248, 248),
        "panel": (255, 255, 255),
        "panel2": (236, 236, 236),
        "hover": (218, 218, 218),
        "pressed": (198, 198, 198),
        "text": (8, 8, 8),
        "muted": (105, 105, 105),
        "line": (202, 202, 202),
        "x": (8, 8, 8),
        "o": (75, 75, 75),
        "accent": (8, 8, 8),
    }
}

theme_name = "DARK"


NICK_COLORS = [
    ("Cream", (245, 240, 230)),
    ("Mint", (168, 218, 185)),
    ("Blue", (162, 210, 230)),
    ("Lavender", (200, 180, 225)),
    ("Sand", (245, 220, 150)),
    ("Peach", (240, 168, 160)),
    ("Pink", (242, 180, 205)),
]

nick_color_index = 0


def theme():
    return THEMES[theme_name]


# ============================================================
# ШРИФТЫ
# ============================================================

FONT_TITLE = pygame.font.SysFont(
    "Segoe UI",
    34,
    bold=True
)

FONT_BIG = pygame.font.SysFont(
    "Segoe UI",
    76,
    bold=True
)

FONT_BUTTON = pygame.font.SysFont(
    "Segoe UI",
    17,
    bold=True
)

FONT_NORMAL = pygame.font.SysFont(
    "Segoe UI",
    16
)

FONT_SMALL = pygame.font.SysFont(
    "Segoe UI",
    13
)


# ============================================================
# ЛОКАЛИЗАЦИЯ
# ============================================================

LANG = "RU"

TEXT = {
    "RU": {
        "title": "КРЕСТИКИ — НОЛИКИ",
        "online": "ОНЛАЙН",
        "local": "ЛОКАЛЬНАЯ ИГРА",
        "bot": "БОТ",
        "brain": "УМ",
        "searching": "ПОДБОР СОПЕРНИКА...",
        "profile": "ПРОФИЛЬ",
        "settings": "НАСТРОЙКИ",
        "history": "ИСТОРИЯ",
        "back": "НАЗАД",
        "save": "СОХРАНИТЬ",
        "nickname": "Никнейм",
        "nick_color": "Цвет ника",
        "theme": "Тема",
        "language": "Язык",
        "resolution": "Разрешение",
        "dark": "Тёмная",
        "light": "Светлая",
        "player1": "Игрок 1",
        "player2": "Игрок 2",
        "your_turn": "Ваш ход",
        "turn": "Ход",
        "winner": "Победитель",
        "draw": "Ничья",
        "restart": "НОВАЯ ИГРА",
        "menu": "МЕНЮ",
        "surrender": "СДАТЬСЯ",
        "search": "ПОИСК СОПЕРНИКА",
        "victory": "ПОБЕДА",
        "defeat": "ПОРАЖЕНИЕ",
        "no_history": "История пока пуста",
        "fullscreen": "Полный экран",
        "change": "Изменить",
        "local_hint": "Два игрока на одном устройстве",
        "round": "Раунд",
        "match_result": "РЕЗУЛЬТАТ МАТЧА",
        "you_win": "ПОБЕДА",
        "you_lose": "ПОРАЖЕНИЕ",
        "match_draw": "НИЧЬЯ",
        "mmr": "MMR",
        "new_match": "НОВЫЙ МАТЧ",
        "saved": "СОХРАНЕНО",
        "exit": "ВЫХОД",
    },

    "EN": {
        "title": "TIC — TAC — TOE",
        "online": "ONLINE",
        "local": "LOCAL GAME",
        "bot": "BOT",
        "brain": "BRAIN",
        "searching": "FINDING OPPONENT...",
        "profile": "PROFILE",
        "settings": "SETTINGS",
        "history": "HISTORY",
        "back": "BACK",
        "save": "SAVE",
        "nickname": "Nickname",
        "nick_color": "Nick color",
        "theme": "Theme",
        "language": "Language",
        "dark": "Dark",
        "light": "Light",
        "player1": "Player 1",
        "player2": "Player 2",
        "your_turn": "Your turn",
        "turn": "Turn",
        "winner": "Winner",
        "draw": "Draw",
        "restart": "NEW GAME",
        "menu": "MENU",
        "surrender": "SURRENDER",
        "search": "SEARCHING",
        "victory": "VICTORY",
        "defeat": "DEFEAT",
        "no_history": "History is empty",
        "fullscreen": "Fullscreen",
        "change": "Change",
        "local_hint": "Two players on one device",
        "round": "Round",
        "match_result": "MATCH RESULT",
        "you_win": "VICTORY",
        "you_lose": "DEFEAT",
        "match_draw": "DRAW",
        "mmr": "MMR",
        "new_match": "NEW MATCH",
        "saved": "SAVED",
        "exit": "EXIT",
    }
}


def tr(key):
    return TEXT[LANG].get(key, key)


# ============================================================
# ИГРОВЫЕ ДАННЫЕ
# ============================================================

player_name = f"Player{random.randint(1000, 9999)}"
player2_name = "Player 2"

player_mmr = 1000

history = []

game_state = "MENU"

# LOCAL / ONLINE
game_mode = "LOCAL"

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]

current_player = "X"

winner = None
game_finished = False

round_score_x = 0
round_score_o = 0

# Онлайн-матч состоит ровно из 3 раундов.
round_number = 1
TOTAL_ROUNDS = 3
round_pause_until = 0
round_results = []  # Результат каждого завершённого онлайн-раунда
match_mmr_delta = 0
match_result = "DRAW"

# В онлайне бот играет за O
bot_thinking = False
bot_move_time = 0
bot_delay = 650
bot_name = "NOVA_404"
bot_intelligence = 75

# Таймер
turn_started = 0
time_left = TURN_TIME_LIMIT

# Анимация
animations = []

# Кнопки
button_states = {}

# Профиль
nickname_editing = False

# Выбор разрешения
resolution_index = 0

# Состояние сохранения настроек
settings_saved_until = 0

# Android stores writable app data in its private app directory.
# On desktop we keep the JSON next to the script as before.
if IS_ANDROID:
    try:
        from android.storage import app_storage_path
        APP_DATA_DIR = app_storage_path()
    except Exception:
        APP_DATA_DIR = os.path.expanduser("~")
else:
    APP_DATA_DIR = os.path.dirname(os.path.abspath(__file__))

os.makedirs(APP_DATA_DIR, exist_ok=True)
SETTINGS_FILE = os.path.join(APP_DATA_DIR, "ttt_settings.json")


# ============================================================
# СОХРАНЕНИЕ НАСТРОЕК
# ============================================================

def save_settings():

    global settings_saved_until

    data = {
        "player_name": player_name.strip() or f"Player{random.randint(1000, 9999)}",
        "theme_name": theme_name,
        "language": LANG,
        "nick_color_index": nick_color_index,
        "resolution_index": resolution_index,
        "player_mmr": player_mmr,
        "history": history[-50:],
    }

    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        settings_saved_until = pygame.time.get_ticks() + 1600
    except (OSError, TypeError, ValueError):
        settings_saved_until = 0


def load_settings():

    global player_name
    global theme_name
    global LANG
    global nick_color_index
    global resolution_index
    global player_mmr
    global history

    if not os.path.exists(SETTINGS_FILE):
        return

    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        saved_name = str(data.get("player_name", "")).strip()
        if saved_name:
            player_name = saved_name[:16]

        saved_theme = data.get("theme_name")
        if saved_theme in THEMES:
            theme_name = saved_theme

        saved_lang = data.get("language")
        if saved_lang in TEXT:
            LANG = saved_lang

        saved_color = int(data.get("nick_color_index", 0))
        nick_color_index = saved_color % len(NICK_COLORS)

        saved_resolution = int(data.get("resolution_index", 0))
        resolution_index = saved_resolution % len(RESOLUTIONS)

        saved_mmr = int(data.get("player_mmr", 1000))
        player_mmr = max(0, saved_mmr)

        saved_history = data.get("history", [])
        if isinstance(saved_history, list):
            history = [item for item in saved_history if isinstance(item, dict)][-50:]

    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        pass


load_settings()


# ============================================================
# УТИЛИТЫ
# ============================================================

def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))


def clamp_color(color):
    return tuple(
        clamp(int(v), 0, 255)
        for v in color[:3]
    )


def mouse_position():
    sw, sh = screen.get_size()

    if sw <= 0 or sh <= 0:
        return 0, 0

    # Canvas сохраняет пропорции 600x750 и центрируется в окне.
    # Поэтому учитываем и масштаб, и letterbox-смещение.
    scale = min(sw / BASE_W, sh / BASE_H)
    if scale <= 0:
        return 0, 0

    new_w = BASE_W * scale
    new_h = BASE_H * scale
    offset_x = (sw - new_w) / 2
    offset_y = (sh - new_h) / 2

    mx, my = pygame.mouse.get_pos()
    x = int((mx - offset_x) / scale)
    y = int((my - offset_y) / scale)

    return (
        clamp(x, 0, BASE_W - 1),
        clamp(y, 0, BASE_H - 1),
    )


def draw_text(
    surface,
    text,
    font,
    color,
    center,
):
    img = font.render(
        str(text),
        True,
        clamp_color(color)
    )

    rect = img.get_rect(
        center=center
    )

    surface.blit(img, rect)


def rounded_rect(
    surface,
    color,
    rect,
    radius=10,
    width=0
):
    pygame.draw.rect(
        surface,
        clamp_color(color),
        rect,
        width,
        border_radius=radius
    )


def lerp(a, b, speed):
    return a + (b - a) * speed


# ============================================================
# АНИМАЦИИ КНОПОК
# ============================================================

class AnimatedButton:

    def __init__(
        self,
        rect,
        text,
        action=None,
        radius=10
    ):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.action = action
        self.radius = radius

        self.hover = 0.0
        self.press = 0.0
        self.glow = 0.0
        self.ripple = 0.0

    def update(self, dt):
        mx, my = mouse_position()
        hovered = self.rect.collidepoint(mx, my)

        target_hover = 1.0 if hovered else 0.0
        speed = min(1.0, dt * 14.0)
        self.hover = lerp(self.hover, target_hover, speed)
        self.glow = lerp(self.glow, target_hover, min(1.0, dt * 10.0))
        self.press = lerp(self.press, 0.0, min(1.0, dt * 20.0))
        self.ripple = lerp(self.ripple, 0.0, min(1.0, dt * 5.0))

    def draw(self):
        t = theme()

        # Мягкое увеличение при наведении + физический offset при нажатии.
        scale = 1.0 + 0.018 * self.hover - 0.008 * self.press
        w = int(self.rect.width * scale)
        h = int(self.rect.height * scale)
        cx, cy = self.rect.center
        rect = pygame.Rect(0, 0, w, h)
        rect.center = (cx, cy + int(self.press * 2))

        base = t["panel2"]
        hover_color = t["hover"]
        color = tuple(
            int(base[i] + (hover_color[i] - base[i]) * self.hover)
            for i in range(3)
        )

        # Тень / глубина.
        shadow = pygame.Surface((w + 12, h + 12), pygame.SRCALPHA)
        pygame.draw.rect(
            shadow,
            (0, 0, 0, int(55 * (0.35 + self.hover))),
            (6, 7, w, h),
            border_radius=self.radius + 2
        )
        canvas.blit(shadow, (rect.x - 6, rect.y - 5))

        rounded_rect(canvas, color, rect, self.radius)

        # Живая рамка.
        if self.hover > 0.01:
            overlay = pygame.Surface(rect.size, pygame.SRCALPHA)
            alpha = int(70 * self.hover)
            pygame.draw.rect(
                overlay,
                (*t["accent"], alpha),
                overlay.get_rect(),
                1,
                border_radius=self.radius
            )
            canvas.blit(overlay, rect.topleft)

        # Короткая вспышка после клика.
        if self.ripple > 0.01:
            overlay = pygame.Surface(rect.size, pygame.SRCALPHA)
            radius = int((1.0 - self.ripple) * max(w, h) * 0.75)
            alpha = int(40 * self.ripple)
            pygame.draw.circle(
                overlay,
                (*t["accent"], alpha),
                (w // 2, h // 2),
                max(1, radius),
                2
            )
            canvas.blit(overlay, rect.topleft)

        draw_text(
            canvas,
            self.text,
            FONT_BUTTON,
            t["text"],
            rect.center
        )

    def click(self):
        self.press = 1.0
        self.ripple = 1.0
        if self.action:
            self.action()


# ============================================================
# АНИМАЦИЯ X / O
# ============================================================

class MarkAnimation:

    def __init__(
        self,
        x,
        y,
        symbol
    ):
        self.x = x
        self.y = y
        self.symbol = symbol

        self.time = 0.0
        self.duration = 0.18

    def update(self, dt):

        self.time += dt

    def draw(self):

        t = theme()

        progress = clamp(
            self.time / self.duration,
            0.0,
            1.0
        )

        # smoothstep
        progress = (
            progress *
            progress *
            (3 - 2 * progress)
        )

        scale = 0.55 + 0.45 * progress

        font_size = max(
            1,
            int(76 * scale)
        )

        font = pygame.font.SysFont(
            "Segoe UI",
            font_size,
            bold=True
        )

        color = (
            t["x"]
            if self.symbol == "X"
            else t["o"]
        )

        draw_text(
            canvas,
            self.symbol,
            font,
            color,
            (self.x, self.y)
        )


# ============================================================
# ЧАСТИЦЫ
# ============================================================

class Particle:

    def __init__(
        self,
        x,
        y,
        color
    ):
        self.x = float(x)
        self.y = float(y)

        angle = random.random() * math.tau
        speed = random.uniform(
            20,
            70
        )

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.life = random.uniform(
            0.25,
            0.55
        )

        self.max_life = self.life

        self.size = random.uniform(
            1.0,
            3.0
        )

        self.color = clamp_color(
            color
        )

    def update(self, dt):

        self.x += self.vx * dt
        self.y += self.vy * dt

        self.vx *= 0.97
        self.vy *= 0.97

        self.life -= dt

    def draw(self):

        if self.life <= 0:
            return

        alpha = int(
            255 *
            clamp(
                self.life / self.max_life,
                0,
                1
            )
        )

        surface = pygame.Surface(
            (
                max(2, int(self.size * 2)),
                max(2, int(self.size * 2))
            ),
            pygame.SRCALPHA
        )

        color = (
            self.color[0],
            self.color[1],
            self.color[2],
            alpha
        )

        pygame.draw.circle(
            surface,
            color,
            (
                surface.get_width() // 2,
                surface.get_height() // 2
            ),
            max(
                1,
                int(self.size)
            )
        )

        canvas.blit(
            surface,
            (
                int(self.x - self.size),
                int(self.y - self.size)
            )
        )


particles = []


def create_particles(x, y, color):

    for _ in range(12):

        particles.append(
            Particle(
                x,
                y,
                color
            )
        )


def update_particles(dt):

    for p in particles:
        p.update(dt)

    particles[:] = [
        p for p in particles
        if p.life > 0
    ]


def draw_particles():

    for p in particles:
        p.draw()


# ============================================================
# ИГРОВОЕ ПОЛЕ
# ============================================================

BOARD_RECT = pygame.Rect(
    50,
    190,
    500,
    500
)


def cell_rect(row, col):

    size = BOARD_RECT.width // 3

    return pygame.Rect(
        BOARD_RECT.x + col * size + 5,
        BOARD_RECT.y + row * size + 5,
        size - 10,
        size - 10
    )


def reset_board():

    global board
    global current_player
    global winner
    global game_finished
    global turn_started
    global time_left
    global bot_thinking

    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]

    current_player = (
        "X"
        if game_mode == "ONLINE"
        else random.choice(["X", "O"])
    )

    winner = None
    game_finished = False

    bot_thinking = False

    turn_started = pygame.time.get_ticks()

    time_left = TURN_TIME_LIMIT

    animations.clear()


def start_local_game():

    global game_mode
    global game_state

    game_mode = "LOCAL"
    game_state = "GAME"

    reset_board()


def choose_bot_intelligence(mmr):
    """
    Подбирает силу бота по MMR игрока.

    На низком MMR слабые боты встречаются заметнее, но средние/сильные
    всё равно суммарно преобладают. Чем выше MMR, тем сильнее смещается
    подбор в сторону сильных соперников.
    """
    mmr = max(0, int(mmr))
    progress = clamp((mmr - 700) / 1300.0, 0.0, 1.0)

    # Суммарно средние+сильные всегда чаще слабых.
    weak_weight = 18 - 12 * progress
    medium_weight = 57 - 27 * progress
    strong_weight = 25 + 39 * progress

    bucket = random.choices(
        ["weak", "medium", "strong"],
        weights=[weak_weight, medium_weight, strong_weight],
        k=1
    )[0]

    if bucket == "weak":
        return random.randint(38, 57)
    if bucket == "medium":
        return random.randint(58, 79)
    return random.randint(80, 98)


def start_online_game():

    global game_mode
    global game_state
    global bot_name
    global bot_intelligence
    global bot_delay
    global round_number
    global round_score_x
    global round_score_o
    global match_mmr_delta
    global match_result
    global round_results

    bot_names = [
        "NOVA_404", "PixelFox", "ZeroMind", "NightByte",
        "KrossX", "Mori_77", "WhiteRook", "EchoNine",
        "GhostLine", "Axiom", "Vektor", "MonoCat",
        "ByteWolf", "NullPlayer", "BlackDot"
    ]

    game_mode = "ONLINE"
    game_state = "GAME"
    round_number = 1
    round_score_x = 0
    round_score_o = 0
    round_results = []
    match_mmr_delta = 0
    match_result = "DRAW"

    # Каждый онлайн-матч получает нового виртуального соперника.
    bot_name = random.choice(bot_names)
    bot_intelligence = choose_bot_intelligence(player_mmr)

    if bot_intelligence < 55:
        bot_delay = random.randint(650, 1050)
    elif bot_intelligence < 80:
        bot_delay = random.randint(500, 850)
    else:
        bot_delay = random.randint(380, 700)

    reset_board()


# ============================================================
# ПОБЕДИТЕЛЬ
# ============================================================

def get_winner():

    # строки
    for row in board:

        if (
            row[0] != "" and
            row[0] == row[1] == row[2]
        ):
            return row[0]

    # столбцы
    for col in range(3):

        if (
            board[0][col] != "" and
            board[0][col] ==
            board[1][col] ==
            board[2][col]
        ):
            return board[0][col]

    # диагонали
    if (
        board[0][0] != "" and
        board[0][0] ==
        board[1][1] ==
        board[2][2]
    ):
        return board[0][0]

    if (
        board[0][2] != "" and
        board[0][2] ==
        board[1][1] ==
        board[2][0]
    ):
        return board[0][2]

    # ничья
    if all(
        board[r][c] != ""
        for r in range(3)
        for c in range(3)
    ):
        return "DRAW"

    return None


def finish_game(result):

    global winner
    global game_finished
    global round_score_x
    global round_score_o
    global round_pause_until
    global game_state
    global match_mmr_delta
    global match_result
    global player_mmr

    if game_finished:
        return

    winner = result
    game_finished = True

    if game_mode == "ONLINE":
        if result == "X":
            round_score_x += 1
        elif result == "O":
            round_score_o += 1

        # Результат нужен только для нижнего индикатора трёх раундов.
        round_results.append(result)

        # После каждого из первых двух раундов автоматически запускаем следующий.
        if round_number < TOTAL_ROUNDS:
            round_pause_until = pygame.time.get_ticks() + 1000
        else:
            if round_score_x > round_score_o:
                match_result = "X"
                match_mmr_delta = 25
            elif round_score_o > round_score_x:
                match_result = "O"
                match_mmr_delta = -20
            else:
                match_result = "DRAW"
                match_mmr_delta = 0

            player_mmr = max(0, player_mmr + match_mmr_delta)
            game_state = "RESULT"

            history.append({
                "result": (
                    tr("victory") if match_result == "X"
                    else tr("defeat") if match_result == "O"
                    else tr("draw")
                ),
                "score": f"{round_score_x} — {round_score_o}",
                "opponent": bot_name,
                "color": (
                    theme()["x"] if match_result == "X"
                    else theme()["o"] if match_result == "O"
                    else theme()["muted"]
                ),
            })

            # Прогресс матча сразу записывается на диск, а не только при выходе.
            save_settings()

    t = theme()

    if result == "X":
        create_particles(BASE_W // 2, BOARD_RECT.centery, t["x"])
    elif result == "O":
        create_particles(BASE_W // 2, BOARD_RECT.centery, t["o"])


# ============================================================
# ХОД
# ============================================================

def make_move(row, col):

    global current_player
    global turn_started
    global time_left

    if game_finished:
        return

    if board[row][col] != "":
        return

    if game_mode == "ONLINE":
        if current_player != "X":
            return

    board[row][col] = current_player

    rect = cell_rect(
        row,
        col
    )

    animations.append(
        MarkAnimation(
            rect.centerx,
            rect.centery,
            current_player
        )
    )

    color = (
        theme()["x"]
        if current_player == "X"
        else theme()["o"]
    )

    create_particles(
        rect.centerx,
        rect.centery,
        color
    )

    result = get_winner()

    if result:
        finish_game(result)
        return

    current_player = (
        "O"
        if current_player == "X"
        else "X"
    )

    turn_started = pygame.time.get_ticks()

    time_left = TURN_TIME_LIMIT

    if (
        game_mode == "ONLINE"
        and current_player == "O"
    ):
        start_bot_thinking()


# ============================================================
# БОТ
# ============================================================

def start_bot_thinking():

    global bot_thinking
    global bot_move_time
    global bot_delay

    bot_thinking = True

    bot_move_time = (
        pygame.time.get_ticks()
    )

    bot_delay = random.randint(
        450,
        850
    )


def bot_move():

    global current_player
    global bot_thinking

    if game_finished:
        bot_thinking = False
        return

    empty = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if board[r][c] == ""
    ]

    if not empty:
        bot_thinking = False
        return

    move = find_best_move()

    if move is None:
        move = random.choice(
            empty
        )

    row, col = move

    board[row][col] = "O"

    rect = cell_rect(
        row,
        col
    )

    animations.append(
        MarkAnimation(
            rect.centerx,
            rect.centery,
            "O"
        )
    )

    create_particles(
        rect.centerx,
        rect.centery,
        theme()["o"]
    )

    bot_thinking = False

    result = get_winner()

    if result:
        finish_game(result)
        return

    current_player = "X"

    global turn_started
    global time_left

    turn_started = pygame.time.get_ticks()
    time_left = TURN_TIME_LIMIT


def find_best_move():
    """Выбор хода зависит от случайного уровня ума соперника."""
    empty = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if board[r][c] == ""
    ]

    if not empty:
        return None

    # Низкий уровень иногда ошибается и играет случайно.
    if bot_intelligence < 55:
        if random.random() < 0.72:
            return random.choice(empty)
        return find_heuristic_move()

    # Средний — старается выиграть/заблокировать, но не идеален.
    if bot_intelligence < 80:
        if random.random() < 0.18:
            return random.choice(empty)
        return find_heuristic_move()

    # Высокий — почти всегда играет оптимально.
    return find_minimax_move()


def find_heuristic_move():
    empty = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if board[r][c] == ""
    ]

    for r, c in empty:
        board[r][c] = "O"
        if get_winner() == "O":
            board[r][c] = ""
            return r, c
        board[r][c] = ""

    for r, c in empty:
        board[r][c] = "X"
        if get_winner() == "X":
            board[r][c] = ""
            return r, c
        board[r][c] = ""

    if board[1][1] == "":
        return 1, 1

    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    free_corners = [p for p in corners if board[p[0]][p[1]] == ""]
    if free_corners:
        return random.choice(free_corners)

    return random.choice(empty)


def minimax_score(player, depth=0):
    result = get_winner()
    if result == "O":
        return 10 - depth
    if result == "X":
        return depth - 10
    if result == "DRAW":
        return 0

    empty = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if board[r][c] == ""
    ]

    if player == "O":
        best = -999
        for r, c in empty:
            board[r][c] = "O"
            best = max(best, minimax_score("X", depth + 1))
            board[r][c] = ""
        return best

    best = 999
    for r, c in empty:
        board[r][c] = "X"
        best = min(best, minimax_score("O", depth + 1))
        board[r][c] = ""
    return best


def find_minimax_move():
    empty = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if board[r][c] == ""
    ]

    best_score = -999
    best_moves = []

    for r, c in empty:
        board[r][c] = "O"
        score = minimax_score("X")
        board[r][c] = ""

        if score > best_score:
            best_score = score
            best_moves = [(r, c)]
        elif score == best_score:
            best_moves.append((r, c))

    return random.choice(best_moves) if best_moves else None


# ============================================================
# ТАЙМЕР
# ============================================================

def update_timer():

    global time_left

    if game_finished:
        return

    if game_mode != "ONLINE":
        return

    if bot_thinking:
        return

    elapsed = (
        pygame.time.get_ticks()
        - turn_started
    ) / 1000.0

    time_left = max(
        0,
        TURN_TIME_LIMIT - elapsed
    )

    if time_left <= 0:

        if current_player == "X":
            finish_game("O")
        else:
            finish_game("X")


# ============================================================
# HEADER
# ============================================================

def draw_header(title=None):

    t = theme()

    title = title or tr("title")

    draw_text(
        canvas,
        title,
        FONT_TITLE,
        t["text"],
        (BASE_W // 2, 50)
    )


def draw_back_button():

    button = AnimatedButton(
        (
            30,
            25,
            100,
            38
        ),
        tr("back"),
        go_menu
    )

    button.update(1 / 60)
    button.draw()

    return button


# ============================================================
# МЕНЮ
# ============================================================

menu_buttons = []


def go_menu():

    global game_state
    global nickname_editing

    nickname_editing = False
    game_state = "MENU"


def exit_game():

    global running

    save_settings()
    running = False


def open_settings():

    global game_state

    game_state = "SETTINGS"


def open_profile():

    global game_state

    game_state = "PROFILE"


def open_history():

    global game_state

    game_state = "HISTORY"


def draw_menu():

    t = theme()

    canvas.fill(
        t["bg"]
    )

    draw_text(
        canvas,
        tr("title"),
        FONT_TITLE,
        t["text"],
        (BASE_W // 2, 115)
    )

    color = NICK_COLORS[
        nick_color_index
    ][1]

    draw_text(
        canvas,
        f"{player_name}  ·  {player_mmr} MMR",
        FONT_SMALL,
        color,
        (BASE_W // 2, 150)
    )

    # Минималистичные кнопки
    y = 225

    buttons = [
        AnimatedButton(
            (150, y, 300, 52),
            tr("online"),
            start_online_game
        ),

        AnimatedButton(
            (150, y + 68, 300, 52),
            tr("local"),
            start_local_game
        ),

        AnimatedButton(
            (150, y + 136, 300, 52),
            tr("profile"),
            open_profile
        ),

        AnimatedButton(
            (150, y + 204, 300, 52),
            tr("settings"),
            open_settings
        ),

        AnimatedButton(
            (150, y + 272, 300, 52),
            tr("exit"),
            exit_game
        ),
    ]

    menu_buttons.clear()
    menu_buttons.extend(buttons)

    for button in buttons:
        button.update(1 / 60)
        button.draw()

    # Маленькая подпись
    draw_text(
        canvas,
        "F11  ·  Fullscreen",
        FONT_SMALL,
        t["muted"],
        (BASE_W // 2, 690)
    )


# ============================================================
# ПРОФИЛЬ
# ============================================================

profile_buttons = []


def change_nick_color():

    global nick_color_index

    nick_color_index = (
        nick_color_index + 1
    ) % len(NICK_COLORS)


def save_profile():

    global player_name

    player_name = player_name.strip()

    if not player_name:
        player_name = f"Player{random.randint(1000, 9999)}"

    player_name = player_name[:16]
    save_settings()
    go_menu()


def draw_profile():

    t = theme()

    canvas.fill(
        t["bg"]
    )

    draw_header(
        tr("profile")
    )

    draw_back_button()

    # Карточка профиля — без перекрывающихся элементов.
    panel = pygame.Rect(
        70,
        120,
        460,
        500
    )

    rounded_rect(
        canvas,
        t["panel"],
        panel,
        16
    )

    # Подпись и поле никнейма находятся в разных строках.
    draw_text(
        canvas,
        tr("nickname"),
        FONT_SMALL,
        t["muted"],
        (BASE_W // 2, 160)
    )

    name_rect = pygame.Rect(
        120,
        180,
        360,
        50
    )

    rounded_rect(
        canvas,
        t["panel2"],
        name_rect,
        10
    )

    name_color = NICK_COLORS[
        nick_color_index
    ][1]

    draw_text(
        canvas,
        player_name
        + (
            "|"
            if nickname_editing
            and (pygame.time.get_ticks() // 500) % 2 == 0
            else ""
        ),
        FONT_NORMAL,
        name_color,
        name_rect.center
    )

    color_button = AnimatedButton(
        (150, 265, 300, 50),
        f"{tr('nick_color')}: {NICK_COLORS[nick_color_index][0]}",
        change_nick_color
    )

    history_button = AnimatedButton(
        (150, 330, 300, 50),
        tr("history"),
        open_history
    )

    save_button = AnimatedButton(
        (150, 395, 300, 50),
        tr("save"),
        save_profile
    )

    profile_buttons.clear()

    for button in [color_button, history_button, save_button]:
        profile_buttons.append(button)
        button.update(1 / 60)
        button.draw()




# ============================================================
# НАСТРОЙКИ
# ============================================================

settings_buttons = []


def toggle_theme():

    global theme_name

    theme_name = (
        "LIGHT"
        if theme_name == "DARK"
        else "DARK"
    )


def toggle_language():

    global LANG

    LANG = (
        "EN"
        if LANG == "RU"
        else "RU"
    )


def change_resolution():

    global resolution_index
    global screen

    if IS_ANDROID:
        # Android controls the physical display resolution.
        return

    resolution_index = (
        resolution_index + 1
    ) % len(RESOLUTIONS)

    if not fullscreen:

        screen = pygame.display.set_mode(
            RESOLUTIONS[resolution_index],
            pygame.RESIZABLE
        )
        pygame.display.set_caption("Tic-Tac-Toe")


def toggle_fullscreen():

    global fullscreen
    global screen

    if IS_ANDROID:
        fullscreen = True
        return

    fullscreen = not fullscreen

    if fullscreen:

        screen = pygame.display.set_mode(
            (0, 0),
            pygame.FULLSCREEN
        )

    else:

        screen = pygame.display.set_mode(
            RESOLUTIONS[resolution_index],
            pygame.RESIZABLE
        )
        try:
            pygame.display.set_caption("Tic-Tac-Toe")
        except pygame.error:
            pass


def draw_settings():

    t = theme()

    canvas.fill(
        t["bg"]
    )

    draw_header(
        tr("settings")
    )

    draw_back_button()

    buttons = [
        AnimatedButton(
            (130, 145, 340, 50),
            f"{tr('theme')}: "
            + (
                tr("dark")
                if theme_name == "DARK"
                else tr("light")
            ),
            toggle_theme
        ),

        AnimatedButton(
            (130, 210, 340, 50),
            tr("language"),
            toggle_language
        ),

        AnimatedButton(
            (130, 275, 340, 50),
            f"{tr('resolution')}: "
            f"{RESOLUTIONS[resolution_index][0]}"
            f"x"
            f"{RESOLUTIONS[resolution_index][1]}",
            change_resolution
        ),

        AnimatedButton(
            (130, 340, 340, 50),
            tr("fullscreen"),
            toggle_fullscreen
        ),

        AnimatedButton(
            (130, 405, 340, 50),
            tr("save"),
            save_settings
        ),
    ]

    settings_buttons.clear()

    for button in buttons:

        settings_buttons.append(
            button
        )

        button.update(1 / 60)

        button.draw()

    if pygame.time.get_ticks() < settings_saved_until:
        draw_text(
            canvas,
            tr("saved"),
            FONT_SMALL,
            t["text"],
            (BASE_W // 2, 480)
        )


# ============================================================
# ИСТОРИЯ
# ============================================================

def draw_history():

    t = theme()

    canvas.fill(
        t["bg"]
    )

    draw_header(
        tr("history")
    )

    draw_back_button()

    if not history:

        draw_text(
            canvas,
            tr("no_history"),
            FONT_NORMAL,
            t["muted"],
            (
                BASE_W // 2,
                BASE_H // 2
            )
        )

        return

    y = 150

    for item in history[-7:]:

        panel = pygame.Rect(
            70,
            y,
            460,
            65
        )

        rounded_rect(
            canvas,
            t["panel"],
            panel,
            10
        )

        draw_text(
            canvas,
            item["result"],
            FONT_BUTTON,
            item["color"],
            (
                180,
                y + 23
            )
        )

        opponent = item.get("opponent", "BOT")

        draw_text(
            canvas,
            f"vs {opponent}",
            FONT_SMALL,
            t["muted"],
            (
                285,
                y + 23
            )
        )

        draw_text(
            canvas,
            item["score"],
            FONT_SMALL,
            t["muted"],
            (
                455,
                y + 23
            )
        )

        y += 78


# ============================================================
# ИГРА
# ============================================================

game_buttons = []


def draw_round_indicator():
    """Три полоски внизу: текущий и завершённые онлайн-раунды."""
    if game_mode != "ONLINE":
        return

    t = theme()
    bar_w = 92
    bar_h = 7
    gap = 12
    total_w = bar_w * TOTAL_ROUNDS + gap * (TOTAL_ROUNDS - 1)
    start_x = (BASE_W - total_w) // 2
    y = BASE_H - 53

    for i in range(TOTAL_ROUNDS):
        rect = pygame.Rect(
            start_x + i * (bar_w + gap),
            y,
            bar_w,
            bar_h
        )

        if i < len(round_results):
            result = round_results[i]
            color = (
                t["x"] if result == "X"
                else t["o"] if result == "O"
                else t["muted"]
            )
            rounded_rect(canvas, color, rect, 4)
        elif i == round_number - 1:
            # Текущий раунд — контур.
            rounded_rect(canvas, t["panel2"], rect, 4)
            pygame.draw.rect(
                canvas,
                t["text"],
                rect,
                width=1,
                border_radius=4
            )
        else:
            rounded_rect(canvas, t["line"], rect, 4)


def surrender_online_game():
    """Сдаться в онлайне: мгновенно завершить матч поражением и сохранить MMR/историю."""
    global game_finished
    global winner
    global match_result
    global match_mmr_delta
    global player_mmr
    global game_state
    global bot_thinking

    if game_mode != "ONLINE" or game_finished or game_state != "GAME":
        return

    game_finished = True
    winner = "O"
    bot_thinking = False
    match_result = "O"
    match_mmr_delta = -20
    player_mmr = max(0, player_mmr + match_mmr_delta)
    game_state = "RESULT"

    history.append({
        "result": tr("defeat"),
        "score": f"{round_score_x} — {round_score_o}",
        "opponent": bot_name,
        "color": theme()["o"],
    })
    save_settings()


def restart_game():

    reset_board()


def draw_game():

    t = theme()

    canvas.fill(
        t["bg"]
    )

    # Верхняя строка
    draw_text(
        canvas,
        (
            f"{player_name}  ·  {player2_name}"
            if game_mode == "LOCAL"
            else f"{player_name}  ·  {bot_name}"
        ),
        FONT_NORMAL,
        t["text"],
        (BASE_W // 2, 35)
    )

    # Счёт
    draw_text(
        canvas,
        f"{round_score_x}  —  {round_score_o}",
        FONT_SMALL,
        t["muted"],
        (BASE_W // 2, 65)
    )

    # Статус
    if game_finished:

        if winner == "DRAW":
            status = tr("draw")

        elif winner == "X":
            status = (
                player_name
                if game_mode == "ONLINE"
                else player_name
            )

            status = (
                f"{tr('winner')}: {status}"
            )

        else:
            status = (
                f"{tr('winner')}: "
                + (
                    bot_name
                    if game_mode == "ONLINE"
                    else player2_name
                )
            )

        draw_text(
            canvas,
            status,
            FONT_BUTTON,
            t["text"],
            (BASE_W // 2, 105)
        )

    else:

        if game_mode == "ONLINE":

            current = (
                player_name
                if current_player == "X"
                else bot_name
            )

        else:

            current = (
                player_name
                if current_player == "X"
                else player2_name
            )

        draw_text(
            canvas,
            f"{tr('turn')}: {current}",
            FONT_BUTTON,
            t["text"],
            (BASE_W // 2, 105)
        )

    # Таймер
    if game_mode == "ONLINE" and not game_finished:

        timer_text = f"{time_left:.1f}"

        draw_text(
            canvas,
            timer_text,
            FONT_SMALL,
            t["muted"],
            (BASE_W // 2, 130)
        )

    # Поле
    for r in range(3):

        for c in range(3):

            rect = cell_rect(
                r,
                c
            )

            mx, my = mouse_position()

            hovered = (
                rect.collidepoint(
                    mx,
                    my
                )
                and board[r][c] == ""
                and not game_finished
            )

            color = (
                t["hover"]
                if hovered
                else t["panel"]
            )

            rounded_rect(
                canvas,
                color,
                rect,
                14
            )

            symbol = board[r][c]

            if symbol:

                # Если есть активная анимация,
                # она отрисует символ.
                active = False

                for animation in animations:

                    if (
                        animation.x
                        == rect.centerx
                        and
                        animation.y
                        == rect.centery
                    ):
                        animation.draw()
                        active = True

                if not active:

                    draw_text(
                        canvas,
                        symbol,
                        FONT_BIG,
                        (
                            t["x"]
                            if symbol == "X"
                            else t["o"]
                        ),
                        rect.center
                    )

    # Нижняя кнопка: в онлайне только сдача.
    game_buttons.clear()

    if game_mode == "ONLINE":
        surrender = AnimatedButton(
            (110, 710, 380, 32),
            tr("surrender"),
            surrender_online_game
        )
        surrender.update(1 / 60)
        surrender.draw()
        game_buttons.append(surrender)
    else:
        restart = AnimatedButton(
            (110, 710, 180, 32),
            tr("restart"),
            restart_game
        )
        menu = AnimatedButton(
            (310, 710, 180, 32),
            tr("menu"),
            go_menu
        )
        restart.update(1 / 60)
        menu.update(1 / 60)
        restart.draw()
        menu.draw()
        game_buttons.extend([restart, menu])

    # Индикатор раундов находится в самом низу и не занимает место в шапке.
    draw_round_indicator()


# ============================================================
# ЭКРАН РЕЗУЛЬТАТА МАТЧА
# ============================================================

result_buttons = []

def draw_result():

    t = theme()
    canvas.fill(t["bg"])

    draw_text(canvas, tr("match_result"), FONT_TITLE, t["text"], (BASE_W // 2, 110))

    if match_result == "X":
        title = tr("you_win")
        title_color = t["x"]
    elif match_result == "O":
        title = tr("you_lose")
        title_color = t["o"]
    else:
        title = tr("match_draw")
        title_color = t["muted"]

    draw_text(canvas, title, FONT_BIG, title_color, (BASE_W // 2, 185))
    draw_text(canvas, f"{player_name}  —  {bot_name}", FONT_NORMAL, t["text"], (BASE_W // 2, 245))
    draw_text(canvas, f"{round_score_x}  —  {round_score_o}", FONT_TITLE, t["text"], (BASE_W // 2, 295))

    delta = f"+{match_mmr_delta}" if match_mmr_delta > 0 else str(match_mmr_delta)
    draw_text(canvas, f"{tr('mmr')}: {player_mmr}  ({delta})", FONT_BUTTON, t["text"], (BASE_W // 2, 350))

    result_buttons.clear()
    new_match = AnimatedButton((120, 440, 360, 52), tr("new_match"), start_online_game)
    menu = AnimatedButton((120, 510, 360, 52), tr("menu"), go_menu)

    new_match.update(1 / 60)
    menu.update(1 / 60)
    new_match.draw()
    menu.draw()
    result_buttons.extend([new_match, menu])


# ============================================================
# ОБНОВЛЕНИЕ АНИМАЦИЙ
# ============================================================

def update_animations(dt):

    for animation in animations:
        animation.update(dt)

    animations[:] = [
        animation
        for animation in animations
        if animation.time < animation.duration
    ]


# ============================================================
# КЛИКИ
# ============================================================

def handle_button_click(
    buttons
):

    mx, my = mouse_position()

    for button in buttons:

        if button.rect.collidepoint(
            mx,
            my
        ):
            button.click()
            return True

    return False


def handle_game_click():

    mx, my = mouse_position()

    # Кнопки
    if handle_button_click(
        game_buttons
    ):
        return

    if game_finished:
        return

    if game_mode == "ONLINE":
        if current_player != "X":
            return

    for r in range(3):

        for c in range(3):

            rect = cell_rect(
                r,
                c
            )

            if rect.collidepoint(
                mx,
                my
            ):

                make_move(
                    r,
                    c
                )

                return


# ============================================================
# ОБРАБОТКА KEYBOARD
# ============================================================

def handle_key(event):

    global player_name
    global nickname_editing

    if game_state != "PROFILE":
        return

    if not nickname_editing:
        return

    if event.key == pygame.K_RETURN:

        nickname_editing = False

        player_name = (
            player_name.strip()
            or f"Player{random.randint(1000, 9999)}"
        )

    elif event.key == pygame.K_BACKSPACE:

        player_name = player_name[:-1]

    elif event.unicode.isprintable():

        if len(player_name) < 16:

            player_name += (
                event.unicode
            )


# ============================================================
# РИСОВАНИЕ ПРОФИЛЯ + КЛАВИАТУРА
# ============================================================

def profile_click():

    global nickname_editing

    mx, my = mouse_position()

    # область имени
    name_rect = pygame.Rect(
        120,
        180,
        360,
        50
    )

    if name_rect.collidepoint(
        mx,
        my
    ):

        nickname_editing = True

        return True

    return False


# ============================================================
# MAIN LOOP
# ============================================================

running = True

while running:

    dt = clock.tick(144) / 1000.0

    dt = min(
        dt,
        0.033
    )

    # --------------------------------------------------------
    # UPDATE
    # --------------------------------------------------------

    update_particles(dt)
    update_animations(dt)

    if game_state == "GAME":

        # Пауза между раундами — даём увидеть результат текущего раунда.
        if (
            game_mode == "ONLINE"
            and game_finished
            and round_number < TOTAL_ROUNDS
            and pygame.time.get_ticks() >= round_pause_until
        ):
            round_number += 1
            reset_board()

        update_timer()

        if (
            game_mode == "ONLINE"
            and current_player == "O"
            and bot_thinking
            and not game_finished
        ):

            elapsed = (
                pygame.time.get_ticks()
                - bot_move_time
            )

            if elapsed >= bot_delay:

                bot_move()

    # --------------------------------------------------------
    # DRAW
    # --------------------------------------------------------

    if game_state == "MENU":

        draw_menu()

    elif game_state == "PROFILE":

        draw_profile()

    elif game_state == "SETTINGS":

        draw_settings()

    elif game_state == "HISTORY":

        draw_history()

    elif game_state == "GAME":

        draw_game()

    elif game_state == "RESULT":

        draw_result()

    # Частицы поверх интерфейса
    draw_particles()

    # --------------------------------------------------------
    # АДАПТИВНАЯ ОТРИСОВКА
    # --------------------------------------------------------

    sw, sh = screen.get_size()

    screen.fill(
        theme()["bg"]
    )

    if sw > 0 and sh > 0:

        # Интерфейс перестраивается под окно:
        # сохраняем пропорции, но НЕ растягиваем объекты
        scale = min(
            sw / BASE_W,
            sh / BASE_H
        )

        new_w = int(
            BASE_W * scale
        )

        new_h = int(
            BASE_H * scale
        )

        scaled = pygame.transform.smoothscale(
            canvas,
            (
                new_w,
                new_h
            )
        )

        x = (
            sw - new_w
        ) // 2

        y = (
            sh - new_h
        ) // 2

        screen.blit(
            scaled,
            (
                x,
                y
            )
        )

    pygame.display.flip()

    # --------------------------------------------------------
    # EVENTS
    # --------------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            save_settings()
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_F11:

                toggle_fullscreen()

            elif event.key == pygame.K_ESCAPE and IS_ANDROID:
                # Android Back is commonly delivered through Escape.
                if game_state != "MENU":
                    go_menu()
                else:
                    save_settings()
                    running = False

            else:

                handle_key(
                    event
                )

        elif IS_ANDROID and event.type in (
            getattr(pygame, "APP_WILLENTERBACKGROUND", -9999),
            getattr(pygame, "APP_TERMINATING", -9998),
        ):

            save_settings()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button != 1:
                continue

            # MENU
            if game_state == "MENU":

                handle_button_click(
                    menu_buttons
                )

            # PROFILE
            elif game_state == "PROFILE":

                mx, my = mouse_position()

                if profile_click():
                    continue

                if handle_button_click(
                    profile_buttons
                ):
                    continue

                back_rect = pygame.Rect(
                    30,
                    25,
                    100,
                    38
                )

                if back_rect.collidepoint(
                    mx,
                    my
                ):

                    go_menu()

            # SETTINGS
            elif game_state == "SETTINGS":

                mx, my = mouse_position()

                back_rect = pygame.Rect(
                    30,
                    25,
                    100,
                    38
                )

                if back_rect.collidepoint(
                    mx,
                    my
                ):

                    go_menu()

                else:

                    handle_button_click(
                        settings_buttons
                    )

            # HISTORY
            elif game_state == "HISTORY":

                mx, my = mouse_position()

                back_rect = pygame.Rect(
                    30,
                    25,
                    100,
                    38
                )

                if back_rect.collidepoint(
                    mx,
                    my
                ):

                    game_state = "PROFILE"

            # RESULT
            elif game_state == "RESULT":

                handle_button_click(result_buttons)

            # GAME
            elif game_state == "GAME":

                handle_game_click()


pygame.quit()
sys.exit()
