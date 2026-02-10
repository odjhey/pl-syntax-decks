import numpy as np

from .decks import load
from .mini_srs import draw_rand, load_history


def main():
    cards = load.get_cards()
    # draw
    some_seq = np.random.randn(len(cards))
    some_seq = np.exp(some_seq) / np.sum(np.exp(some_seq))
    oh = np.random.default_rng().multinomial(1, some_seq, size=None)
    print(cards[np.argmax(oh)])


def exec_load_history():
    print("Loading history...")
    srs = load_history()
    draw_rand(srs)


if __name__ == "__main__":
    # main()
    exec_load_history()
