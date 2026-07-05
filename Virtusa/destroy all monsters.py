import math
def destroyAllMonsters(input1, input2):
    def solve(arr):
        n = len(arr)
        if n <= 1:
            return 0
        mid = n // 2
        ans = float('inf')
        if 0 != mid:
            new_arr = arr[:]
            cost = math.gcd(new_arr[0], new_arr[mid])
            new_arr.pop(mid)
            new_arr.pop(0)
            ans = min(ans, cost + solve(new_arr)
        if mid != n - 1:
            new_arr = arr[:]
            cost = math.gcd(new_arr[mid], new_arr[-1])
            new_arr.pop(n - 1)
            new_arr.pop(mid)
            ans = min(ans, cost + solve(new_arr)
        if n > 1:
            new_arr = arr[:]
            cost = math.gcd(new_arr[0], new_arr[-1])
            new_arr.pop(n - 1)
            new_arr.pop(0)
            ans = min(ans, cost + solve(new_arr)
        return ans
    return solve(input2)
print(destroyAllMonsters(4, [1, 2, 3, 4]))
