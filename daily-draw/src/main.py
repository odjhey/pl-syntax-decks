from .decks import load
import numpy as np


def main():
    cards = load.get_cards()
    # draw
    some_seq = np.random.randn(len(cards))
    some_seq = np.exp(some_seq) / np.sum(np.exp(some_seq))
    oh = np.random.default_rng().multinomial(1, some_seq, size=None)
    print(cards[np.argmax(oh)])


if __name__ == "__main__":
    main()
