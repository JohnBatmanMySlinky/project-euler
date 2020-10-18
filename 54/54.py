# 1: High Card: Highest value card.
# 2: One Pair: Two cards of the same value.
# 3: Two Pairs: Two different pairs.
# 4: Three of a Kind: Three cards of the same value.
# 5: Straight: All cards are consecutive values.
# 6: Flush: All cards of the same suit.
# 7: Full House: Three of a kind and a pair.
# 8: Four of a Kind: Four cards of the same value.
# 9: Straight Flush: All cards are consecutive values of same suit.
# 10: Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# import wget
# wget.download('https://projecteuler.net/project/resources/p054_poker.txt', './54.txt')

with open('./54.txt') as f:
    file = []
    for l in f:
        file.append(l.strip('\n').split(' '))

n_of_a_kind_dict = {
    '21': 2,
    '22': 3,
    '31': 4,
    '41': 8
}

straight_dict = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14
}

def n_of_a_kind(hand, n, i):
    hand_val = [x[0] for x in hand]
    target = ''.join([str(n)] * n * i)
    if (''.join(sorted([str(hand_val.count(x)) for x in hand_val]))).find(target) > -1:
        return(n_of_a_kind_dict[str(n)+str(i)])
    else:
        return(0)

def check_full_house(hand):
    if n_of_a_kind(hand,3,1) & n_of_a_kind(hand,2,1):
        return(7)
    else:
        return(0)

def check_straight(hand):
    hand_num = sorted([straight_dict[x[0]] for x in hand])
    answer = []
    for x in range(1,5):
        answer.append(hand_num[x] == hand_num[x-1]+1)
    if all(answer):
        return(5)
    else:
        return(0)

def check_flush(hand):
    if all([x[1] == hand[0][1] for x in hand]):
        return(6)
    else:
        return(0)

def check_straight_flush(hand):
    if check_straight(hand) & check_flush(hand):
        return(9)
    else:
        return(0)

def check_royal_flush(hand):
    royal = ['T', 'J', 'Q', 'K', 'A']
    for each in hand:
        if each[0] in royal:
            royal.remove(each[0])
    if (not royal) & (check_flush(hand)):
        return(10)
    else:
        return(0)

def winner(p1, p2):


p1_wins = 0
for each in file[:1]:
    p1_hand = each[:5]
    p2_hand = each[5:]


# translate each hand to a point value
# deal with ties
