import csv
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

import numpy as np


class Grade(Enum):
    EASY = 1
    AGAIN = 2
    SKIP = 3


@dataclass
class SrsEntry:
    id: str
    card_id: str
    grade: Grade
    created_at: datetime = field(default_factory=datetime.now)


class Srs:
    def __init__(self, history=None):
        self.history = []
        if history is not None:
            self.history = history


def generate_id():
    # @todo implement a proper ID generator
    return str(int(datetime.now().timestamp() * 1000))


def append_to_history(entry: SrsEntry):
    # @todo check for dupes via `id`
    history_file = "history.csv"
    with open(history_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [entry.id, entry.card_id, entry.grade.value, entry.created_at.isoformat()]
        )
    print(f"Appended entry to history: {entry}")


def load_history(srs: Optional[Srs] = None):
    history_file = "history.csv"
    with open(history_file, mode="r") as file:
        reader = csv.DictReader(file)
        history = []
        for row in reader:
            entry = SrsEntry(
                id=row["id"],
                card_id=row["card_id"],
                grade=Grade(int(row["grade"])),
                created_at=datetime.fromisoformat(row["created_at"]),
            )
            history.append(entry)
    print(f"Loaded {len(history)} entries from history.")
    print("Data loaded successfully.")
    print(history)
    if srs is not None:
        srs.history = history
        return srs
    srs = Srs(history=history)
    return srs


def draw(srs: Srs):
    # remove dupes, only keep latest
    # derive due_date field, by simple increment due by create_date + grade
    pass


def draw_rand(srs: Srs):
    """get one"""
    probs = np.random.rand(len(srs.history))
    probs = np.exp(probs) / np.sum(np.exp(probs))
    hit = np.random.default_rng().multinomial(5, probs, size=None)
    hit = np.argmax(hit)
    print(probs)
    print(f"Drawn entry: {srs.history[hit]}")

    return srs.history[hit]
