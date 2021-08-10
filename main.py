from suit import Suit
from card import Card
from deck import Deck
from player import Player
from war_card_game import WarCardGame

player = Player("Nora", Deck(is_empty=True))
computer = Player("computer", Deck(is_empty=True), is_computer=True)
deck = Deck()

game = WarCardGame(player, computer, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("\nAre you ready for the next round? \nPress Enter to continue. Press x to exit. ")

    if answer.lower() == "x":
        break