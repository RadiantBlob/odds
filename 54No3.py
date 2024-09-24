from random import randint

target = [str(a) for a in range(1, 11)]
# print(target)

def toss() -> str:  return str(randint(1, 10))

def play() -> (str, int):
    cards = ""
    num = 0
    while True:
        cards += toss() + "-"
        num += 1
        if len(cards) < 9:  continue
        if all(x in cards for x in target):
            return (cards[:-3], num)

games = [play() for _ in range(20)]
[print(game[0], game[1]) for game in games]

print("Average length: ", sum([game[1] for game  in games]) / len(games))
