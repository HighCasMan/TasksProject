import sys

''' python task4.py input.txt '''


def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            nums = [int(line.strip()) for line in file]
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    result = min_moves_to_equal_elements(nums)
    print(result)
