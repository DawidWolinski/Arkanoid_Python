# Arkanoid_Python
 
This is a clone of Arkanoid, an arcade game released in 1986 where the player uses a paddle to bounce the ball and break the bricks on the map. It was written using Python and Pygame library and it's a mini-version of my C++ project in whcih I recreated most of the original game.

I used a finite state machine design pattern to manage different states/scenes of the game. There are three states: Menu, Gameplay and GameOver. Depending on each state, the game behaves differently when it comes to event handling, updating and displaying objects.
The state machine I used is based on: https://gist.github.com/iminurnamez/8d51f5b40032f106a847

I struggled with handling different resolutions using Pygame, so I just 'hard coded' the object sizes (all textures are scaled by 3). That's why it runs only in one resolution - 672x768. 

The game doesn't run very smoothly because apparently Pygame doesn't have vsync unlike most modern frameworks. Hence why moving objects might be jittering a little.

Assets were taken from:
- Textures: https://www.spriters-resource.com/arcade/arkanoid/
- Font: https://www.dafont.com/arcade-ya.font

Run the main.py file to play the game.
