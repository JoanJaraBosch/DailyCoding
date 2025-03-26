def longest_substring_k_distinct(s, k):
    if k == 0 or not s:
        return 0

    char_count = {}  # Dictionary to store frequency of characters
    left, max_length = 0, 0

    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1

        # If more than k distinct characters, shrink from left
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1  # Shrink window

        # Update max length of valid substring
        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    # Example Usage:
    print(longest_substring_k_distinct("abcba", 2))  # Output: 3 ("bcb")
    print(longest_substring_k_distinct("aabbcc", 2)) # Output: 4 ("aabb")
    print(longest_substring_k_distinct("aaaabvbbbbbbb", 1))   # Output: 7 ("bbbbbbb")
    print(longest_substring_k_distinct("abcdef", 3)) # Output: 3 ("abc", "bcd", etc.)