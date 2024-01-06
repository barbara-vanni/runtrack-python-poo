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



def BlackJack():
    run = True
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0   

    while len(player_hand) < 2:
        jeu.deal_cards(player_hand)

        player_score += jeu.calculate_hand_value(player_hand)

        # check if the first two cards are aces and if so, subtract 10 from the player_score
        # if len(player_hand) == 2:
        #     if player_hand[0].cards_values == 'Ace' and player_hand[1].cards_values == 'Ace':
        #         player_score -= 10
        print(f"Player card is {player_hand} with {jeu.calculate_hand_value(player_hand)} points")

        jeu.deal_cards(dealer_hand)
        dealer_score += jeu.calculate_hand_value(dealer_hand)

        # if len(dealer_hand) == 2:
        #     if dealer_hand[0].cards_values == 'Ace' and dealer_hand[1].cards_values == 'Ace':
        #         dealer_score -= 10

        print(f"Dealer card is {dealer_hand} with {jeu.calculate_hand_value(dealer_hand)} points")

    if player_score == 21:
        print('Player wins!')
        run = False


    while player_score < 21 :

        choice = input('Do you want to hit (h) or stand (s)? ')

        if choice == 'h':
            jeu.hit(player_hand)
            player_score += jeu.calculate_hand_value(player_hand)
            print(f"Player card is {player_hand} with {jeu.calculate_hand_value(player_hand)} points")
        elif choice == 's':
            break
        

    # if player_score == 21:
    #     print('Player wins!')
    #     run = False

    # if player_score > 21:
    #     print('Player loses!')
    #     run = False
            
    while dealer_score < 21:
        if dealer_score < 17:
            jeu.hit(dealer_hand)
            dealer_score += jeu.calculate_hand_value(dealer_hand)
            print(f"Dealer card is {dealer_hand} with {jeu.calculate_hand_value(dealer_hand)} points")
        else:
            break
        
    if dealer_score == 21:
        print('Dealer wins!')
        run = False

    if dealer_score > 21:    
        print('Dealer loses!')
        run = False

    if dealer_score == player_score:
        print('Tie game !')
        run = False

    elif player_score > dealer_score:
        print('Player wins!')
        run = False
    else:
        print('Dealer wins!')
        run = False



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


