"""Rich theming palette for the MAINFRAME terminal multitool.

Centralizes the color / style mapping so rendering stays visually consistent
across banners, menus, tables, panels, and status messages.
"""
from rich.theme import Theme

# Logical -> rich style mappings used by the ConsoleUI helpers.
COLOR_MAP = {
    "cyan": "cyan",
    "amber": "yellow",
    "yellow": "yellow",
    "green": "green",
    "red": "red",
    "blue": "blue",
    "magenta": "magenta",
    "grey": "dim",
}

MAINFRAME_THEME = Theme({
    "info": "cyan",
    "success": "green",
    "warning": "yellow",
    "error": "red",
    "header": "bold cyan",
    "banner": "cyan",
    "menu.title": "bold magenta",
    "menu.item": "cyan",
    "menu.back": "yellow",
    "border": "cyan",
    "dim": "dim",
}, inherit=False)
