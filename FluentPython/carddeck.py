import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# Now work with it some
deck = FrenchDeck()
len(deck)
deck[0]
deck[51]

choice(deck)

# Because we implement we can slice like a list and iterate
deck[:3]

for card in deck:
    print(card)
for card in reversed(deck):
    print(card)

# Iteration is often implicit collection with no __contains__ does
# sequential for in
Card('Q', 'hearts') in deck

# Sorting
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
