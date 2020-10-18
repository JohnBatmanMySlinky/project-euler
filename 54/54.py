# High Card: Highest value card.

# import wget
# wget.download('https://projecteuler.net/project/resources/p054_poker.txt', './54.txt')

with open('./54.txt') as f:
    file = []
    for l in f:
        file.append(l.strip('\n').split(' '))

test = ['9H', 'QH', '9H', 'QH', '9H']

def n_of_a_kind(hand, n, i):
    hand_val = [x[0] for x in hand]
    target = ''.join([str(n)] * n * i)
    return((''.join(sorted([str(hand_val.count(x)) for x in hand_val]))).find(target) > -1)

def check_full_house(hand):
    return(n_of_a_kind(hand,3,1) & n_of_a_kind(hand,2,1))

def check_straight(hand):
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
    hand_num = sorted([straight_dict[x[0]] for x in hand])
    answer = []
    for x in range(1,5):
        answer.append(hand_num[x] == hand_num[x-1]+1)
    return(all(answer))

def check_flush(hand):
    return(all([x[1] == hand[0][1] for x in hand]))

def check_straight_flush(hand):
    return(check_straight(hand) & check_flush(hand))

def check_royal_flush(hand):
    royal = ['T', 'J', 'Q', 'K', 'A']
    for each in hand:
        if each[0] in royal:
            royal.remove(each[0])
    if (not royal) & (check_flush(hand)):
        return(True)
    else:
        return(False)
