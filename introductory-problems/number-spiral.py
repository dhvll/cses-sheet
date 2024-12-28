def spiral(y, x):

    maxi = max(x, y)


    square = (maxi - 1) * (maxi - 1)

    if maxi % 2 == 0:
        if x > y:
            return square + y
        else:
            return (maxi * maxi) - x + 1
    else:
        if x > y:
            return (maxi * maxi) - y + 1
        else:
            return square + x


n = int(input())
for _ in range(n):
    y, x = map(int, input().split())
    print(spiral(y,x))


# Input:
# 3
# 2 3
# 1 1
# 4 2

# Output:
# 8
# 1
# 15

# Time Complexity: O(n)
# Space Complexity: O(1)