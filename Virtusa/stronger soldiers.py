 def stronger(n, arr):
    count = 0

    for i in range(n):
        left = sum(1 for j in range(i) if arr[j] > arr[i])
        right = sum(1 for j in range(i + 1, n) if arr[j] > arr[i])

        if left > right:
            count += 1

    return count

print(stronger(5, [4, 3, 5, 2, 1]))
