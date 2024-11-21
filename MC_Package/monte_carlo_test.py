import unittest
import numpy as np
import pandas as pd
from die import Die
from game import Game
from analyzer import Analyzer

class MonteCarloTestSuite(unittest.TestCase):
    '''This is the test suite for die.py, game.py, and analyzer.py.
    Each method is named for the class method that it tests. Example: die.py's "change_weights" test is called test_change_weights.'''

    def setUp(self):
        '''Correctly setup die, game, and analyzer classes are created here to be used throughout testing'''

        # for die testing
        my_die_faces = np.array([1,2,3,4,5,6])
        self.my_die1 = Die(my_die_faces)
        self.my_die2 = Die(my_die_faces)
        self.my_die3 = Die(my_die_faces)
        # for game testing
        my_die_list = [self.my_die2,self.my_die3]    
        self.my_game = Game(my_die_list)
        # for analyzer testing
        self.my_game.play(100)
        self.my_analyzer = Analyzer(self.my_game)

    ####### die.py methods
    def test_die_init(self):
        '''Checks dataframe output and expected errors'''
        # 1 Check that a dataframe is created when a die is correctly created
        self.assertTrue(isinstance(self.my_die1.die_df, pd.DataFrame))
        # 2 Check that TypeError is raised when an array is not passed
        my_die_not_an_array = ['I"m not an array']
        with self.assertRaises(TypeError):
            Die(my_die_not_an_array)
        # 3 Check error if faces aren't unique
        my_die_not_unique_faces = np.array([1,2,1])
        with self.assertRaises(ValueError):
            Die(my_die_not_unique_faces)
    
    def test_change_weights(self):
        '''Checks that weights can be changed correctly and checks expected errors for incorrect input'''
        # 1 Check that change weights correctly changes to 10
        self.my_die1.change_weights(1,10)
        die_df = self.my_die1.show_current_state()
        self.assertEqual(die_df['weights'][1],10)
        # 2 Check indexerror
        with self.assertRaises(IndexError):
            Die(self.my_die1.change_weights(7,2)) # 7 is not an index of this die
        # 3 Check TypeError
        with self.assertRaises(TypeError):
            Die(self.my_die1.change_weights(1,'not a number')) 
        
    def test_roll_die(self):
        '''Checks that the die are rolled the correct number of times when played'''
        # Check that the number of rolls is correct
        num_rolls = 50
        self.assertEqual(len(self.my_die1.roll_die(num_rolls)),50)

    def test_show_current_state(self):
        '''Checks that the show current state returns a dataframe as expected'''
        self.assertTrue(isinstance(self.my_die1.show_current_state(), pd.DataFrame))
    
    ####### game.py methods
    def test_game_init(self):
        # Check if created die set is a game object
        self.assertTrue(isinstance(self.my_game, Game))
    
    def test_play(self):
        # Check that the game results is a 5 x 2, 5 rolls of 2 dice
        self.my_game.play(5)
        self.assertEqual(self.my_game.game_results_df.shape,(5,2))

    def test_show_results(self):
        # Play the game first
        self.my_game.play(5)
        # 1 Check value error
        with self.assertRaises(ValueError):
            self.my_game.show_results('This should throw an error since it is not "narrow" or "wide"')
        # 2 Check wide format is returned automatically
        self.assertEqual(self.my_game.show_results().shape, (5,2))
        # 3 Check narrow format is returned if requested
        self.assertEqual(self.my_game.show_results('narrow').shape, (10,3))

    ####### analyzer.py methods
    def test_analyzer_init(self):
        # 1 Check if created die set is a analyzer object
        self.assertTrue(isinstance(self.my_analyzer, Analyzer))
        # 2 Check ValueError if not a game object is passed
        with self.assertRaises(ValueError):
            Analyzer('I"m not a game object')
    
    def test_check_jackpot(self):
        # 1 Check that the jackpot output is an integer
        jackpot_output = self.my_analyzer.check_jackpot()
        self.assertTrue(isinstance(jackpot_output,np.int64))
        # 2 Check that the output count is between 0 and the number of plays (in this case 100)
        self.assertTrue(0 <= jackpot_output < 100)

    def test_face_counts(self):
        # Check that the shape of the return is # rolls x # faces (in this case, 100 rolls x 6 faces)
        self.assertTrue(self.my_analyzer.face_counts().shape, (100,6))
        # Check that the output is a dataframe
        self.assertTrue(isinstance(self.my_analyzer.face_counts(), pd.DataFrame))

    def test_combo_count(self):
        # Check that the shape of the return is # rolls x (faces totals + counts of that instance) (in this case, 100 rolls x 7 columns)
        self.assertTrue(self.my_analyzer.face_counts().shape, (100,7))
        # Check that the output is a dataframe
        self.assertTrue(isinstance(self.my_analyzer.face_counts(), pd.DataFrame))

    def test_permutation_count(self):
        # Check that the shape of the return is # rolls x (faces totals + counts of that instance) (in this case, 100 rolls x 7 columns)
        self.assertTrue(self.my_analyzer.face_counts().shape, (100,7))
        # Check that the output is a dataframe
        self.assertTrue(isinstance(self.my_analyzer.face_counts(), pd.DataFrame))

if __name__ == '__main__':
    unittest.main(verbosity=3)

    # python monte_carlo_test.py 2> monte_carlo_results.txt 