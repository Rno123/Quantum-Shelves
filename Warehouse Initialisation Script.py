number_of_layers = 2

import string
import pandas as pd
alphabets_list = list(string.ascii_lowercase)

# Number of Units is actually 8, Number of Sides is actually 2, Number of Levels is actually 3 but they are +1 because we start counting from 1
number_of_units = 9
number_of_sides = 3
number_of_levels = 4

# Unit, Side and Level Counters start from 1 so the string will start with 1
layer_counter = 0
unit_counter = 1
side_counter = 1
level_counter = 1
final_list = []

while layer_counter != number_of_layers:
    while side_counter != number_of_sides:
        while level_counter != number_of_levels:
            while unit_counter != number_of_units:
                spot = str(alphabets_list[layer_counter]) + str(side_counter) + '-' + str(level_counter) + '-' + str(unit_counter)
                final_list.append(spot)
                unit_counter += 1
            level_counter += 1
            unit_counter = 1
        side_counter += 1
        level_counter = 1
    layer_counter += 1
    side_counter = 1
    number_of_units = number_of_units + 8
    
package_list = [None] * len(final_list)

final_df = pd.DataFrame({'Spot':final_list,
                       'Package':package_list})

final_df.to_csv(r'C:\Users\Arnold\Desktop\Dyson Scripts\In Out CSV\Warehouse State.csv',index=False)


 
