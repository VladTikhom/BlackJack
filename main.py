from typing import Tuple, List
import random
from enum import Enum


class Suit(Enum):
    Club = '♣'
    Diamond = '♢'
    Heart = '♡'
    Space = '♠'


class Card:
    def __init__(self, rank: str, suit: Suit, hard: int, soft: int) -> None:
        self.suit = suit
        self.rank = rank
        self.hard = hard
        self.soft = soft

    def __str__(self):
        return f'{self.suit.value}, {self.rank}'


class NumberCard(Card):
    def __init__(self, rank: int, suit: Suit) -> None:
        super().__init__(str(rank), suit, rank, rank)


class AceCard(Card):
    def __init__(self, rank: int, suit: Suit) -> None:
        super().__init__('A', suit, 1, 11)


def card(rank: int, suit: Suit):
    if rank == 1:
        return AceCard(rank, suit)
    elif 2 <= rank < 11:
        return NumberCard(rank, suit)
    elif 11 <= rank < 14:
        return FaceCard(rank, suit)
    else:
        raise Exception('Rank out of range')


class FaceCard(Card):
    def __init__(self, rank: int, suit: Suit) -> None:
        rank_str = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        super().__init__(rank_str, suit, 10, 10)


class Deck:
    def __init__(self) -> None:
        self._cards = [card(r + 1, s) for r in range(13) for s in iter(Suit)]
        random.shuffle(self._cards)

    def pop(self) -> Card:
        return self._cards.pop()


class Hand:
    def __init__(self, dealer_card: Card, *cards: Card):
        self.dealer_card : Card = dealer_card
        self.cards: List[Card] = list(cards)

    def add_card(self, card: Card):
        self.cards.append(card)

    def hard_total(self) -> int:
        return sum(c.hard for c in self.cards)

    def soft_total(self) -> int:
        return sum(c.soft for c in self.cards)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} {self.dealer_card} {self.cards}"


if __name__ == '__main__':
    deck = Deck()
    hand = Hand(deck.pop())
    hand.add_card(deck.pop())
    hand.add_card(deck.pop())
    for card in hand.cards:
        print(card)
    print(hand.hard_total())
    print(hand.soft_total())
