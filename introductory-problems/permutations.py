def solve(n):
    if n == 1:
        return [1]
    if n <= 3:
        return None

    result = []
    for i in range(2, n + 1, 2):
        result.append(i)

    for i in range(1, n + 1, 2):
        result.append(i)

    return result

n = int(input())
result = solve(n)
if result is None:
    print("NO SOLUTION")
else:
    print(" ".join(map(str, result)))
# Time Complexity: O(n)
# Space Complexity: O(n)