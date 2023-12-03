import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import more_itertools as mit

def get_index_locations(lines):
    index_digets = []
    index_sign = []

    index_star_sign = []
    for line in lines: 
        
        index_digets_line = []
        index_sign_line = []
        index_star_sign_line = []
        for i in range(len(line)):

            #Part 1 
            if line[i].isdigit():
                index_digets_line.append(i)
            elif line[i] not in ["." ," ", "","  ","\n"]:
                index_sign_line.append(i)

            #Part 2
            if line[i] == "*":
                index_star_sign_line.append(i)

        index_digets_line_grouped = [list(group) for group in mit.consecutive_groups(index_digets_line)]
        index_digets.append(index_digets_line_grouped) 
        index_sign.append(index_sign_line) 
        index_star_sign.append(index_star_sign_line)

    return index_digets, index_sign, index_star_sign

def find_adjecent_numbers(index_in_row,row,index_digets,found_adjecent):
    for target_element in index_in_row: 
            target_element_index = [[i, e.index(target_element)] for i, e in enumerate(index_digets[row]) if target_element in e]
            if len(target_element_index) > 0:
                    found_adjecent.append([row,target_element_index[0][0]]) 
    return found_adjecent 

def get_real_number(number_indexes,lines,row):
    #get realnumber
    real_number = ""
    for ind in number_indexes: 
        real_number += lines[row][ind]
    return real_number

def main():
    data_location = Path(".\data\Day_03.txt")
    with open(data_location, "r") as f:
        lines = f.readlines()

    #get index locations for digets, signs and star sign
    index_digets, index_sign, index_star_sign = get_index_locations(lines)

    #Part 1
    saved_number_indexes = []
    saved_real_number = []
    for row in range(len(index_digets)):
        for number_indexes in index_digets[row]: 
            index_in_same_row = [number_indexes[0]-1,number_indexes[-1]+1]
            index_in_row_above_or_below = [number_indexes[0]-1]+number_indexes+[number_indexes[-1]+1]

            checked_same_row = []
            checked_row_above =  []
            checked_row_below =  []
            if row == 0: 
                checked_same_row = list(set(index_in_same_row) & set(index_sign[row]))
                checked_row_below =  list(set(index_in_row_above_or_below) & set(index_sign[row+1]))
            elif row == len(index_digets)-1:
                checked_same_row = list(set(index_in_same_row) & set(index_sign[row]))
                checked_row_above =  list(set(index_in_row_above_or_below) & set(index_sign[row-1]))
            else:
                checked_same_row = list(set(index_in_same_row) & set(index_sign[row]))
                checked_row_above =  list(set(index_in_row_above_or_below) & set(index_sign[row-1]))
                checked_row_below =  list(set(index_in_row_above_or_below) & set(index_sign[row+1]))

            number_adjecent_found = (len(checked_same_row) +  len(checked_row_above) + len(checked_row_below))
            if number_adjecent_found >= 1: 
                saved_number_indexes.append(number_indexes)
                saved_real_number.append(int(get_real_number(number_indexes,lines,row)))
    #Part 2
    saved_real_number_part_2 = []
    for row in range(len(index_star_sign)):
        for star_index in index_star_sign[row]: 
            index_in_same_row = [star_index-1,star_index+1]
            index_in_row_above_or_below = [star_index-1,star_index,star_index+1]
            found_adjecent = []
            if row == 0: 
                found_adjecent = find_adjecent_numbers(index_in_same_row,row,index_digets,found_adjecent)
                found_adjecent = find_adjecent_numbers(index_in_row_above_or_below,row+1,index_digets,found_adjecent)
                
            elif row == len(index_digets)-1:
                found_adjecent = find_adjecent_numbers(index_in_same_row,row,index_digets,found_adjecent)
                found_adjecent = find_adjecent_numbers(index_in_row_above_or_below,row-1,index_digets,found_adjecent)

            else:
                found_adjecent = find_adjecent_numbers(index_in_same_row,row,index_digets,found_adjecent)
                found_adjecent = find_adjecent_numbers(index_in_row_above_or_below,row-1,index_digets,found_adjecent)
                found_adjecent = find_adjecent_numbers(index_in_row_above_or_below,row+1,index_digets,found_adjecent)
                  
            found_adjecent = list(set(tuple(sub) for sub in found_adjecent))
            if len(found_adjecent) >= 2: 
                product = 1
                for found in  found_adjecent:
                     roww,indd = found
                     product = product * int(get_real_number(index_digets[roww][indd],lines,roww))
                saved_real_number_part_2.append(product)
                
    print(f'Sum for part 1: = {sum(saved_real_number)}')
    print(f'Sum for part 2: = {sum(saved_real_number_part_2)}')
        
if __name__ == '__main__':
    main()