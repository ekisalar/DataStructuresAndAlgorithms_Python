def add_to_80(n: int) -> int:
    return n + 80


cache = {}


def memoized_add_to_80(n: int) -> int:
    if cache.get(n) is not None:
        print("cached value"),
        return cache[n]
    else:
        print("long time")
        cache[n] = add_to_80(5)
        return cache[n]


def memoized_add_to_80_closure():
    def add_to_80_closure(n: int) -> int:
        return n + 80

    cache_closure = {}

    def closure_function(n: int) -> int:
        if cache_closure.get(n) is not None:
            print("cached value"),
            return cache_closure[n]
        else:
            print("long time")
            cache_closure[n] = add_to_80_closure(5)
            return cache_closure[n]

    return closure_function
