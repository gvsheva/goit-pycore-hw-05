import re
from decimal import Decimal
from typing import Callable, Iterable

PATTERNS = {
    "SPACE_DOT_REAL": r"\d{1,3}(?: \d{3})*(?:\.\d+)",
    "COMMA_DOT_REAL": r"\d{1,3}(?:,\d{3})*(?:\.\d+)",
    "_COMMA_REAL": r"\d+,\d+",
    "_DOT_REAL": r"\d+\.\d+",
    "SPACE_INT": r"\d{1,3}(?: \d{3})*",
    "COMMA_INT": r"\d{1,3}(?:,\d{3})*",
    "INT": r"\d+",
}

PATTERN = re.compile(
    r"|".join(f"(?P<{name}>{pattern})" for name, pattern in PATTERNS.items()))


def find_numbers(text: str):
    for m in PATTERN.finditer(text):
        match m.groupdict():
            case {"SPACE_DOT_REAL": value} if value is not None:
                yield Decimal(value.replace(" ", ""))
            case {"COMMA_DOT_REAL": value} if value is not None:
                yield Decimal(value.replace(",", ""))
            case {"_COMMA_REAL": value} if value is not None:
                yield Decimal(value.replace(",", "."))
            case {"_DOT_REAL": value} if value is not None:
                yield Decimal(value)
            case {"SPACE_INT": value} if value is not None:
                yield Decimal(value.replace(" ", ""))
            case {"COMMA_INT": value} if value is not None:
                yield Decimal(value.replace(",", ""))
            case {"INT": value} if value is not None:
                yield Decimal(value)
            case _:
                raise RuntimeError("Unknown pattern")


def sum_numbers(text: str, gen: Callable[[str], Iterable[Decimal]]):
    return sum(gen(text))
