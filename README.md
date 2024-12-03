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
 from MC_Package.die import Die <br>
    To create a simple coin: my_die_faces = np.array(['H','T']), my_coin1 = Die(my_die_faces)
 from MC_Package.game import Game <br>
    To flip a coin 50 times: my_game1 = Game([my_die_faces]), my_game1.play(1000)
 from MC_Package.analyzer import Analyzer <br>
    To determine the number of jackpots: my_analyzer = Analyzer(my_game1), print(my_analyzer.check_jackpot())
