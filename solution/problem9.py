def max_non_adjacent_sum(nums):
    if not nums:
        return 0  # No elements

    include, exclude = 0, 0  # Initialize sums

    for num in nums:
        new_include = exclude + num  # Include current number
        new_exclude = max(include, exclude)  # Skip current number
        include, exclude = new_include, new_exclude  # Update states

    return max(include, exclude)

if __name__ == "__main__":
    print(max_non_adjacent_sum([2, 4, 6, 2, 5]))  # Output: 13
    print(max_non_adjacent_sum([5, 1, 1, 5]))    # Output: 10
    print(max_non_adjacent_sum([-1, -2, -3]))    # Output: 0  (Avoid negatives)