from random import randint
number = 2000

def bids() -> str:
    return "".join([str(randint(0, 9)) for _ in range(15)])

c = 0
for _ in range(number):
    b = bids()
    
    count = {str(x): 0 for x in range(0, 10)}
    for char in b:
        count[char] += 1

    not_sold = [key for key, val in count.items() if val == 0]
    # print(b, not_sold)
    c += len(not_sold)

print(c / number)

# print(bids())
