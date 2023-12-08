with open('input2.txt') as file:
    data = file.read().strip()

def check_cubes_amount(data):
    games_list = data.split('\n')
    games_id_sum = 0

    for game in games_list: 
        game_valid = True
        hand_dict = {
            'red': 0,
            'green': 0,
            'blue': 0}
        for cubes_at_hand in game.split(':')[1].split(';'):
            for cubes in cubes_at_hand.split(','):
                hand_dict[cubes.split()[1]] = int(cubes.split()[0])

            
            if not compare_amounts(hand_dict):
                game_valid = False
                break

        games_id_sum += int(game.split(':')[0].split(' ')[1]) if game_valid else 0   
    return games_id_sum


def compare_amounts(input_dict):
    return all(input_dict[color] <= limit for color, limit in [('red', 12), ('blue', 14), ('green', 13)])

print(check_cubes_amount(data))