import re
from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Iterable, TextIO


class Level(StrEnum):
    DEBUG = "DEBUG"
    TRACE = "TRACE"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


@dataclass
class Record:
    datetime: datetime
    level: Level
    message: str


PATTERN = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (DEBUG|TRACE|INFO|WARNING|ERROR) (.+)$")


def parse_log(log: TextIO):
    for line in log:
        if match := PATTERN.match(line):
            yield Record(
                datetime=datetime.strptime(
                    match.group(1), "%Y-%m-%d %H:%M:%S"),
                level=Level(match.group(2)),
                message=match.group(3),
            )


def filter_records(level: Level, records: Iterable[Record]):
    for record in records:
        if record.level == level:
            yield record


def stat_records(records: Iterable[Record]):
    stats = defaultdict(int)
    for record in records:
        stats[record.level] += 1
    return stats


def tail(n, records: Iterable[Record]):
    return iter(deque(records, maxlen=n))
