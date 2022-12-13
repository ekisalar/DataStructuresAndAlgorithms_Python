# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


class Solution1:
    pos = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3
    }

    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        i = 4
        while i <= n:
            self.pos[str(i)] = self.pos[str(i - 1)] + self.pos[str(i - 2)]
            i += 1
        return self.pos[str(n)]


class Solution2:

    def climbStairs(self, n: int) -> int:

        array = [0, 1, 2, 3]

        if n < 4:
            return n
        i = 4
        while i <= n:
            array.append(array[i - 1] + array[i - 2])
            i += 1
        return array[n]


solution1 = Solution1()
print(solution1.climbStairs(10))

solution2 = Solution2()
print(solution2.climbStairs(10))
