import tkinter as tk

from .hearts_shared import FallingHeart
from .platform_utils import configure_overlay_window, set_process_dpi_awareness


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
