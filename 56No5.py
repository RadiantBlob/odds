from random import randint
num_games = 40

def toss() -> (int, int): return (randint(1, 4), randint(1, 4))

def play() -> int:
    return sum(toss())
table = {a: 0 for a in range(2, 9)}

for _ in range(num_games):
    throw = play()
    table[throw] += 1
    
[print(f"{a} was rolled {b} times with a propability of {b / num_games}") for a, b in list(table.items())]
