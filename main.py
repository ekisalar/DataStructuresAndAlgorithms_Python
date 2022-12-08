from memoization import *

lambda_test = lambda num: \
    num + 80000
print(lambda_test(5))

# print(memoized_add_to_80(5))
# print(memoized_add_to_80(5))
# print(memoized_add_to_80(5))


memoized = memoized_add_to_80_closure()

print(memoized(5))
print(memoized(5))
print(memoized(5))

