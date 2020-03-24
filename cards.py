import random

class Cards:
    def __init__(self, face):
        self.face = face
    def __str__(self):
        if self.face < 11 and self.face > 1:
            return("I am a(n) {}".format(self.face))
        elif self.face == 1:
            return("I am an Ace")
        elif self.face == 11:
            return ("I am a Jack")
        elif self.face == 12:
            return("I am a Queen")
        else:
            return("I am a King")

class Red_cards(Cards):
    def __init__(self, face):
        Cards.__init__(self, face)
        self.color = 'Red'
    def __str__(self):
        if self.face < 11 and self.face > 1:
            return("I am a {} {}".format(self.color, self.face))
        elif self.face == 1:
            return("I am a {} Ace")
        elif self.face == 11:
            return ("I am a {} Jack")
        elif self.face == 12:
            return("I am a {} Queen")
        else:
            return("I am a {} King") 

class Black_cards(Cards):
    def __init__(self, face):
        Cards.__init__(self, face)
        self.color = 'Black'
    def __str__(self):
        if self.face < 11 and self.face > 1:
            return("I am a {} {}".format(self.color, self.face))
        elif self.face == 1:
            return("I am a {} Ace".format(self.color))
        elif self.face == 11:
            return("I am a {} Jack".format(self.color))
        elif self.face == 12:
            return("I am a {} Queen".format(self.color))
        else:
            return("I am a {} King".format(self.color))

class Diamond_cards(Red_cards, Cards):
    def __init__(self, face):
        Red_cards.__init__(self, face)
        Cards.__init__(self, face)
        self.suit = 'Diamonds'
    def __str__(self):
        if self.face < 11 and self.face > 1:
            return("I am a(n) {} of {}\n".format(self.face, self.suit))
        elif self.face == 1:
            return("I am an Ace of {}\n".format(self.suit))
        elif self.face == 11:
            return ("I am a Jack of {}\n".format(self.suit))
        elif self.face == 12:
            return("I am a Queen of {}\n".format(self.suit))
        else:
            return("I am a King of {}\n".format(self.suit)) 

class Heart_cards(Red_cards, Cards):
    def __init__(self, face):
        Red_cards.__init__(self, face)
        Cards.__init__(self, face)
        self.suit = 'Hearts'
    def __str__(self):
        if self.face < 11 and self.face > 1:
            return("I am a(n) {} of {}\n".format(self.face, self.suit))
        elif self.face == 1:
            return("I am an Ace of {}\n".format(self.suit))
        elif self.face == 11:
            return ("I am a Jack of {}\n".format(self.suit))
        elif self.face == 12:
            return("I am a Queen of {}\n".format(self.suit))
        else:
            return("I am a King of {}\n".format(self.suit)) 

class Spade_cards(Black_cards, Cards):
    def __init__(self, face):
        Black_cards.__init__(self, face)
        Cards.__init__(self, face)
        self.suit = 'Spades'
    def __str__(self):
        if self.face < 11 and self.face > 1:
            return("I am a(n) {} of {}\n".format(self.face, self.suit))
        elif self.face == 1:
            return("I am an Ace of {}\n".format(self.suit))
        elif self.face == 11:
            return ("I am a Jack of {}\n".format(self.suit))
        elif self.face == 12:
            return("I am a Queen of {}\n".format(self.suit))
        else:
            return("I am a King of {}\n".format(self.suit)) 

class Club_cards(Black_cards, Cards):
    def __init__(self, face):
        Black_cards.__init__(self, face)
        Cards.__init__(self, face)
        self.suit = 'Clubs'
    def __str__(self):
        if self.face < 11 and self.face > 1:
            return("I am a(n) {} of {}\n".format(self.face, self.suit))
        elif self.face == 1:
            return("I am an Ace of {}\n".format(self.suit))
        elif self.face == 11:
            return ("I am a Jack of {}\n".format(self.suit))
        elif self.face == 12:
            return("I am a Queen of {}\n".format(self.suit))
        else:
            return("I am a King of {}\n".format(self.suit)) 

card_dictionary = {
    1 : Diamond_cards(1),
    2 : Diamond_cards(2),
    3 : Diamond_cards(3),
    4 : Diamond_cards(4),
    5 : Diamond_cards(5),
    6 : Diamond_cards(6),
    7 : Diamond_cards(7),
    8 : Diamond_cards(8),
    9 : Diamond_cards(9),
    10 : Diamond_cards(10),
    11 : Diamond_cards(11),
    12 : Diamond_cards(12),
    13 : Diamond_cards(13),
    14 : Heart_cards(1),
    15 : Heart_cards(2),
    16 : Heart_cards(3),
    17 : Heart_cards(4),
    18 : Heart_cards(5),
    19 : Heart_cards(6),
    20 : Heart_cards(7),
    21 : Heart_cards(8),
    22 : Heart_cards(9),
    23 : Heart_cards(10),
    24 : Heart_cards(11),
    25 : Heart_cards(12),
    26 : Heart_cards(13),
    27 : Spade_cards(1),
    28 : Spade_cards(2),
    29 : Spade_cards(3),
    30 : Spade_cards(4),
    31 : Spade_cards(5),
    32 : Spade_cards(6),
    33 : Spade_cards(7),
    34 : Spade_cards(8),
    35 : Spade_cards(9),
    36 : Spade_cards(10),
    37 : Spade_cards(11),
    38 : Spade_cards(12),
    39 : Spade_cards(13),
    40 : Club_cards(1),
    41 : Club_cards(2),
    42 : Club_cards(3),
    43 : Club_cards(4),
    44 : Club_cards(5),
    45 : Club_cards(6),
    46 : Club_cards(7),
    47 : Club_cards(8),
    48 : Club_cards(9),
    49 : Club_cards(10),
    50 : Club_cards(11),
    51 : Club_cards(12),
    52 : Club_cards(13),
}

card_deck = []
#test_full_house = []
test_three = []

for i in range(52):
    curr_card = card_dictionary.get(i+1)
    card_deck.append(curr_card)
    #print(curr_card)
    #print(card_deck)

#test_full_house.append(card_deck[2])
#test_full_house.append(card_deck[15])
#test_full_house.append(card_deck[9])
#test_full_house.append(card_deck[22])
#test_full_house.append(card_deck[35])

test_three.append(card_deck[2])
test_three.append(card_deck[15])
test_three.append(card_deck[28])
test_three.append(card_deck[41])
test_three.append(card_deck[6])

for i in test_three:
    print(i)
print()
sysRan = random.SystemRandom()
sysRan.shuffle(card_deck)

def deal_cards(card_deck, size_of_hand):
    hand = []
    for i in range(size_of_hand):
        hand.append(card_deck.pop())
    return hand

#def compare_hands(dealer_hand, player_hand):

def check_straight(curr_deck):
    prev_val = 0
    val_list = []
    for i in curr_deck:
        val_list.append(i.face)
    val_list.sort()
    for i in val_list:
        if prev_val == 0:
            prev_val = i
        else:
            if (i - prev_val) != 1:
                return False
            else:
                #print(i - prev_val)
                prev_val = i
    return True

def check_flush(curr_deck):
    match_suit = curr_deck[0].suit
    for i in curr_deck:
        if match_suit != i.suit:
            return False
    return True

def check_straight_flush(curr_deck):
    if (check_straight(curr_deck)) and (check_flush(curr_deck)):
        return True
    else:
        return False

def check_set_of_num(curr_deck, set_num):
    curr_val = 0
    total_same = 0
    set_num_found = False
    val_list = []
    for i in curr_deck:
        val_list.append(i.face)
    val_list.sort()
    for i in val_list:
        if curr_val == 0:
            curr_val = i
            total_same += 1
        else:
            if i == curr_val:
                total_same += 1
                if total_same == set_num:
                    set_num_found = True
            else:
                total_same = 0
                curr_val = i
                total_same += 1  
    if set_num_found:
        return True
    else:
        return False

def check_full_house(curr_deck):
    val_list = []
    curr_val = 0
    running_total = 0
    was_two = False
    for i in curr_deck:
        val_list.append(i.face)
    val_list.sort()
    for i in val_list:
        if curr_val == 0:
            curr_val = i
            running_total += 1
        else:
            if i == curr_val:
                running_total += 1
            else:
                if (running_total == 3): 
                    running_total = 0
                    curr_val = i
                    running_total += 1
                elif (running_total == 2) and (was_two == False):
                    running_total = 0
                    curr_val = i
                    running_total += 1
                    was_two = True  
                else:                      #means it is not currently 3, it is not 2, or it was 2 but there was already a pair
                    return False
    return True

def check_two_pair(curr_deck):
    num_pairs = 0
    curr_val = 0
    total_same = 0
    val_list = []
    for i in curr_deck:
        val_list.append(i.face)
    val_list.sort()
    for i in val_list:
        if curr_val == 0:
            curr_val = i
            total_same += 1
        else:
            if i == curr_val:
                total_same += 1
                if total_same == 2:
                    num_pairs += 1
                    total_same = 0
                    curr_val = 0
            else:
                total_same = 0
                curr_val = i
    if num_pairs != 2:
        return False
    else:
        return True


player_hand = deal_cards(card_deck, 5)

dealer_hand = deal_cards(card_deck, 5)

for i in player_hand:
    print(i)

print("\n")

for i in dealer_hand:
    print(i)

print(check_full_house(player_hand))
#print(check_full_house(test_full_house))
print(check_set_of_num(test_three, 3))