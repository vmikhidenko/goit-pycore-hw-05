import time
from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    # defining main function
    cache = {}

    def fibonacci(n: int) -> int:
        # defining closing function
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2) #calculation of fibonacci number
            return cache[n]

    return fibonacci

def nocaching_fibonacci() -> Callable[[int], int]:
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci

# Testing the functions
fib_cached = caching_fibonacci()
fib_not_cached = nocaching_fibonacci()

# Testing caching version
print("Testing caching version:")
begin = time.time()
print(fib_cached(10))
end = time.time()
print("Time taken to execute function with cache:", end - begin)

begin = time.time()
print(fib_cached(10))
end = time.time()
print("Time taken to execute function with cache (second run):", end - begin)

begin = time.time()
print(fib_cached(15))
end = time.time()
print("Time taken to execute function with cache:", end - begin)

begin = time.time()
print(fib_cached(15))
end = time.time()
print("Time taken to execute function with cache (second run):", end - begin)

# Testing non-caching version
print("\nTesting non-caching version:")
begin = time.time()
print(fib_not_cached(10))
end = time.time()
print("Time taken to execute function without cache:", end - begin)

begin = time.time()
print(fib_not_cached(10))
end = time.time()
print("Time taken to execute function without cache (second run):", end - begin)

begin = time.time()
print(fib_not_cached(15))
end = time.time()
print("Time taken to execute function without cache:", end - begin)

begin = time.time()
print(fib_not_cached(15))
end = time.time()
print("Time taken to execute function without cache (second run):", end - begin)
