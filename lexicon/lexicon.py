from dataclasses import dataclass


class InitMessage():
    def __init__(self, attempts: int):
        self.text = f"""Я загадал число от 1 до 100.

        У тебя {attempts} попыток."""


@dataclass
class WarningMessage:
    header = "Так нельзя"
    body = "Необходимо ввести целое число!"


class LowerNumber():
    def __init__(self, attempts: int):
        self.text = f"""Загаданное число меньше!

    Осталось {attempts} попыток."""


class HigherNumber():
    def __init__(self, attempts: int):
        self.text = f"""Загаданное число больше!

    Осталось {attempts} попыток."""


class WinMessage():
    def __init__(self, number: int):
        self.header = "Победа"
        self.body = f"""Вы угадали!

        Было загадано число {number}

        Хотите сыграть ещё?"""


class LoseMessage():
    def __init__(self, number: int):
        self.header = "Поражение"
        self.body = f"""Жаль, но Вы не угадали!

        Было загадано число {number}

        Хотите сыграть ещё?"""
