    #TASK

#   The Collatz sequence is as follows:
    - Start with some given integer n
    -if it is even, next number will be n divided by 2
    -If it is odd, multply it by 3 and add 1 to make the next number.
    - The sequence stops when it reaches 1

 According to the Collatz conjecture, it will alwasy reach 1. If that's true, you can construct a finite sequence following the aforementioned method for any given integer. 

 Write a function that takes in an integer n and returns the highest integer in the corresponding Collatz sequence. 

    Examples:

    max_collatz(10) -->  16
    #collatz sequence: 10, 5, 16, 8, 4, 2, 1

    max_collatz(32) --> 32
    #collatz sequence: 32, 16, 8, 4, 2, 1

    max_collatz(85) --> 256
    #collatz sequence: 85, 256, 128, 64, 32, 16, 8, 4, 2, 1

    #SOLUTION



    
