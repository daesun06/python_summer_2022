# Final homework for python course

Create a snake game using python turtle package.

For inspiration references here is a sample snake game below:

![Gif](https://media.geeksforgeeks.org/wp-content/uploads/20201111233237/snakegame.gif)

## What chapters can be used for reference?

All chapters, you should utilize variables (int, float, string, list, dict), if/else conditionals, for or while loops, functions, for bonus points utilize classes.

## Part 1

Create a function that initiates the level of fixed width (can be changed via input param):

```python
def create_level(width: int):
```

## Part 2

Create a simple moving square object that can be controlled with arrows (up, down, left, right). Clickin on an arrow should change the direction of the square, square should be moving with a certain speed (for example every 1 second square should move in the specified direction by its width)

# Part 3

## 3.1 Refactoring

Move level generation, snake generation, and food generation into dedicated functions. 

## 3.2 Collision detection

Snake needs to die when it hits the walls outside of the level visible boundary. Snake should auto respawn after N seconds.

## 3.3 Food respawn

When snake overlaps with the food square, square dissapears and appears at a new random position after N seconds (N can be arbitrary)