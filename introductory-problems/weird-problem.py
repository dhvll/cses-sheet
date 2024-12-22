def weird_algorithm(n):
    result = []
 
    while n != 1:
        result.append(n)
 
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
 
    result.append(1)
    return result
 
def main():
 
    try:
        n = int(input())
        sequence = weird_algorithm(n)
        print(*sequence)
    except ValueError:
        print("Please enter a valid integer.")
 
if __name__ == "__main__":
    main()

# Time complexity: O(log(n))
# Space complexity: O(log(n))