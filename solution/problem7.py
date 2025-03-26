def num_decodings(s):
    if not s or s[0] == '0':
        return 0  # Invalid input
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # Base cases

    for i in range(2, n + 1):
        one_digit = int(s[i-1])      # Last single digit
        two_digits = int(s[i-2:i])   # Last two digits

        if 1 <= one_digit <= 9:  # Valid single digit
            dp[i] += dp[i-1]

        if 10 <= two_digits <= 26:  # Valid two-digit number
            dp[i] += dp[i-2]

    return dp[n]

if __name__ == '__main__':
    # Example usage:
    print(num_decodings("111"))  # Output: 3
    print(num_decodings("226"))  # Output: 3 (BZ, VF, BBF)
    print(num_decodings("06"))   # Output: 0 (invalid)