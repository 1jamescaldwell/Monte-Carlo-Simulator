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

## Comprehensive overview of each class

### Die class
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

FILE
    /sfs/gpfs/tardis/home/ywe4kw/Documents/MSDS/DS5100/Monte_Carlo_Simulator/Monte-Carlo-Simulator/MC_Package/die.py

