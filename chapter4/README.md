Chapter 4:
    What you'll learn
    - Create your own loops to repeat a set of instructions a certain number of times.
    - Use the 'range()' function to generate lists of values to control your 'for' loops.
    - Create empty lists and add to lists using the 'append()' function.
    - Create your own 'while' loops to repeat while the condition is True.
    - Explain how each type of loop works and how you code it in Python.
    - Give examples of situations in which you would use each type of loop.
    - Design and modify programs that use nested loops.

    A 'for' loop in Python iterates over, or repeats, a list of numbers:
    1 through 100, or 0 through 3 (right).

    The 'range()' function helps us generate a series of numbers easily - perfect for a 'for' loop.

    In a game loop, we don't know how many times the user might want to keep playing.
    We use the 'while' loop to test for a condition.
        while (condition):
            (intented statement(s))

    You can set up an empty list with square brackets:
        family = []
    You can append, or add, elements to a list with the 'append()' function:
        family.append("Dad")

    You can check the length of a list with the 'len()' function:
        len(family)

    A nested loop is a loop inside another loop:
        for x in range(10):
            for y range(10):