import random
import tkinter as tk

from .platform_utils import configure_overlay_window, set_process_dpi_awareness

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


def main() -> None:
    set_process_dpi_awareness()

    root = tk.Tk()
    configure_overlay_window(root)

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
    canvas.pack()

    hearts = [FallingHeart(canvas, screen_width, screen_height) for _ in range(60)]

    def animate() -> None:
        for heart in hearts:
            heart.fall()
        root.after(20, animate)

    root.bind("<Escape>", lambda _e: root.destroy())
    canvas.create_text(
        screen_width // 2,
        50,
        text="Press ESC to close the hearts overlay",
        fill="white",
        font=("Arial", 12, "bold"),
    )

    animate()
    root.mainloop()
