from first_recurring_item import FirstRecurringItem

firstRecurringItem = FirstRecurringItem()
# result1 = recurringItemInArray.by_brute_force([2, 5, 1, 2, 3, 5, 1, 2, 4])
# result2 = recurringItemInArray.by_brute_force([2, 1, 1, 2, 3, 5, 1, 2, 4])
# result3 = recurringItemInArray.by_brute_force([2, 3, 4, 5])
# print(result1, result2, result3)

result1 = firstRecurringItem.by_hash_table([2, 5, 1, 2, 3, 5, 1, 2, 4])
result2 = firstRecurringItem.by_hash_table([2, 1, 1, 2, 3, 5, 1, 2, 4])
result3 = firstRecurringItem.by_hash_table([2, 3, 4, 5])
print(result1, result2, result3)
