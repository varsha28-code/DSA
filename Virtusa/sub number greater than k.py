def subNumberGreaterThanK(input1, input2):
    s = str(input1)
    k = input2
    ans = float('inf')
    def backtrack(i, curr):
        nonlocal ans
        if i == len(s):
            if curr != "":
                num = int(curr)
                if num > k:
                    ans = min(ans, num)
            return
        backtrack(i + 1, curr + s[i])
        backtrack(i + 1, curr)
    backtrack(0, "")
    return ans
print(subNumberGreaterThanK(123, 14))
