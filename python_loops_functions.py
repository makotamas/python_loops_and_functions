# 1. feladat
def divisibility(arg: list):
    for num in arg:
        if num % 2 == 0:
            print(f'{num}: osztható')
        else:
            print(f'{num}: nem osztható')


nums = [3,4,9,6,2]

divisibility(nums)

# 2. feladat
def print_players(players: list):
    for index, player in enumerate(players):
        print(f'{index + 1}. {player}')

players = ['Peter', 'Kate', 'John']

print_players(players)

# 3. feladat
def function(arg):
    result = []
    for i in arg:
        item_type = type(i).__name__
        result.append(item_type)
    return result
        
x = ['', 4, True]

print(function(x))