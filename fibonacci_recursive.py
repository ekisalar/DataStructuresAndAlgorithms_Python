class Fibonacci:

    def fibonacci_iterative(self, n):
        array = [0, 1]
        for i in range(2, n + 1, +1):
            array.append(array[i - 2] + array[i - 1])
        return array

    counter = 0

    def fibonacci_recursive(self, n):  # O(2^n)
        self.counter += 1
        if n < 2:
            return n
        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    counter_closure_long_time = 0
    counter_closure_cache = 0
    cache = {}

    def fibonacci_recursive_closure(self):  # O(n)

        def __calculate_fibonacci(n):
            if self.cache.get(n) is not None:
                self.counter_closure_cache += 1
                return self.cache[n]
            else:
                self.counter_closure_long_time += 1
                if n < 2:
                    return n
                self.cache[n] = __calculate_fibonacci(n - 1) + __calculate_fibonacci(n - 2)
                return self.cache[n]

        return __calculate_fibonacci


# fib(1):1
# fib(2):1 -> fib(1):1
#          -> fib(0):0
# fib(3):2 -> fib(2):1 -> fib(1):1
#                    -> fib(0):0
#          -> fib(1):1
# fib(4):3 -> fib(3):2 -> fib(2):1 -> fib(1):1
#                                  -> fib(0):0
#                      -> fib(1):1
#          -> fib(2):1 -> fib(1):1
#                      -> fib(0):0


fibonacci = Fibonacci()

# result = fibonacci.fibonacci_iterative(35)
result2 = fibonacci.fibonacci_recursive(5)
process_count3 = fibonacci.fibonacci_recursive_closure()
result3 = process_count3(500)

# print('iterative_result', result)
print('recursive_result', result2)
print('recursive_counter', fibonacci.counter)
print('closure_result', result3)
print('closure_counter', fibonacci.counter_closure_long_time)
print('closure_counter_cache', fibonacci.counter_closure_cache)
