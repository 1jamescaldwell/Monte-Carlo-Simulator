# import numpy as np
# import pandas as pd
# from die import Die
# from game import Game
# from MC_Package import Game
# from game import Game
from MC_Package.game import Game

class Analyzer():
    ''' This is the class that analyzes a die game. An Analyzer object takes the results of a single game and computes
various descriptive statistical properties about it.
'''

    def __init__(self,game_object):
        '''Checks if a game object is passed and initializes the game object and results df to be used by the other methods.'''
        # if not isinstance(game_object, Game):
        if not isinstance(game_object, Game):
            raise ValueError('Passed object is not a Game object.')
        else:
            self.game_object = game_object
            self.results_df = self.game_object.show_results() # Used this several times, so I calculated here to make things easier.
    
    def check_jackpot(self):
        '''Calculates the number of times a jackpot is scored.  A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die.
        If only one dice is rolled, all plays will be a jackpot.'''
        
        # Determine if all columns of each row are equal using .eq 
        jackpot_df = self.results_df.eq(self.results_df.iloc[:, 0], axis=0).all(1)
        jackpot_count = jackpot_df.sum() # add up the number of true values

        return jackpot_count
    
    def face_counts(self):
        '''This method calculates how many instances of each face value there are per roll.
        Step 1. Automatically generate a list of the faces
        Step 2. Use game's method show_results() to calculate by row each face count
        Step 3. Save as a df (dropping unneeded columns) and return'''

        # First, get the list of faces for the die
            # This assumes all the die have the same faces
        self.face_list = self.game_object.game_die[0].show_current_state().index.to_list() # eg. 1, 2, 3, 4, 5, 6 
        die_names = self.results_df.columns.to_list() # These column names will be removed later
        # Create dataframe with roll as index, columns as faces, and values as counts of the faces 
        face_counts_df = self.results_df
        for face in self.face_list:
            face_counts_here = self.results_df == face
            face_counts_df[face] = face_counts_here.sum(axis = 1)
        # Remove results_df column names (eg. Die 1, Die 2, etc)
        for die_name in die_names:
            face_counts_df.drop(die_name, axis=1, inplace=True)
        
        return face_counts_df
    
    def combo_count(self):
        '''This Computes the distinct combinations of faces rolled, along with their counts.
        This method starts with the face_counts_df created by the face_counts() method.'''

        face_counts_df = self.face_counts()
        combo_count_df = face_counts_df.groupby(self.face_list).size().reset_index(name='Counts')

        return combo_count_df
  
    def permutation_count(self):
        '''Computes the distinct permutations of faces rolled, along with their counts. 
        This method starts with the face_counts_df created by the face_counts() method.'''

        die_names = self.results_df.columns.to_list()
        permutation_count_df = self.results_df.groupby(die_names).size().reset_index(name='Counts')

        return permutation_count_df        
