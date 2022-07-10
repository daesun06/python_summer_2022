# This is not a programming challenge.

# First ask the user to enter a math problem.
problem = input("Please enter your math problem, or 'q' to quit: ")

# Then keep going until the user enters 'q' to quit.
while problem != "q":
    # Show the problem, and the answer using 'eval()'.
    print("The answer to ", problem, "is:", eval(problem))

    # Ask for another problem.
    problem = input("Please enter your math problem, or 'q' to quit: ")

    # This 'while' loop will keep going until you enter 'q' to quit.
