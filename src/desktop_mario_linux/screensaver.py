import random
import time
import tkinter as tk

from .hearts_shared import FallingHeart
from .platform_utils import configure_overlay_window, get_idle_time_seconds, set_process_dpi_awareness


class MystifyLines:
    def __init__(self, canvas: tk.Canvas, width: int, height: int):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.points: list[list[int]] = []
        self.velocities: list[list[int]] = []
        self.color = "#%02x%02x%02x" % (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )

        for _ in range(4):
            self.points.append([random.randint(0, width), random.randint(0, height)])
            self.velocities.append([random.choice([-4, -3, 3, 4]), random.choice([-4, -3, 3, 4])])

        self.line_id = canvas.create_polygon(
            self.points[0][0],
            self.points[0][1],
            self.points[1][0],
            self.points[1][1],
            self.points[2][0],
            self.points[2][1],
            self.points[3][0],
            self.points[3][1],
            outline=self.color,
            fill="",
            width=2,
        )

    def move(self) -> None:
        for i in range(4):
            self.points[i][0] += self.velocities[i][0]
            self.points[i][1] += self.velocities[i][1]

            if self.points[i][0] <= 0 or self.points[i][0] >= self.width:
                self.velocities[i][0] *= -1
            if self.points[i][1] <= 0 or self.points[i][1] >= self.height:
                self.velocities[i][1] *= -1

        coords: list[int] = []
        for point in self.points:
            coords.extend(point)
        self.canvas.coords(self.line_id, *coords)

        if random.random() < 0.05:
            self.color = "#%02x%02x%02x" % (
                random.randint(50, 255),
                random.randint(50, 255),
                random.randint(50, 255),
            )
            self.canvas.itemconfig(self.line_id, outline=self.color)


class ScreensaverApp:
    def __init__(self, idle_timeout: int = 60):
        self.root: tk.Tk | None = None
        self.idle_timeout = idle_timeout
        self.running_screensaver = False
        self.idle_supported = get_idle_time_seconds() is not None
        set_process_dpi_awareness()

    def start_screensaver(self) -> None:
        if self.running_screensaver:
            return

        idle_time = get_idle_time_seconds()
        if self.idle_supported and idle_time is not None and idle_time < 0.5:
            return

        self.running_screensaver = True
        self.root = tk.Tk()
        configure_overlay_window(self.root)

        self.root.bind("<Key>", self.stop_screensaver)
        self.root.bind("<Motion>", self.stop_screensaver)
        self.root.bind("<Button>", self.stop_screensaver)

        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.canvas = tk.Canvas(self.root, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.mystify_shapes = [MystifyLines(self.canvas, screen_width, screen_height) for _ in range(5)]
        self.hearts = [FallingHeart(self.canvas, screen_width, screen_height) for _ in range(50)]

        self.animate()

    def stop_screensaver(self, _event=None) -> None:
        if self.running_screensaver and self.root:
            self.running_screensaver = False
            self.root.destroy()
            self.root = None

    def animate(self) -> None:
        if not self.running_screensaver or not self.root:
            return

        idle_time = get_idle_time_seconds()
        if self.idle_supported and idle_time is not None and idle_time < 1:
            self.stop_screensaver()
            return

        for shape in self.mystify_shapes:
            shape.move()

        for heart in self.hearts:
            heart.fall()

        self.root.after(20, self.animate)

    def monitor_idle(self) -> None:
        idle = get_idle_time_seconds()

        if idle is None:
            if not self.running_screensaver:
                self.start_screensaver()
            return

        if idle >= self.idle_timeout and not self.running_screensaver:
            self.start_screensaver()

        if not self.root or not self.running_screensaver:
            time.sleep(1)


def main() -> None:
    app = ScreensaverApp()

    if not app.idle_supported:
        print("Idle-time detection is unavailable on this platform. Starting screensaver immediately.")
        app.start_screensaver()
        if app.root:
            app.root.mainloop()
        return

    print("Screensaver monitor running. Waiting for 1 minute of idle time...")
    while True:
        try:
            app.monitor_idle()
            if app.root and app.running_screensaver:
                app.root.mainloop()
        except KeyboardInterrupt:
            break
