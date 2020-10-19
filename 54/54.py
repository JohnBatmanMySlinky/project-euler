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

def check_n_of_a_kind(hand, n, i):
    # bool, pass check
    hand_val = [x[0] for x in hand]
    target = ''.join([str(n)] * n * i)
    answer = (''.join(sorted([str(hand_val.count(x)) for x in hand_val]))).find(target) > -1

    # max used in answer
    if answer:
        val = list(set([x for x in hand_val if hand_val.count(x) == n]))
    else:
        val = '0'

    # rest of hand to be checked again
    remainder = [x for x in hand if x[0] != val[0]]

    # return
    return([answer, straight_dict[val[0]], remainder])

def check_full_house(hand):
    # bool answer
    answer = check_n_of_a_kind(hand,3,1)[0] & check_n_of_a_kind(hand,2,1)[0]

    # value of winning
    hand_val = [x[0] for x in hand]
    val = []
    if answer:
        val.append(list(set([x for x in hand_val if hand_val.count(x) == 3]))[0])
        val.append(list(set([x for x in hand_val if hand_val.count(x) == 2]))[0])
        for z in range(len(val)):
            val[z] = straight_dict[val[z]]
    else:
        val.append(0)

    #full house uses all 5 cards so no remainder
    remainder = [0]

    #return
    return([answer, val, remainder])

def check_straight(hand):
    #get answer
    hand_num = sorted([straight_dict[x[0]] for x in hand])
    answer = []
    for x in range(1,5):
        answer.append(hand_num[x] == hand_num[x-1]+1)
    answer = all(answer)

    # get value
    val = []
    if answer:
        val.append(max(hand_num))
    else:
        val = [0]

    # get remainder
    remainder = [0]

    # return
    return([answer, val, remainder])

def check_flush(hand):
    return(all([x[1] == hand[0][1] for x in hand]))

test = ['9D', 'TD', '8D', 'QD', 'KD']
print(check_straight(test))

def check_straight_flush(hand):
    return(check_straight(hand) & (check_flush(hand)>0))

def check_royal_flush(hand):
    royal = ['T', 'J', 'Q', 'K', 'A']
    for each in hand:
        if each[0] in royal:
            royal.remove(each[0])
    if (not royal) & check_flush(hand):
        return(10)
    else:
        return(0)

scoring_dict = {
    "check_royal_flush": [],
    "check_straight_flush": [],
    "check_n_of_a_kind": [4,1],
    "check_full_house": [],
    "check_flush": [],
    "check_straight": [],
    "check_n_of_a_kind": [3,1],
    "check_n_of_a_kind": [2,2],
    "check_n_of_a_kind": [2,1],
}

def winner(p1, p2):
    for k, v in scoring_dict.items():
        if not v:
            p1_score = globals()[k](p1)
            p2_score = globals()[k](p2)
        else:
            p1_score = globals()[k](p1,
                                    v[0],
                                    v[1])
            p2_score = globals()[k](p2,
                                    v[0],
                                    v[1])
        # running thru check functions in order, so if someone wins, return and stop
        #p1 wins
        if p1_score & ~p2_score:
             return(1)
        #p2 wins
        if ~p1_score & p2_score:
             return(2)
    # tie!
    # or highest card
    return(0)

# def tie_breaker()


# test  = ['3C', '3D', '3S', '7S', '7D']
# func = "check_n_of_a_kind"
# print(locals()[func](test,2,1))



p1_wins = 0
for each in file[:1]:
# for each in [['2D', '9C', 'AS', 'AH', 'AC', '3D', '6D', '7D', 'TD', 'QD']]:
# for each in [['5H', '5C', '6S', '7S', 'KD', '2C', '3S', '8S', '8D', 'TD']]:
    p1_hand = each[:5]
    p2_hand = each[5:]
    result = winner(p1_hand, p2_hand)
    if result == 1:
        p1_wins += 1
    if result == 0:
        p1_wins = tie_breaker()


# translate each hand to a point value
# deal with ties
