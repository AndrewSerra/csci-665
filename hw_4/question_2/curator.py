__author__ = "Andrew Serra"
'''


Author: Andrew Serra
Date: 03/22/2024
'''
from dataclasses import dataclass

# Purchase items cost in total < B. 
# Restriction is to be able to buy one item from each category.
# Need O(nB) algorithm to determine the max value you 
# can bring to the exhibit
# n items to selsect from, one item per category

# input
# n items
# B budget 
# n lines -> each line is one item, contains 3 integers
    # cost value type

@dataclass
class Item:
    type: int
    value: int
    cost: int


def find_most_valuable_exhibit(budget, items):
    dp = [[0 for _ in range(budget+1)] for _ in range(len(items)+1)]

    print("Budget ", budget, " Num Items ", len(items))

    for i in range(1, len(items)+1):
        item = items[i-1]
        for b in range(1, budget+1):
            if b < item.cost:
                dp[i][b] = dp[i-1][b]
            else:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b-item.cost] + item.value)

    for i in range(len(items), -1, -1):
        for b in range(budget-1, -1, -1):
            

    print()
    for r in dp:
        for item in r:
            print(f"{item:5}", end=" ")
        print()


if __name__ == "__main__":

    try:
        num_items = int(input().strip())
        budget = int(input().strip())
        items = []

        while len(items) < num_items:
            line = input().strip()
            item = list(map(lambda x: int(x), line.split()))

            items.append(
                Item(
                    type=item[2], 
                    value=item[1], 
                    cost=item[0]))

        soln = find_most_valuable_exhibit(budget, items)
        print(soln)

    except ValueError as e:
        print(e)
