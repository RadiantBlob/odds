from random import randint 

def toss() -> chr: return ("M", "F")[randint(0, 1)]

def play() -> str:
    kids = ""
    for i in range(6):
        gender = toss()
        kids += gender
        if "M" in kids and "F" in kids:
            return kids
    return kids

games = [play() for _ in range(20)]
[print(game) for game in games]
