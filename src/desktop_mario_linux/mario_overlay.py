import tkinter as tk

from .platform_utils import configure_overlay_window, set_process_dpi_awareness

MARIO_COLORS = {
    "_": "",
    "R": "#ff0000",
    "B": "#663300",
    "S": "#ffcc99",
    "O": "#0000ff",
    "Y": "#ffff00",
}

FRAME_1 = [
    "____RRRRR___",
    "___RRRRRRRRR",
    "___BBBSSBSS_",
    "__BBBSBSSSSS",
    "__BBBSBSSBSS",
    "__BBBBSSSS__",
    "____RRRRRRR_",
    "___RRROORRR_",
    "__RRROOORRRR",
    "__RROOYOORRR",
    "____OOOOOO__",
    "___OO_OO_OO_",
    "__OO__OO__OO",
    "______RR____",
    "_____BBBB___",
]

FRAME_2 = [
    "____RRRRR___",
    "___RRRRRRRRR",
    "___BBBSSBSS_",
    "__BBBSBSSSSS",
    "__BBBSBSSBSS",
    "__BBBBSSSS__",
    "____RRRRRRR_",
    "___RRROORRR_",
    "__RRRRROORRR",
    "__RRROOYOORR",
    "__R_OOOOOO__",
    "__RROO_OO___",
    "__ROO__OO___",
    "___OO_RR____",
    "___BBBBBB___",
]


class Mario:
    def __init__(self, canvas: tk.Canvas, screen_width: int, screen_height: int):
        self.canvas = canvas
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pixel_size = 4
        self.width = len(FRAME_1[0]) * self.pixel_size
        self.height = len(FRAME_1) * self.pixel_size
        self.x = -self.width
        self.y = screen_height - 48 - self.height
        self.speed = 3
        self.frame_index = 0
        self.frames = [FRAME_1, FRAME_2]
        self.pixels: list[int] = []

    def draw_frame(self, frame_data: list[str]) -> None:
        for pixel in self.pixels:
            self.canvas.delete(pixel)
        self.pixels.clear()

        for row_idx, row in enumerate(frame_data):
            for col_idx, color_code in enumerate(row):
                if color_code == "_":
                    continue
                px_x = self.x + (col_idx * self.pixel_size)
                px_y = self.y + (row_idx * self.pixel_size)
                rect_id = self.canvas.create_rectangle(
                    px_x,
                    px_y,
                    px_x + self.pixel_size,
                    px_y + self.pixel_size,
                    fill=MARIO_COLORS[color_code],
                    outline=MARIO_COLORS[color_code],
                )
                self.pixels.append(rect_id)

    def update(self) -> None:
        self.x += self.speed
        if self.x > self.screen_width:
            self.x = -self.width

        self.frame_index += 1
        current_frame = self.frames[(self.frame_index // 5) % len(self.frames)]
        self.draw_frame(current_frame)


def main() -> None:
    set_process_dpi_awareness()

    root = tk.Tk()
    configure_overlay_window(root)

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
    canvas.pack()

    mario = Mario(canvas, screen_width, screen_height)

    def animate() -> None:
        mario.update()
        root.after(30, animate)

    root.bind("<Escape>", lambda _e: root.destroy())

    animate()
    root.mainloop()
