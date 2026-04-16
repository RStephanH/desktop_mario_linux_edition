import random
import tkinter as tk

EMOJI_FONT_FAMILY = ("Segoe UI Emoji", "Noto Color Emoji", "Apple Color Emoji", "Arial Unicode MS")


class FallingHeart:
    def __init__(self, canvas: tk.Canvas, width: int, height: int):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.x = random.randint(0, width)
        self.y = random.randint(-1000, -50)
        self.speed_y = random.uniform(2, 6)
        self.speed_x = random.uniform(-0.5, 0.5)
        self.size = random.randint(20, 80)

        colors = ["#ff3366", "#ff6699", "#cc0033", "#ff99aa"]
        chars = ["❤", "💖", "💗", "💕", "💘"]

        self.id = canvas.create_text(
            self.x,
            self.y,
            text=random.choice(chars),
            fill=random.choice(colors),
            font=(EMOJI_FONT_FAMILY, self.size),
        )

    def fall(self) -> None:
        self.canvas.move(self.id, self.speed_x, self.speed_y)
        pos = self.canvas.coords(self.id)
        if len(pos) >= 2 and pos[1] > self.height + 100:
            self.canvas.coords(self.id, random.randint(0, self.width), random.randint(-200, -50))
