import time

# fib(n) = fib(n-1) + fib(n-2)
def fibonacci_recursion(n):
    global num_calls
    num_calls += 1

    if n == 1:
        return 0
    elif n == 2:
        return 1

    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


def fibonacci_recursion_cache(n, cache={}):
    global num_calls
    num_calls += 1

    if n in cache:
        return cache[n]

    if n == 1:
        return 0
    elif n == 2:
        return 1

    result = fibonacci_recursion_cache(n-1, cache) + fibonacci_recursion_cache(n-2, cache)
    cache[n] = result

    return result



start = time.time()
num_calls = 0
print('Recursion fib: ', fibonacci_recursion(30))
print('Num of calls: ', num_calls)
end = time.time()
print('Recursion: ', end-start)

print('\n*********\n')

start = time.time()
num_calls = 0
print('Recursion fib with cache: ', fibonacci_recursion_cache(990))
print('Num of calls with cache: ', num_calls)
end = time.time()
print('Recursion with cache: ', end-start)