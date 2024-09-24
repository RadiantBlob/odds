from random import randint

target = [str(a) for a in range(1, 6)]

def toss() -> str:  return str(randint(1, 5))

def play() -> (str, int):
    taxis = ""
    num = 0 
    while True:
        taxis += toss() + " "
        num += 1
        if len(taxis) < 5:  continue
        if all(x in taxis for x in target):
            return (taxis[:-1], num)

games = [play() for _ in range(20)]
[print(game[0], game[1]) for game in games]

print("Average length: ", sum([game[1] for game  in games]) / len(games))

