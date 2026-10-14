import pygame
import pygetwindow as gw
from pathlib import Path
import random
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

pygame.init()
screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption("RANSOM")
window = gw.getWindowsWithTitle("RANSOM")[0]
pygame.display.set_icon(
    pygame.image.load(resource_path("icon.webp"))
)

# Ransom theme
pygame.mixer.init()

pygame.mixer.music.load(resource_path("Ransom theme.wav"))
pygame.mixer.music.play(loops=-1)

clock = pygame.time.Clock()

# PyGame font
font = pygame.font.Font(None, 72)
font.set_bold(True)

# Ransom-image
ransom_image = pygame.image.load(resource_path("Ransom.png")).convert()
size_x, size_y = ransom_image.get_size()
screen = pygame.display.set_mode((size_x / 6, size_y / 6))
sw, sh = pygame.display.get_desktop_sizes()[0]

# 90 second timer
time_left = 90
start_ticks = pygame.time.get_ticks()

# Moves the window to a random spot on the screen
def move_window(_window):
    x = random.randint(0, sw - window_width)
    y = random.randint(0, sh - window_height)
    _window.moveTo(x, y)

# Gets all files within the current folder and "encrypts" them (file extension change)
script_files = ["ransom.py", "Ransom.png", "Ransom theme.wav", "main.spec", "icon.webp", "main.RANSOM.exe"]
original_names = {}

if getattr(sys, "frozen", False):
    file_path = Path(sys.executable).parent
else:
    file_path = Path(__file__).parent

for file in file_path.iterdir():
    if file.is_file() and file.name not in script_files:
        new = file.with_name(
            file.stem + file.suffix + ".RANSOM"
        )
        original_names[new] = file
        file.rename(new)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            move_window(window)
            if random.randint(0, 9) == 0:
                running = False

    window_width, window_height = screen.get_size()
    screen.fill((0, 0, 0))

    # Fit image accordingly
    image_width, image_height = ransom_image.get_size()

    scale = min(
        window_width / image_width,
        window_height / image_height
    )

    new_width = int(image_width * scale)
    new_height = int(image_height * scale)

    scaled_image = pygame.transform.smoothscale(
        ransom_image,
        (new_width, new_height)
    )

    # Center image
    image_x = (window_width - new_width) // 2
    image_y = (window_height - new_height) // 2

    screen.blit(scaled_image, (image_x, image_y))

    # Timer stuff
    elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining = max(0, time_left - elapsed_seconds)

    minutes = remaining // 60
    seconds = remaining % 60

    # Stuff when timer runs out
    if remaining <= 0:
        running = False

    timer_text = font.render(
        f"{minutes:02d}:{seconds:02d}",
        True,
        (0, 0, 0)
    )

    # Timer display
    timer_rect = timer_text.get_rect(
        bottomright=(window_width - 100, window_height - 25)
    )

    screen.blit(timer_text, timer_rect)

    # Move the window
    if random.randint(0, 300) == 0:
        move_window(window)

    pygame.display.flip()
    clock.tick(60)

for new, original in original_names.items():
    if new.exists():
        new.rename(original)
pygame.quit()
