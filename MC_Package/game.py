# from die import Die
# import die
import numpy as np
import pandas as pd

class Game():
    ''' This is the class that sets up the attributes for a game. A game consists of rolling of one or more similar dice (Die objects)
    one or more times. Each game is initialized with a Python list that contains one or
    more dice. '''

    def __init__(self,die_list):
        self.game_die = die_list
    
    def play(self,num_rolls):
        '''Rolls the set of die the specified number of times and stores the result of the rolls.'''
        game_results = {} # initialize dict to store each die's results in, with the die name/number as a key
        for index, die in enumerate(self.game_die):
            die_name = 'Die ' + str(index) # Create name for die to store as df header
            game_results[die_name] = die.roll_die(num_rolls) # roll each dice the desired number of times
        self.game_results_df = pd.DataFrame(game_results) # store results in a df
        self.game_results_df.index.name = "Roll Number" # set index name

    def show_results(self,format = 'wide'):
        '''Returns the game results as a dataframe. An optional input is "wide" or "narrow" for the format of the dataframe. Defaults to "wide"'''
        if format == 'wide':
            return self.game_results_df
        elif format == 'narrow':
            game_results_df_Narrow = pd.DataFrame.stack(self.game_results_df).reset_index()
            game_results_df_Narrow.rename(columns={game_results_df_Narrow.columns[1]: 'Die Name',game_results_df_Narrow.columns[2]: 'Result'}, inplace=True) 
            return game_results_df_Narrow
        else:
            raise ValueError('Must provide "narrow" or "wide" as input to show_results')