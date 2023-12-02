


import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path



def main():
    data_location = Path("./data/Day_02.txt")

    with open(data_location, "r") as f:
        lines = f.readlines()

    #For part 1
    max_values_valled_game = {'red' : 12,  'green' : 13, 'blue' : 14,} 

    invalled_games = []

    sum_part_2 = 0
    for line in lines: 
        line = line.replace("\n", "")

        game = line.split(": ")[0].split(" ")[1]
    
        #For part 2
        min_values_valled_game ={'red' : 0, 'blue' : 0, 'green' : 0} 
        
        hands_in_game = line.split(": ")[1].split("; ")
        for hand in hands_in_game: 
            
            colors_and_values = hand.split(", ")

            dict_hand = {color_and_value.split(' ')[1] :  int(color_and_value.split(' ')[0]) for color_and_value in colors_and_values} 
            for k in dict_hand.keys(): 

                #part 1
                if  dict_hand[k] > max_values_valled_game[k]:
                    if int(game) not in invalled_games: 
                        invalled_games.append(int(game))
            
                #part 2
                if dict_hand[k] >  min_values_valled_game[k]:
                    min_values_valled_game[k] = dict_hand[k]
        
        sum_part_2 += np.prod(list(min_values_valled_game.values()))
     

    sum_part_1 = sum(range(1,100)) - sum(invalled_games)
    print(f"Sum part 1 = {sum_part_1}")
    print(f"Sum part 2 = {sum_part_2}")

if __name__ == "__main__":
    main()
