from typing import Callable

def caching_fibonacci() -> Callable[[int], int]: # setting main function
    cache = {} # creating an empty dict

    def fibonacci(n: int) -> int: # closing function
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci (n - 2)
        return cache[n]
    return fibonacci
    
fib = caching_fibonacci() # extracting fibonacci function
# using the function to calculate Fibonacci numbers
print(fib(12))
print(fib(5))  
print(fib(10)) # with using cahing every next calculation is stored in memory (cache)
print(fib(20))     

