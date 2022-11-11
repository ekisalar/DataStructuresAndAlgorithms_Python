# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined

# Brute force

class FirstRecurringItem:
    def by_brute_force(self, array):
        recurring_indexes = []
        i = 0
        j = 1
        while i < len(array):
            while j < len(array):
                if array[i] == array[j]:
                    recurring_indexes.append(j)
                j += 1
            i += 1
            j = i + 1
        if len(recurring_indexes) > 0:
            return array[min(recurring_indexes)]
        else:
            return "No recurring item"

    def by_hash_table(self, array):
        hash_table = {}
        for i, item in enumerate(array):
            if item in hash_table:
                return item
            hash_table[item] = i
        return None
