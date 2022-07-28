Chapter 5:
    What you'll learn
    - Use 'if' statements to make decisions using conditionals.
    - Use conditionals and Boolean expressions to control program flow.
    - Describe how a Boolean expression evaluates to 'True' of 'False'.
    - Write condiotional expressions using comparison operators (<, >, ==, !=, <=, >=).
    - Use if-else statement combinations to choose between two alternative program paths.
    - Test a variable to see if it is odd or even using the modulo operator, %.
    - Write if-elif-else statements that select from among a number of options.
    - Use 'and' and 'or' to test multiple conditions at once. 
    - Use the 'not' operator to check whether a value or variable is 'False'.
    - Explain how letters and other characters are stored as numeric values in computers.
    - Use 'ord()' and 'chr()' to convert characters into their ASCII equivalents and vice versa.
    - Manipulate strings using various string functions like 'lower()', 'upper()', and 'isupper()'.
    - Add strings and characters together using the + operator.

    The 'if' statement allows us o tell the computer 'whether' to run a set of statements based on a condition.
        if (condition):
            (indented statement(s))

    Boolean expressions allow programs to make decisions based on a condition.

    Conditional expressions evaluate to 'True' or 'False'
        expressiona1 (conditional_operator) expression2 
        answer == 'y'

    Comparison operators:

    |    Python operator   |          Meaning             |      Example     |      Result       |
    |                      |                              |                  |                   |
    |          <           |         Less than            |      1 < 2       |       True        |      
    |          >           |        Greater than          |      1 > 2       |       False       |  
    |         <=           |    Less than or equal to     |      1 <= 2      |       True        |   
    |         >=           |   Greater than ot equal to   |      1 >= 2      |       False       |  
    |         ==           |        Is eqaul to           |      1 == 2      |       False       | 
    |         !=           |        Not equal to          |      1 != 2      |       True        |        
    
    Even or odd:

        if (m % 2 == 0): (Tests if 'm' is even.)
        else: (Otherwise, 'm' must be odd.)


    Complex operators:

    |    Logical operator      |                 Usage                   |                               Result                                       |      
    |                          |                                         |                                                                            |
    |          and             |      if(condition1 and condition2):     |       True only if BOTH 'condition1' and 'condition2' are 'True'           |      
    |          or              |      if(condition1 or condition2):      |       True if either of 'condition1' or 'condition2' are 'True'            |      
    |          not             |           if not (condition):           |                  True only if the 'condition' is 'False'                   |

    Secret messages:
        - The Caesar cipher is a 2,000-year-old secret code that shifts letters in 13 letters in the alphabet to send private messages.( A ---> N, B ---> O)
        Example: SECRET MESSAGES ARE COOL ---> FRPERG ZRFFNTRF NER PBBY

    How to make strings with upper or lower cases?
        >>> 'Hello'.upper()
        HELLO
        >>> 'Hello'.lower()
        hello
    
    Numeric values of charaters in Python
        - The Python function to turn a character into ASCII number is 'ord()'
        >>> ord('A')
        65
        >>> chr(65)
        'A'
        