import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    data_location = Path("./data/Day_04.txt")

    with open(data_location, "r") as f:
        lines = f.readlines()

    sum_part_1 = 0
    number_of_carts =  {int(k): [] for k in range(1,len(lines)+1)}
    for line in lines:  
        line.strip()

        card_nr = int(line.split(": ")[0].split(" ")[-1])
        win_numbers = line.split(": ")[1].split(" | ")[0].split(" ")
        my_numbers =  line.split(": ")[1].split(" | ")[1].split(" ")

        #Part 1
        intersection = [a for a in list(set(win_numbers) & set(my_numbers)) if a !=""]
        if len(intersection)>0:
            sum_part_1 += 2**(len(intersection)-1)

        #Part 2
        for copies in range(card_nr+1,card_nr+len(intersection)+1):
            number_of_carts[copies].append(card_nr)

            for already_copied in number_of_carts[card_nr]:
                 number_of_carts[copies].append(already_copied)

    sum_part_2 = len(lines) + sum([len(a) for a in number_of_carts.values()])

    print(f"Sum part 1 = {sum_part_1}")
    print(f"Sum part 2 = {sum_part_2}")

if __name__ == "__main__":
    main()