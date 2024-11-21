import pandas as pd
import numpy as np

class Die():
    ''' This is the class that sets up the attributes for a die. A die has N sides, or faces, and a weight for each face. By default, the weights for each face are equal.'''

    def __init__(self, faces_array):
        '''Sets up a die given an array of faces, such as [1, 2, 3, 4, 5, 6] for a 6-sided die.
        Raises errors if an array is not passed as input or if each face of the die is unique'''
        # Check that the faces is passed as an array
        if not isinstance(faces_array, np.ndarray):
            raise TypeError("Die faces must be an array!")
        # Check that each face of the die is unique
            # length of array = length of array unique list
        if not (len(np.unique(faces_array))) == len(faces_array):
            raise ValueError('Faces of die must be unique!')
        
        # Generate a fair dice by default
        weights = np.ones(len(faces_array))

        # Initialize df with faces as index, weights as column
        self.die_df = pd.DataFrame(columns = ['weights'], index=faces_array, data = weights)

    def change_weights(self,face_value,new_weight):
        '''Allows the user to adjust the weights of a die manually. 
        Expects input for the face to be changed and the new weight.
        Throws an index error if the face trying to be changed to does not exist in the die.
        Also throws an error if the new weight is not a numeric.'''
        # Ensure face index exists
        if not face_value in self.die_df.index:
            raise IndexError("The face weight that you are trying to change does not exist!")
        # Ensure new weight is a numeric or castable to a numeric
        try:
            float(new_weight)
        except:
            raise TypeError('New weight is not a numeric')

        # Assign new weight to index=face_value
        self.die_df.loc[face_value,'weights'] = new_weight

    def roll_die(self,num_rolls=1):
        '''Allows the user to roll a die the specified number of times. 
         The method is a random sample with replacement, from the private die data frame, that applies the weights.
         Results are returned as a dataframe.'''
        die_faces = self.die_df.index
        
        # The weights for np.random.choice (variable "p") need to sum to 1. Calculate the relative weights here:
        faces_probability = (self.die_df['weights'] / sum(self.die_df['weights'])).to_list()

        self.roll_result = np.random.choice(die_faces, size=num_rolls, replace=True, p=faces_probability) # replace=True for sample with replacement
        
        return self.roll_result

    def show_current_state(self):
        '''Returns a copy of the die dataframe, which shows the faces and weights for the given die.'''
        return self.die_df
