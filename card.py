import random

values={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
# this is a dictionary- global variable
suits= ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# these are tuples because we dont want to change the values
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self) -> str:
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self) -> None:
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                #create the card object and append it to the list of all cards
                created_card= Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self): # deal one card from the top of the deck
        return self.all_cards.pop()

class Player:
    def __init__(self, name) -> None:
        self.name=name
        self.all_cards=[]

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards)== type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f'Player {self.name} has {len(self.all_cards)} cards'




# two_hearts=Card("hearts", "King")
# three_clubs=Card("Clubs","Three")
# print(two_hearts.value== three_clubs.value)

# new_deck=Deck()
# for card_object in new_deck.all_cards:
#     print(card_object)
# print("shuffled cards are:  ")
# new_deck.shuffle()
# for card_object in new_deck.all_cards:
#     print(card_object)
# mycard1=new_deck.deal_one()
# mycard2=new_deck.deal_one()
# mycard3=new_deck.deal_one()
# print(mycard, mycard2, mycard3)
# print(len(new_deck.all_cards))

# new_player=Player("Maddy")

# new_player.add_cards([mycard1,mycard2, mycard3])
# print(new_player)
# print(new_player.all_cards[0])
# print(new_player.all_cards[1])
# print(new_player.all_cards[2])
# new_player.remove_one()
# print(new_player)
# print(new_player.all_cards[0])
# print(new_player.all_cards[1])


#GAME SETUP
# WHILE GAME ON
# WHILE AT WAR

#CREATE THE PLAYERS
player_one =Player("One")
player_two=Player("Two")

#CREATE THE DECK
new_deck=Deck()
new_deck.shuffle()

# SPLIT THE DECK BETWEEN THE TWO PLAYERS
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# print(len(player_one.all_cards))
# print(len(player_two.all_cards))

game_on=True
round_num=0
while game_on:
    round_num+=1
    print(f"Round {round_num} \n")

    if len(player_one.all_cards)==0:
        print('Player One is out of cards! Player Two WINS!!!!!!')
        game_on=False
        break
    
    elif len(player_two.all_cards)==0:
        print('Player Two is out of cards! Player One WINS!!!!!!')
        game_on=False
        break

    # START A NEW ROUND
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())

    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())

    # WHILE AT WAR
    at_war=True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war=False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war=False

        else:
            print('WAR!!')
            if len(player_one.all_cards)<5:
                print("Player one unable to declare war, and player two WINS")
                game_on=False
                break
            elif len(player_two.all_cards)<5:
                print("Player two unable to declare war, and player one WINS")
                game_on=False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


