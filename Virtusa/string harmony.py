def kk(inp1):
    n = len(inp1)
    ans = 0

    for start in range(n):
        pos = start
        curr_len = 0
        block_len = 2

        while True:
            expected = ""
            for i in range(block_len):
                expected += chr(ord('a') + i)

            if pos + block_len <= n and inp1[pos:pos + block_len] == expected:
                curr_len += block_len
                ans = max(ans, curr_len)
                pos += block_len
                block_len += 1
            else:
                break

    return ans


inp1 = "ababcabcd"
print(kk(inp1))
