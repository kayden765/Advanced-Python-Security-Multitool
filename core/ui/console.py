from .themes import MAINFRAME_THEME

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.box import ROUNDED, DOUBLE
    from rich.rule import Rule
    from rich.text import Text
    from rich.markup import escape
    _HAS_RICH = True
except Exception:  
    _HAS_RICH = False


class Colors:
    RED = '\033[91m'
    AMBER = '\033[93m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BLUE = '\033[94m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_MAGENTA = '\033[95m'
    CLEAR_SCREEN = '\033[2J\033[3J\033[H'


_BANNER_ART = r"""
      ______
     .-"      "-.
    /            \
   |              |
   |,.  .-.  .-.  ,|
   | )(__/  \__)( |
   |/     /\     \|
   (_     ^^     _)
    \__|IIIIII|__/
     | \IIIIII/ |
     \          /
     `--------`
"""


class ConsoleUI:

    def __init__(self, console=None):
        self.console = console or Console(
            theme=MAINFRAME_THEME,
            highlight=False,
            soft_wrap=True,
        )

    def clear(self):
        self.console.clear()

    @staticmethod
    def _cell(value):
        if isinstance(value, str):
            try:
                return Text.from_markup(value)
            except Exception:
                return Text(value)
        if isinstance(value, Text):
            return value
        return Text(str(value))

    def rule_header(self, title, color="cyan"):
        self.console.print(
            Rule(title=Text(title, style=f"bold {color}"), style=color, characters="═")
        )

    def info(self, msg):
        self.console.print(f"[info]ℹ[/info] {msg}")

    def success(self, msg):
        self.console.print(f"[success]✓[/success] {msg}")

    def warning(self, msg):
        self.console.print(f"[warning]![/warning] {msg}")

    def error(self, msg):
        self.console.print(f"[error][×][/error] {msg}")

    def pause(self, msg="Press Enter to continue..."):
        self.console.print(f"[dim]{msg}[/dim]")
        try:
            self.console.input()
        except (KeyboardInterrupt, EOFError):
            pass

    def panel(self, content, title="", border_style="cyan",
              box_style=None, padding=None, subtitle=None):
        box = box_style if box_style is not None else ROUNDED
        kwargs = {"title": title, "border_style": border_style, "box": box}
        if padding is not None:
            kwargs["padding"] = padding
        if subtitle is not None:
            kwargs["subtitle"] = subtitle
        self.console.print(Panel(content, **kwargs))

    def section(self, title, color="cyan", subtitle=None):
        self.console.print()
        self.console.print(
            Rule(title=Text(title, style=f"bold {color}"),
                 style=color, characters="─")
        )
        if subtitle:
            self.console.print(f"[dim]{subtitle}[/dim]")
        self.console.print(Rule(style=color, characters="─"))

    def keyval_table(self, title, rows, border_style="cyan"):
        table = Table(title=title, box=ROUNDED, border_style=border_style,
                      header_style=f"bold {border_style}")
        table.add_column("FIELD", style="bold")
        table.add_column("VALUE", ratio=1)
        for label, value in rows:
            table.add_row(self._cell(label), self._cell(value))
        self.console.print(table)

    def result_table(self, title, headers, rows, border_style="cyan"):
        table = Table(title=title, box=ROUNDED, border_style=border_style,
                      header_style=f"bold {border_style}",
                      pad_edge=True, show_lines=False)
        for h in headers:
            table.add_column(h, overflow="fold")
        ncols = len(table.columns)
        for row in rows:
            cells = list(row) if isinstance(row, (list, tuple)) else [row]
            cells = cells[:ncols] + [""] * max(0, ncols - len(cells))
            table.add_row(*[self._cell(c) for c in cells])
        self.console.print(table)

    def prompt_input(self, prompt, default=None):
        if default is not None:
            line = (
                f"[bold yellow]{escape(str(prompt))} "
                f"[dim](default: {escape(str(default))})[/dim] \u2192 [/bold yellow]"
            )
        else:
            line = f"[bold yellow]{escape(str(prompt))} \u2192 [/bold yellow]"
        try:
            value = self.console.input(line).strip()
        except (KeyboardInterrupt, EOFError):
            value = ""
        if value == "" and default is not None:
            return default
        return value

    def banner(self):
        body = Text(justify="center")
        body.append(Text(_BANNER_ART, style="cyan"))
        body.append("\n")
        body.append(Text("MAINFRAME // SEC-OPS TERMINAL MULTITOOL", style="bold green"))
        body.append("\n")
        body.append(Text("DEPLOYMENT SPECIFICATION RELEASE v5.90 // 40-IN-1 TOOL PLATFORM",
                         style="cyan"))
        self.console.print(
            Panel(body,
                  title=Text("MAINFRAME v5.90", style="bold cyan"),
                  border_style="cyan", box=DOUBLE, padding=(1, 4))
        )

    def main_menu(self):
        table = Table(title="MAIN SYSTEM DIRECTORY CORE", box=ROUNDED,
                      border_style="cyan", header_style="bold cyan",
                      pad_edge=True, show_header=False)
        table.add_column("ID", style="bold", width=6)
        table.add_column("SUB-DIRECTORY", overflow="fold", ratio=1)
        table.add_row("1", "[cyan]Sub-Directory 01 // Network Infrastructure & Endpoint Recon Cores[/cyan]")
        table.add_row("2", "[cyan]Sub-Directory 02 // External OSINT & Target Record Profilers[/cyan]")
        table.add_row("3", "[green]Sub-Directory 03 // Local Data Traffic Monitors, Audits & Utilities[/green]")
        table.add_row("4", "[cyan]Sub-Directory 04 // Advanced Infrastructure Audits & Integrity Cores[/cyan]")
        table.add_row("5", "[red]Sub-Directory 05 // Attack Vectors & Exploit Frameworks [SHELL BASELINE][/red]")
        table.add_row("6", "[red]Terminate Active Mainframe Operator Control Session[/red]")
        self.console.print(table)

    def submenu(self, title, items, back_text=None):
        table = Table(title=title, box=ROUNDED, border_style="cyan",
                      header_style="bold cyan", pad_edge=True, show_header=False)
        table.add_column("ID", style="bold", width=6)
        table.add_column("MODULE", overflow="fold", ratio=1)
        for item in items:
            if isinstance(item, (list, tuple)) and len(item) >= 3:
                key, label, color = item[0], item[1], item[2]
                table.add_row(str(key), f"[{color}]{label}[/{color}]")
            elif isinstance(item, (list, tuple)) and len(item) == 2:
                key, label = item[0], item[1]
                table.add_row(str(key), label)
            else:
                table.add_row(str(item), "")
        self.console.print(table)
        if back_text:
            self.console.print(f"[yellow]↩  {escape(str(back_text))}[/yellow]")

    def directory_menu(self, title, items, header_color="cyan"):
        self.console.print(Text(f"[{title}]", style=f"bold {header_color}"))
        self.console.print()
        if not items:
            return
        maxw = max(len(item[1]) for item in items)
        for item in items:
            raw_key = item[0]
            key = f"{int(raw_key):02d}" if str(raw_key).isdigit() else str(raw_key)
            name = item[1]
            desc = item[2] if len(item) > 2 else ""
            color = item[3] if len(item) > 3 else header_color
            row = Text("  [", style=f"bold {color}")
            row.append(f"{key}] ", style=color)
            row.append(f"{name.ljust(maxw)} - {desc}", style=color)
            self.console.print(row)


_ui_singleton = None


def get_ui():
    global _ui_singleton
    if _HAS_RICH and _ui_singleton is None:
        try:
            _ui_singleton = ConsoleUI()
        except Exception:
            _ui_singleton = None
    return _ui_singleton


ui = ConsoleUI() if _HAS_RICH else None

