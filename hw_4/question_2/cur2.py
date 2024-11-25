def maximum_exhibit_value(items, budget):
  n = len(items)
  dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
  seen_categories = set()  # Track seen categories

  for i in range(1, n + 1):
    cost, value, category = items[i - 1]
    for j in range(budget + 1):
      option1 = dp[i - 1][j]
      option2 = 0
      # Consider including the item if budget allows and category hasn't been used before OR
      # if including it provides a higher value than previously seen for the category
      if (j >= cost and category not in seen_categories) or \
         (j >= cost and value > dp[i - 1][j - cost]):
        option2 = value + dp[i - 1][j - cost]
        seen_categories.add(category)
      dp[i][j] = max(option1, option2)
      seen_categories.discard(category)  # Reset category check for next item

  return dp[n][budget]


if __name__ == "__main__":

    try:
        num_items = int(input().strip())
        budget = int(input().strip())
        items = []

        while len(items) < num_items:
            line = input().strip()
            item = tuple(map(lambda x: int(x), line.split()))

            items.append(item)

        soln = maximum_exhibit_value(items, budget)
        print(soln)

    except ValueError as e:
        print(e)
