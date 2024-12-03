# Monte-Carlo-Simulator
Created by James Caldwell <br>
Fall 2024 <br>
Created for UVA DS5100 class, Programming for Data Science

## Overview
For this project, I wrote, tested (unittest), used, packaged, and published a Python module and accompanying files. The main idea of this project was to create a monte carlo simulator. This consisted of created several classes that could be used to create, play, and analyze games of coin tosses and dice. <br>

## Contents
This repo contains: <br>
 1. A python package for the monte carlo simulator. It contains a Die class, a Game class, an Analyzer class, and a unittest file. <br>
 2. A python notebook demonstrating the package's usage. <br>
 3. Setup and .txt files used for playing the monte carlo simulator. <br>

This project demonstrated understanding of OOP, packaging, data wrangling, and analysis using python.

## Usage
After downloading the package, install using: pip install -e . (or pip install MC_Package) <br>
To use the classes: <br>
1. from MC_Package.die import Die <br>
   a. To create a simple coin: my_die_faces = np.array(['H','T']), my_coin1 = Die(my_die_faces)
2. from MC_Package.game import Game <br>
   a. To flip a coin 50 times: my_game1 = Game([my_die_faces]), my_game1.play(50)
3. from MC_Package.analyzer import Analyzer <br>
   a. To determine the number of jackpots: my_analyzer = Analyzer(my_game1), print(my_analyzer.check_jackpot())

# Comprehensive overview of each class

## Die class
NAME
    MC_Package.die

CLASSES
    builtins.object
        Die
    
    class Die(builtins.object)
     |  Die(faces_array)
     |  
     |  This is the class that sets up the attributes for a die. A die has N sides, or faces, and a weight for each face. By default, the weights for each face are equal.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, faces_array)
     |      Sets up a die given an array of faces, such as [1, 2, 3, 4, 5, 6] for a 6-sided die.
     |      Raises errors if an array is not passed as input or if each face of the die is unique
     |  
     |  change_weights(self, face_value, new_weight)
     |      Allows the user to adjust the weights of a die manually. 
     |      Expects input for the face to be changed and the new weight.
     |      Throws an index error if the face trying to be changed to does not exist in the die.
     |      Also throws an error if the new weight is not a numeric.
     |  
     |  roll_die(self, num_rolls=1)
     |      Allows the user to roll a die the specified number of times. 
     |      The method is a random sample with replacement, from the private die data frame, that applies the weights.
     |      Results are returned as a dataframe.
     |  
     |  show_current_state(self)
     |      Returns a copy of the die dataframe, which shows the faces and weights for the given die.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

## Game Class
NAME
    MC_Package.game

CLASSES
    builtins.object
        Game
    
    class Game(builtins.object)
     |  Game(die_list)
     |  
     |  This is the class that sets up the attributes for a game. A game consists of rolling of one or more similar dice (Die objects)
     |  one or more times. Each game is initialized with a Python list that contains one or
     |  more dice.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, die_list)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  play(self, num_rolls)
     |      Rolls the set of die the specified number of times and stores the result of the rolls.
     |  
     |  show_results(self, format='wide')
     |      Returns the game results as a dataframe. An optional input is "wide" or "narrow" for the format of the dataframe. Defaults to "wide"
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)



   ## Analyzer Class
   NAME
    MC_Package.analyzer

DESCRIPTION
    # import numpy as np
    # import pandas as pd

CLASSES
    builtins.object
        Analyzer
    
    class Analyzer(builtins.object)
     |  Analyzer(game_object)
     |  
     |  This is the class that analyzes a die game. An Analyzer object takes the results of a single game and computes
     |  various descriptive statistical properties about it.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, game_object)
     |      Checks if a game object is passed and initializes the game object and results df to be used by the other methods.
     |  
     |  check_jackpot(self)
     |      Calculates the number of times a jackpot is scored.  A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die.
     |      If only one dice is rolled, all plays will be a jackpot.
     |  
     |  combo_count(self)
     |      This Computes the distinct combinations of faces rolled, along with their counts.
     |      This method starts with the face_counts_df created by the face_counts() method.
     |  
     |  face_counts(self)
     |      This method calculates how many instances of each face value there are per roll.
     |      Step 1. Automatically generate a list of the faces
     |      Step 2. Use game's method show_results() to calculate by row each face count
     |      Step 3. Save as a df (dropping unneeded columns) and return
     |  
     |  permutation_count(self)
     |      Computes the distinct permutations of faces rolled, along with their counts. 
     |      This method starts with the face_counts_df created by the face_counts() method.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
