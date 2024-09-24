from random import randint

def toss() -> chr: return ("Z", "K")[randint(0, 1)]

def play() -> (str, int, str):
    result = ""
    while True:
        result += toss()
        if len(result) < 2: continue
        if "ZZZ" in result:
            return (result, len(result), "Anton")
        elif "ZKZ" in result:
            return (result, len(result), "Egon")


games = [play() for _ in range(20)]

max_len = max([game[1] for game in games])
[print(f"{game[0]}{' ' * (max_len + 2 - game[1])}{game[2]}") for game in games]

print(f"Sum of all tosses in {len(games)} games: ", total := sum([game[1] for game in games]),"\nAverage number of tosses per game: ", total / len(games))
anton = sum([game[2] == "Anton" for game in games])
egon = sum([game[2] == "Egon" for game in games])
print(f"Anton won: {anton} times \nEgon won: {egon} times")
print("Egon won ", egon / anton, " times more")
