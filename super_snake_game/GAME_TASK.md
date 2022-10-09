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

# Part 4

Code refactoring

## Task 1

Introduce a new function called `restart_level` that will recreate all turtle objects, clear entire canvas and setup everything again from scratch.
Each spawn function should return new turtle object instead of relying on a global variable outside of function scope. For example:

Instead:
```python
head = turtle.Turtle()
def spawn_snake(shape:str, color:str, x:int, y:int):
    head.speed(0)
    head.shape(shape)
    head.color(color)
    head.penup()
    head.goto(x,y)
    head.direction = "stop"
```

Use:
```python
def spawn_snake(shape:str, color:str, x:int, y:int):
    head = turtle.Turtle()
    head.speed(0)
    head.shape(shape)
    head.color(color)
    head.penup()
    head.goto(x,y)
    head.direction = "stop"
    return head

head = spawn_snake("square", "white", 0, 0)
```

## Task 2

Remove `magic` variables. Create a constant variable for each hardcoded string or integer value. For example:

Instead
```python
time.sleep(1.5)
```

Use
```python
SLEEP_TIME = 1.5

time.sleep(SLEEP_TIME)
```

> HINT: constant variables should be all UPPERCASE_WITH_UNDERSCORES

## Task 3

Refactor controls setup. Create a dedicated function that takes turtle object as an input and configures the keypress events instead of invoking it globally.
