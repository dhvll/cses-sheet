def solve(n, nums):
    total_sum = n * (n + 1) // 2
    missingNum = total_sum - sum(nums)
    return missingNum

def main():
 
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        test = solve(n, nums)
        print(test)
    except ValueError:
        print("Please enter a valid integer.")
 
if __name__ == "__main__":
    main()

# Time Complexity: O(n)
# Space Complexity: O(n)