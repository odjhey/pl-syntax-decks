import yaml
from pydantic import BaseModel, field_validator


class Card(BaseModel):
    id: str
    title: str
    tags: list[str]
    prompt: str
    hints: str
    constraints: list[str]
    done_when: list[str]
    stretch_goals: list[str]

    @field_validator("title", "prompt", "hints", mode="before")
    def strip_whitespace(cls, v):
        return v.strip()

    # pretty print
    def __str__(self) -> str:
        return f"({self.id}) {self.title} ({', '.join(self.tags)})\n---\n{self.prompt}\nHints: {self.hints}\nConstraints:\n{'\n'.join(self.constraints)}\n---\nDone when:\n{'\n'.join(self.done_when)}\nStretch goals: {', '.join(self.stretch_goals)}"


class Decks(BaseModel):
    cards: list[Card]


with open("./decks.yaml", "r") as f:
    raw_decks = yaml.safe_load(f)


def get_cards() -> list[Card]:
    """Load the cards from the YAML file and return them as a list of Card objects."""
    decks = Decks.model_validate(raw_decks)
    return decks.cards
