Chapter 6 
    - The 'random' module helps us generate pseudorandom numbers, using a program that decides what number    to pick next.
    >>> import random
    >>> random.randint(1, 10) 

    - The 'random.choice()' function returns a randomly selected element from any list or collection.

    - The 'window_width()' function tells us how wide is our turtle screen, in pixels.

    - The 'window_height()' function tells us how tall is our turtle screen, in pixels.

    - The origin ( X:0, Y:0 ) is at the center of our screen.

    How to generate a random (x, y) location on the screen:
        x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)  
        y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)