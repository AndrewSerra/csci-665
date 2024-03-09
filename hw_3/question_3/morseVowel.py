__author__ = "Andrew Serra"
'''


Author: Andrew Serra
Date: 02/27/2024
'''

def count_possible_vowels(symbols):
    '''
    
    '''
    vowels = [".", ".-", "..", "..-", "---"]
    dp = [0] * (len(symbols)+1)
    dp[0] = 1

    if len(symbols) <= 1:
        return len(symbols)

    for i in range(len(symbols)):
        for v in vowels:
            len_v = len(v)

            if len_v <= (len(symbols) - i):
                dp[i+len_v] += dp[i] if symbols[i:i+len_v] == v else 0

    return dp[-1]

if __name__ == "__main__":
    try:
        num_items = int(input().strip())
        symbols = input().strip()
        print(count_possible_vowels(symbols))

    except Exception as e:
        print(f"Error running code: {e}")
