lottery_numbers = {13, 21, 22, 5, 8}
players = [
    {
    'name': 'Bob',
    'numbers': {1, 21, 3, 4, 5}
    },
    {
    'name': 'John',
    'numbers': {13, 8, 3, 22, 5}
    }
]

player1_name = players[0]["name"]
player2_name = players[1]["name"]

player1_num = players[0]["numbers"]
player2_num = players[1]["numbers"]

intersection1 = lottery_numbers.intersection(player1_num)
intersection2 = lottery_numbers.intersection(player2_num)

print(f"Congratulations, {player1_name}. You got {len(intersection1)} numbers right.")
print(f"Congratulations, {player2_name}. You got {len(intersection2)} numbers right.")