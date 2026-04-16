from __future__ import annotations

import ctypes
import platform
import tkinter as tk

IS_WINDOWS = platform.system() == "Windows"


if IS_WINDOWS:
    from ctypes import wintypes

    class LASTINPUTINFO(ctypes.Structure):
        _fields_ = [("cbSize", wintypes.UINT), ("dwTime", wintypes.DWORD)]


def set_process_dpi_awareness() -> None:
    if not IS_WINDOWS:
        return
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        pass


def configure_overlay_window(root: tk.Tk) -> None:
    root.attributes("-fullscreen", True)
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    try:
        root.wm_attributes("-transparentcolor", "black")
    except tk.TclError:
        pass


def get_idle_time_seconds() -> float | None:
    if not IS_WINDOWS:
        return None
    info = LASTINPUTINFO()
    info.cbSize = ctypes.sizeof(info)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(info))
    millis = ctypes.windll.kernel32.GetTickCount() - info.dwTime
    return millis / 1000.0
