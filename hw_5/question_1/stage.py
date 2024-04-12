'''
Author: Andrew Serra
Date: 04/09/2024
'''

def get_min_sum_of_diff(line1, line2):
    m, n = len(line1), len(line2)
    
    dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        dp[i][0][0] = dp[i-1][0][0] + abs(line1[i-1] - line1[i-2]) if i > 1 else 0
        
    for i in range(1, n + 1):
        dp[0][i][1] = dp[0][i-1][1] + abs(line2[i-1] - line2[i-2]) if i > 1 else 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j][0] = min(dp[i-1][j][0] + abs(line1[i-1] - line1[i-2]), 
                              dp[i-1][j][1] + abs(line1[i-1] - line2[j-1])) if i > 1 else dp[i-1][j][1] + abs(line1[i-1] - line2[j-1])
            dp[i][j][1] = min(dp[i][j-1][0] + abs(line2[j-1] - line1[i-1]), 
                              dp[i][j-1][1] + abs(line2[j-1] - line2[j-2])) if j > 1 else dp[i][j-1][0] + abs(line2[j-1] - line1[i-1])

    return min(dp[m][n][0], dp[m][n][1])

if __name__ == "__main__":
    try:
        # the length of the first line
        m = int(input().strip())
        # the length of the second line
        n = int(input().strip())

        heights_m = list(map(int, input().strip().split()))
        heights_n = list(map(int, input().strip().split()))

        print(get_min_sum_of_diff(heights_m, heights_n))

    except ValueError as e:
        print(e)
