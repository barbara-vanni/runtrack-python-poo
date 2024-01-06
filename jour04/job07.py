import random

class Carte:
    def __init__(self):
        self.valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.couleurs = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.carte_valeurs = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}
        self.deck = []


        def get_deck(self):
            return self.deck

        for couleur in self.couleurs:
            for valeur in self.valeurs:
                carte_valeur = self.carte_valeurs[valeur] 
                self.deck.append(f'{valeur} of {couleur}')

        random.shuffle(self.deck)


class Jeu(Carte):
    def __init__(self):
        Carte.__init__(self)
        self.deck = self.deck

    def melanger_paquet(self):
        random.shuffle(self.deck)
    
    def deal_cards(self, hand):
        for i in range(2): 
            card = self.deck.pop() 
            hand.append(card)

    def hit(self, hand):
        card = self.deck.pop()
        hand.append(card)

    def calculate_hand_value(self,hand):
        value = 0
        has_ace = False

        for card in hand:
            self.couleurs = card.split()[0]

            if self.couleurs.isdigit():
                value += int(self.couleurs)
            elif self.couleurs in ['Jack', 'Queen', 'King']:
                value += 10
            elif self.couleurs == 'Ace':
                has_ace = True
                value += 11

        if has_ace and value > 21:
            value -= 10
        return value

player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0   

def BlackJack():
    run = True

    while run:
        jeu.deal_cards(player_hand)
        jeu.deal_cards(dealer_hand)
        print(f"La main du joueur est {player_hand} comptabilisant {jeu.calculate_hand_value(player_hand)}")
        print(f"La main du dealer est {dealer_hand} comptabilisant {jeu.calculate_hand_value(dealer_hand)}")

        while True:
            action = input('Do you want to hit or stand? ')
            if action.lower() == 'hit':
                jeu.hit(player_hand)
                print(f"La main du joueur est {player_hand} comptabilisant {jeu.calculate_hand_value(player_hand)}")
                if int(jeu.calculate_hand_value(player_hand)) > 21:
                    print('Player loses the game!')
                    run = False
                    break
            elif action.lower() == 'stand':
                break

        while jeu.calculate_hand_value(dealer_hand) < 17:
            jeu.hit(dealer_hand)
            print(f"La main du dealer est {dealer_hand} comptabilisant {jeu.calculate_hand_value(dealer_hand)}")

    if jeu.calculate_hand_value(dealer_hand) > 21:
        print('Dealer loses the game! YOU WIN!')

    if jeu.calculate_hand_value(player_hand) > jeu.calculate_hand_value(dealer_hand):
        print('Player wins!')
    elif jeu.calculate_hand_value(player_hand) < jeu.calculate_hand_value(dealer_hand):
        print('Dealer wins!')
    else:
        print('It\'s a tie!')


carte_deck = Carte()
# print(carte_deck.deck)
jeu = Jeu()
# print(jeu.deck)
# jeu.melanger_paquet()



# jeu.deal_cards(player_hand)
# jeu.deal_cards(dealer_hand)

# print(player_hand)
# print(dealer_hand)
# print(jeu.calculate_hand_value(player_hand))

BlackJack()


