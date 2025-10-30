from __future__ import annotations

import os
import sys
from typing import Iterable, Optional, Sequence, Union

CSI = "\x1b["
RESET = CSI + "0m"

COLORS = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
    "bright_black": 90,
    "bright_red": 91,
    "bright_green": 92,
    "bright_yellow": 93,
    "bright_blue": 94,
    "bright_magenta": 95,
    "bright_cyan": 96,
    "bright_white": 97,
}

STYLES = {
    "bold": 1,
    "dim": 2,
    "italic": 3,
    "underline": 4,
    "blink": 5,
    "reverse": 7,
    "hidden": 8,
}

def _join_codes(codes: Iterable[int]) -> str:
    codes_list = [str(int(c)) for c in codes if c is not None]
    if not codes_list:
        return ""
    return f"{CSI}{';'.join(codes_list)}m"

def _color_code(color: Union[str, int, None]) -> Optional[int]:
    if color is None:
        return None
    if isinstance(color, int):
        return int(color)
    key = str(color).lower()
    return COLORS.get(key)

def supports_color() -> bool:
    force = os.environ.get("FORCE_COLOR", "")
    if force and force.lower() not in ("0", "false", "no", ""):
        return True

    if not hasattr(sys.stdout, "isatty"):
        return False

    if not sys.stdout.isatty():
        return False

    # Windows VT enable best-effort
    if os.name == "nt":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
            mode = ctypes.c_uint()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
                new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
                kernel32.SetConsoleMode(handle, new_mode)
                return True
        except Exception:
            # assume modern Windows supports ANSI
            return True

    return True

def colored(
    text: str,
    color: Union[str, int, None] = None,
    styles: Optional[Sequence[str]] = None,
    emoji: Optional[str] = None,
) -> str:
    
    prefix = f"{emoji} " if emoji else ""
    if not supports_color():
        return f"{prefix}{text}"

    codes: list[int] = []
    ccode = _color_code(color)
    if ccode is not None:
        codes.append(ccode)
    if styles:
        for s in styles:
            code = STYLES.get(s.lower())
            if code is not None:
                codes.append(code)
    seq = _join_codes(codes)
    return f"{seq}{prefix}{text}{RESET}"

style_text = colored  # alias

def _print(text: str, end: str = "\n", file=None):
    if file is None:
        file = sys.stdout
    print(text, end=end, file=file)

# ASCII helpers (very small, dependency-free)
def _ascii_box(text: str) -> str:
    lines = text.splitlines() or [text]
    width = max(len(line) for line in lines)
    top = "+" + "-" * (width + 2) + "+"
    middle = "\n".join(f"| {line.ljust(width)} |" for line in lines)
    return f"{top}\n{middle}\n{top}"

def _ascii_banner(text: str) -> str:
    t = text.upper()
    underline = "=" * len(t)
    return f"{t}\n{underline}"

def asciiize(text: str, style: Optional[str] = "box") -> str:
    if not style:
        return text
    style = str(style).lower()
    if style == "banner":
        return _ascii_banner(text)
    # default
    return _ascii_box(text)

# Input helpers
def input_colored(
    prompt: str,
    color: Union[str, int, None] = None,
    styles: Optional[Sequence[str]] = None,
    emoji: Optional[str] = None,
) -> str:
    # colored() already appends RESET; that's safe to pass to input()
    prompt_str = colored(prompt, color=color, styles=styles, emoji=emoji)
    return input(prompt_str)

def confirm(
    prompt: str,
    default: bool = False,
    color: Union[str, int, None] = "yellow",
    styles: Optional[Sequence[str]] = ("bold",),
    emoji: Optional[str] = "❓",
) -> bool:
    hint = "[Y/n]" if default else "[y/N]"
    full_prompt = f"{prompt} {hint} "
    resp = input_colored(full_prompt, color=color, styles=styles, emoji=emoji).strip().lower()
    if not resp:
        return default
    return resp in ("y", "yes", "1", "true", "t")

# Semantic printing (extended)
def _render_message(
    msg: str,
    *,
    color: Union[str, int, None] = None,
    styles: Optional[Sequence[str]] = None,
    emoji: Optional[str] = None,
    ascii: Union[bool, str, None] = None,
    font: Optional[str] = None,
) -> str:
    
    # Interpret font hints
    ascii_style = None
    if ascii:
        # if ascii is True -> default box; if ascii is string -> use as style name
        ascii_style = "box" if ascii is True else str(ascii)
    elif font:
        f = str(font).lower()
        if "banner" in f:
            ascii_style = "banner"
        elif "big" in f or "px" in f or any(d in f for d in ("20", "30", "40")):
            ascii_style = "box"

    if ascii_style:
        block = asciiize(msg, style=ascii_style)
        # color the whole block
        return colored(block, color=color, styles=styles, emoji=emoji)

    return colored(msg, color=color, styles=styles, emoji=emoji)

def success(
    msg: str,
    *,
    end: str = "\n",
    styles: Optional[Sequence[str]] = ("bold",),
    emoji: Optional[str] = "✅",
    ascii: Union[bool, str, None] = None,
    font: Optional[str] = None,
):
    out = _render_message(msg, color="green", styles=styles, emoji=emoji, ascii=ascii, font=font)
    _print(out, end=end)

def warning(
    msg: str,
    *,
    end: str = "\n",
    styles: Optional[Sequence[str]] = ("bold",),
    emoji: Optional[str] = "⚠️",
    ascii: Union[bool, str, None] = None,
    font: Optional[str] = None,
):
    out = _render_message(msg, color="yellow", styles=styles, emoji=emoji, ascii=ascii, font=font)
    _print(out, end=end)

def error(
    msg: str,
    *,
    end: str = "\n",
    styles: Optional[Sequence[str]] = ("bold",),
    emoji: Optional[str] = "❌",
    ascii: Union[bool, str, None] = None,
    font: Optional[str] = None,
):
    out = _render_message(msg, color="red", styles=styles, emoji=emoji, ascii=ascii, font=font)
    _print(out, end=end)

def info(
    msg: str,
    *,
    end: str = "\n",
    styles: Optional[Sequence[str]] = None,
    emoji: Optional[str] = "ℹ️",
    ascii: Union[bool, str, None] = None,
    font: Optional[str] = None,
):
    out = _render_message(msg, color="blue", styles=styles, emoji=emoji, ascii=ascii, font=font)
    _print(out, end=end)

def custom(
    msg: str,
    color: Union[str, int, None] = None,
    styles: Optional[Sequence[str]] = None,
    emoji: Optional[str] = None,
    *,
    ascii: Union[bool, str, None] = None,
    font: Optional[str] = None,
    end: str = "\n",
):
    out = _render_message(msg, color=color, styles=styles, emoji=emoji, ascii=ascii, font=font)
    _print(out, end=end)

# Utility & palette demo
def example_palette():
    parts = []
    for name in [
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
        "bright_red",
        "bright_green",
        "bright_yellow",
        "bright_blue",
        "bright_magenta",
        "bright_cyan",
        "bright_white",
    ]:
        parts.append(colored(name, color=name))
    return "  ".join(parts)

__all__ = [
    "colored",
    "style_text",
    "success",
    "warning",
    "error",
    "info",
    "custom",
    "supports_color",
    "example_palette",
    "input_colored",
    "confirm",
    "asciiize",
]