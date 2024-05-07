"""
utils module
"""

import os


def clear_console() -> None:
    if os.name == "posix":  # Linux/Macos
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")
