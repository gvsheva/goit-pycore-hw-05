from typing import MutableMapping


def caching_fibonacci(cache: MutableMapping[int, int] | None = None):
    if cache is None:
        cache = {}

    def fib(n: int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n not in cache:
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib
