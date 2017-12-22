

def black_jack(player_name):
    class Card:
        def __init__(self, suit, rank, deck_id):
            self.suit = suit
            self.rank = rank
            self.deck_id = deck_id
            self.value = self.get_value()

        def get_value(self):
            try:
                return int(self.rank)
            except ValueError:
                if self.rank in 'JQK':
                    return 10
                elif self.rank is 'A':
                    return 11

        def __str__(self):
            royalty = {'A': 'Ace', 'K': 'King', 'Q': 'Queen', 'J': 'Jack'}
            try:
                return '{} of {}'.format(royalty[self.rank], self.suit)
            except KeyError:
                return '{} of {}'.format(self.rank, self.suit)

        def __repr__(self):
            return '{}{}'.format(self.rank[0], self.suit[0])


    import uuid
    import random

    suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


    class Deck:
        def __init__(self):
            self.deck_id = str(uuid.uuid4())[:4]
            self.cards = self.build_deck()

        def build_deck(self):
            deck = []
            for suit in suits:
                for rank in ranks:
                    deck.append(Card(suit, rank, self.deck_id))
            return deck

        def shuffle(self):
            return random.shuffle(self.cards)

        def cut(self):
            cut_int = random.randint(20, 30)
            self.cards = self.cards[cut_int:]+self.cards[:cut_int]
            return self.cards

        def draw(self):
            return self.cards.pop(0)



        def __repr__(self):
            repr_cards = []
            for c in self.cards:
                repr_cards.append(repr(c))
            return '-'.join(repr_cards)

        def __str__(self):
            str_cards = []
            for c in self.cards:
                str_cards.append(str(c))
            return ', '.join(str_cards)


    class Hand:
        def __init__(self, deck):
            self.deck = deck
            self.starting_hand = self.assign_starting_hand()
            self.hand = self.starting_hand[:]

        def assign_starting_hand(self):
            self.starting_hand = []
            for i in range(2):
                self.starting_hand.append(self.deck.draw())
            return self.starting_hand

        def add_card(self):
            card = self.deck.draw()
            self.hand.append(card)
            return self.hand

        def score(self):
            score = 0
            for c in self.hand:
                score += c.value
            num_aces = len([x for x in self.hand if x.rank is 'A'])
            while num_aces:
                if score > 21:
                    score -= 10
                    num_aces -= 1
                else:
                    break
            return score

        def __str__(self):
            return 'Your hand is: {}.'.format(', '.join(str(c) for c in self.hand))


    def dealer(dealer_hand):
        while True:
            score = dealer_hand.score()
            if score > 21:
                print('Dealer hand: {}'.format(', '.join(str(c) for c in dealer_hand.hand)))
                return 'bust'
            elif dealer_hand.hand == dealer_hand.starting_hand and score == 21:
                print('Dealer hand: {}'.format(', '.join(str(c) for c in dealer_hand.hand)))
                return 'blackjack'
            if score >= 17:
                print('Dealer hand: {}'.format(', '.join(str(c) for c in dealer_hand.hand)))
                return score
            else:
                dealer_hand.add_card()
                continue


    def new_game(players=1, d=Deck()):
        d.shuffle()
        d.cut()
        d_hand = Hand(d)
        p_hands = [Hand(d) for x in range(players)]
        return d, d_hand, p_hands


    def evaluate_hand(h):
        print(h)
        score = h.score()
        if score > 21:
            print('{}: Bust'.format(score))
            return 'bust'
        elif h.hand == h.starting_hand and score == 21:
            print('21: Blackjack!')
            return 'blackjack'
        else:
            return act(h)


    def act(h):
        choice = input(
            'Your score is {}. What would you like to do? H for hit or S for stay: '.format(h.score())).lower()
        if choice in 'hit':
            try:
                h.add_card()
            except IndexError:
                print('Deck is empty')
                exit()
            return evaluate_hand(h)
        else:
            return h.score()


    def winnings(d_final_hand, f_h):
        if f_h == 'bust':
            print('You have lost this hand.')
            return 0
        elif f_h == d_final_hand:
            print('Tie! You must play again.')
            return 0
        elif d_final_hand == 'blackjack':
            print('You have lost this hand.')
            return 0
        elif f_h == 'blackjack':
            print('Blackjack! You have won!')
            return 1
        elif d_final_hand == 'bust' or f_h > d_final_hand:
            print('You have won!')
            return 1
        else:
            print('You have lost this hand.')
            return 0


    def game(players=1, player_name = player_name):
        current_game = new_game(players)
        d = current_game[0]
        d_hand = current_game[1]
        p_hands = current_game[2]
        p_final_hands = []
        query = input('Press enter to play a hand of blackjack, or Q to quit: '.lower())
        if query == '':
            print('The dealer\'s face-up card is {}.'.format(d_hand.hand[0]))
            for h in p_hands:
                print(f'{player_name}:')
                p_final_hands.append(evaluate_hand(h))
            d_final_hand = dealer(d_hand)
            print('Dealer: {}'.format(d_final_hand))
            for f_h in p_final_hands:
                print(f'{player_name}:')
                return winnings(d_final_hand, f_h)

        elif query == 'q':
            exit()
        else:
            print('That is not a valid entry.')


    return game()

