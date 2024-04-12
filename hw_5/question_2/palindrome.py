'''
Author: Andrew Serra
Date: 04/09/2024
'''

def dist_to_palindrome(cc, ca, s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] if j - i > 1 else 0
            else:
                dp[i][j] = min(dp[i+1][j-1] + cc, dp[i+1][j] + ca, dp[i][j-1] + ca)

    return dp[0][-1]

if __name__ == "__main__":
    try:
        # the length of the input string
        n = int(input().strip())
        # the cost to change a character
        cc = int(input().strip())
        # the cost to add a character
        ca = int(input().strip())
        # input string
        s = input().strip()

        print(dist_to_palindrome(cc, ca, s))

    except ValueError as e:
        print(e)
