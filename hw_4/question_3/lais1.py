__author__ = "Andrew Serra"
'''


Author: Andrew Serra
Date: 03/22/2024
'''

# A sequence integers
# B sequence integers
# X alternating increasing sequence of A and B
#   odd index   -> subsequence of either A or B sequence
#   even index  -> subsequence of the other sequence

# O(mn) dp algorithm

def find_len_alternating_inc_seq(a, b):
    m, n = len(a)+1, len(b)+1
    dp = [[0, 0] for _ in range(max(len(a), len(b)))]

    

def conv_lst_to_int_lst(s):
    return list(map(lambda x: int(x), s.strip().split()))

if __name__ == "__main__":
    try:
        m = int(input().strip())
        n = int(input().strip())
        
        a = conv_lst_to_int_lst(input().strip())
        b = conv_lst_to_int_lst(input().strip())

        count = find_len_alternating_inc_seq(a, b)
        print(count)

    except ValueError as e:
        print(e)
