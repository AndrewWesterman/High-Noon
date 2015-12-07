Author info:
    Andrew Westerman
    awesterman@csu.fullerton.edu
    CS 386: Final Project

Intro:
    This is a game called High Noon. It is a 2 player 2D arena shooter
    based upon old west duels.

External reqs:
    - The host computer must have pygame installed locally.
    - The game was written written in python 3.4 so the version of pygame must be compatible with 3.4
    - A linux machine or MAC capable of executing from the terminal

Setup and Install:
    - Extract the contents of the zip file to a location on your machine
    - Navigate to the folder
    - In the terminal type:
      $python3.4 main.py

Rules:
    - Each player must attempt to expend all 3 of their opponent's lives before their opponent does the same
    - The controls are left, right, jump, shoot
        - For p1 that is A, D, W, space
        - For p2 that is Left, Right, Up, Numpad_Enter

Features:
    - 2 player simultaneous play
    - Dynamic hit and bullet collision detection

Bugs:
    - At the time of this writing powerups, bullet firing limitation and background art have yet to be implemented.
    - For an unkown reason the game will randomly animate bullets that shoot across the level, they do not collide with either player it appears so the only issue is appearance and distracting the players.
    