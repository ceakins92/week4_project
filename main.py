# ----------- IMPORTS
import itertools
import random

# ----------- CLASS Blackjack


class Blackjack():

    victor = False
    cash = 50
    current_bet = 0
    player_name = ''
    player_total = 0
    player_cards = []
    dealer_total = 0
    dealer_cards = []
    deck = []

    # -------SHUFFLE METHOD
    def shuffle_deck(self):

        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # -- SHUFFLE PROCESS
        self.deck = list(itertools.product(range(1, 14), ['♦', '♠', '♣', '♥']))
        random.shuffle(self.deck)
        # -- PLAYER INVOLVEMENT
        print('\nThe dealer shuffles the deck....')
        # -- CLEAR PLAYER/DEALER PREVIOUS HANDS
        self.player_cards.clear()
        self.dealer_cards.clear()
        # -- PLAYER INTERACTION / MENU
        set_to_go = False
        while not set_to_go:
            ready = input('The dealer is ready.  Are you? (Yes/No)\n').lower()
            # -- READY, CALL DEAL
            if ready == 'yes':
                set_to_go = True
                self.deal()
            # -- NOT READY, PROMPT, SELF
            if ready == 'no':
                print('The dealer is waiting...')
            # -- INVALID RESPONSE
            else:
                print('Please enter "Yes" or "No"')
        pass

    # -------DEAL CARDS METHOD
    def deal(self):

        # -- CLEAR ANY PREVIOUS CARDS
        if self.player_cards:
            self.player_cards.clear()
        if self.dealer_cards:
            self.dealer_cards.clear()
        self.player_total = 0
        self.dealer_total = 0
        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # -- DEAL TO DEALER
        print('\nThe dealer received two cards.')
        print('The card showing is:')
        random.shuffle(self.deck)
        for i in range(1):
            print(self.deck[i][1], self.deck[i][0])
            self.dealer_cards.append((self.deck[i][1], self.deck[i][0]))
            del self.deck[i]
            self.dealer_total = self.dealer_cards[0][1]
        # -- DEAL TO PLAYER
        print('\nYou received two cards:')
        random.shuffle(self.deck)
        for i in range(2):
            print(self.deck[i][1], self.deck[i][0])
            self.player_cards.append((self.deck[i][1], self.deck[i][0]))
            del self.deck[i]
        player_hand = self.player_cards[0][1] + self.player_cards[1][1]
        self.player_total = player_hand
        if player_hand == 21:
            self.blackjack()
        if player_hand > 21:
            self.bust()
        if player_hand < 21:
            self.moves()

    # -------WINNER CALCULATOR METHOD
    def play_calculator(self):
        # REVEAL DEALER'S SECOND CARD
        print('\nThe dealer reveals their second card...')
        random.shuffle(self.deck)
        for i in range(1):
            print(self.deck[i][1], self.deck[i][0])
            # -- UPDATE DEALER CARDS
            self.dealer_cards.append((self.deck[i][1], self.deck[i][0]))
            del self.deck[i]
        # -- UPDATE DEALER TOTAL
        dealer_hand = self.dealer_cards[0][1] + self.dealer_cards[1][1]
        self.dealer_total = dealer_hand
        # -- CHECK WINNER
        if dealer_hand == 21 and self.player_total != 21:
            self.dealer_wins()
        if dealer_hand > 21 and self.player_total <= 21:
            self.winner()
        if self.player_total > dealer_hand and self.player_total <= 21:
            self.winner()
        if dealer_hand > self.player_total and dealer_hand < 21:
            self.dealer_wins
        else:
            self.moves()

    # -------MOVES, USER INPUT METHOD
    def moves(self):

        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # -- GET USER INPUT
        print(f'Your current hand totals {self.player_total}')
        move = input(f'Would you like to "Hit" or "Stand"?\n').lower()
        # -- HIT OR STAND
        if move == 'hit':
            self.hit()
        if move == 'stand':
            self.play_calculator()
        else:
            print('Please choose "Hit" or "Stand"')
            self.moves()

    # -------HIT, GET CARD METHOD
    def hit(self):

        # -- ADD CARD
        print('\nYou received another card:')
        random.shuffle(self.deck)
        for i in range(1):
            print(self.deck[i][1], self.deck[i][0]
                  if i not in self.player_cards else self.hit())
            # -- UPDATE HAND
            self.player_cards.append((self.deck[i][1], self.deck[i][0]))
        # -- UPDATE PLAYER TOTAL
        player_hand = self.player_total + self.player_cards[-1][1]
        self.player_total = player_hand
        # -- CHECK WINNER
        if player_hand == 21:
            self.winner()
        if player_hand > 21:
            self.bust()
        if player_hand < 21:
            self.moves()

    # -------IF BLACKJACK METHOD
    def blackjack(self):
        # -- CELEBRATE BLACKJACK
        print('♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥')
        print('♦♠♣♥♦♠♣♥♦♠♣♥  BLACKJACK!!! ♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦')
        print('♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥\n')
        print(f'         Congratulations {self.player_name.title()}!')
        print('           You beat the dealer')
        # -- CHECK FOR BET / CONTINUE GAME
        self.victor = True
        if self.current_bet:
            self.money_handler()
        else:
            self.play_again()

    # -------IF BUST METHOD
    def bust(self):
        # -- YOU'RE BUSTED CELEBRATION
        print("~~~~~~~ BUST!!  YOU'RE A LOSER ~~~~~~~~~")
        print(f'           Sorry {self.player_name.title()}')
        print(
            f'      Player: {self.player_total}  |  Dealer: {self.dealer_total}')
        print('          You lost this hand')
        # -- UPDATE WALLET/BET
        self.victor = False
        if self.current_bet:
            self.money_handler()
        else:
            self.play_again()

    # -------DEALER WINS METHOD
    def dealer_wins(self):
        # -- YOU'RE A LOSER CELEBRATION
        print("~~~~~~~ The Dealer Wins, You're a Loser  ~~~~~~~~~")
        print(f'              Sorry {self.player_name.title()}')
        print(f'  Player: {self.player_total}  |  Dealer: {self.dealer_total}')
        print('             You lost this hand')
        # -- UPDATE WALLET/BET
        self.victor = False
        if self.current_bet:
            self.money_handler()
        else:
            self.play_again()

    # -------PLAYER WINS METHOD
    def winner(self):
        # -- CELEBRATE WINNER
        print('♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣  Winner!!! ♦♠♣♥♦♠♣♥♦♠♣♥♦♠♣♥♦')
        print(f'         Congratulations {self.player_name.title()}!')
        print(f'  Player: {self.player_total}  |  Dealer: {self.dealer_total}')
        print('            You beat the dealer')
        # -- UPDATE WALLET/BET
        self.victor = True
        if self.current_bet:
            self.money_handler()
        else:
            self.play_again()

    # INDIVIDUAL FUNCTION TO HANDLE BET CALCULATIONS
    def money_handler(self):
        # -- WINNER ACTION
        if self.victor == True:
            self.cash = self.cash + (self.current_bet * 2)
            print(f'\nYou won ${self.current_bet}!')
        # -- LOSER ACTION
        if self.victor == False:
            print(f'You lost ${self.current_bet}.')
        # -- CONTINE TO GAME
        ready = input('Press enter to continue:\n')
        if ready:
            self.play_again()
        else:
            self.play_again()

    # -------WALLET METHOD
    def wallet(self):

        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # -- DISPLAY CURRENT WALLET AMOUNT
        if self.cash > 50:
            print(f'              Your wallet is up to ${self.cash}!\n')
        if self.cash == 50:
            print(f'                    You have ${self.cash}\n')
        if self.cash < 50:
            print(f'              Your wallet is down to ${self.cash}\n')
        # Ask if the player wants to bet or go to the main menu
        print(f'            What would you like to do now?            ')
        # -- TAKE USER MENU INPUT
        deciding = True
        while deciding:
            action = input(
                f'         PLAY  |  BET  |  NEW PLAYER  |  QUIT\n').lower()
            if action == 'play' or 'play again':
                self.shuffle_deck()
            if action == 'bet':
                self.place_a_bet()
            if action == 'new player' or 'new':
                self.game_driver()
            if action == 'quit' or 'q':
                exit()
            else:
                print(
                    f'Please enter a valid selection, {self.player_name.title()}\n')

    # -------PLACE BET METHOD
    def place_a_bet(self):

        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # -- DISPLAY CURRENT WALLET AMOUNT
        if self.cash > 50:
            print(f'              cash is up to ${self.cash}!\n')
        if self.cash == 50:
            print(f'                    You have ${self.cash}\n')
        if self.cash < 50:
            print(f'              Your wallet is down to ${self.cash}\n')
        # -- PLACE BET, UPDATE CASH, UPDATE CURRENT BET
        getting_cash = True
        while getting_cash == True:
            bet_amount = int(input(f'How much would you like to bet?\n'))
            if bet_amount <= self.cash and bet_amount >= 1:
                self.cash = self.cash - bet_amount
                self.current_bet = bet_amount
                print(
                    f'          You have bet ${self.current_bet} and now')
                print(f'        have ${self.cash} in your wallet.')
                self.shuffle_deck()

            else:
                print("You don't have that. Please enter a valid amount")
                self.place_a_bet()

    # -------PLAY AGAIN MENU METHOD
    def play_again(self):

        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # -- DISPLAY NAME, WALLET UP/DOWN STATUS
        if self.victor == False:
            print(f'\n                Tough luck, {self.player_name.title()}')
        if self.victor == True:
            print(
                f'\n              You\'re on a roll, {self.player_name.title()}!')
        if self.cash > 50:
            print(f'              Your wallet is up to ${self.cash}!\n')
        if self.cash == 50:
            print(f'                You still have ${self.cash}\n')
        if self.cash < 50:
            print(f'              Your wallet is down to ${self.cash}\n')
        # -- PLAY AGAIN MENU
        print(f'          What would you like to do now?            ')
        # -- TAKE USER INPUT MENU
        action = input(
            f'         PLAY   |  BET  |  NEW PLAYER  |  QUIT\n').lower()
        if action == 'play':
            self.current_bet = 0
            self.shuffle_deck()
        if action == 'bet':
            self.place_a_bet()
        if action == 'new':
            self.cash = 50
            self.current_bet = 0
            self.game_driver()
        if action == 'quit':
            exit()
        else:
            print(
                f'Please enter a valid selection, {self.player_name.title()}:\n')

    # -------DRIVER MENU METHOD
    def game_driver(self):

        # -- WELCOME MESSAGE
        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'               Python Casino Blackjack                ')
        print(f'                                                      ')
        print(f'                We have a new player!                 ')
        # -- GET/VERIFY PLAYER NAME
        while True:
            self.player_name = input(
                f'What is your name?\n').lower()
            if self.player_name.isalpha():
                break
            print("\nPlease enter an actual name! :(")
        # -- DISPLAY CURRENT STATUS AND MENU
        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'\n                       Hi {self.player_name.title()}!')
        print(f'                You currently have ${self.cash}\n')
        print(f'            What would you like to do now?            ')
        # -- TAKE USER MENU INPUT
        deciding = True
        while deciding:
            action = input(
                f'        PLAY  |  BET  |  VIEW WALLET  |  QUIT\n').lower()
            if action == 'play':
                deciding = False
                self.shuffle_deck()
            if action == 'bet':
                deciding = False
                self.place_a_bet()
            if action == 'view wallet' or 'view' or 'wallet':
                deciding = False
                self.wallet()
            if action == 'quit' or 'q':
                exit()
            else:
                print(
                    f'Please enter a valid selection, {self.player_name.title()}:\n')
