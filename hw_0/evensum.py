# Problem 2 - Even Sum

if __name__ == "__main__":

    try:
        total = 0
        num_count = int(input())

        for i in range(num_count):
            num = int(input())
            if num % 2 == 0:
                total += num

        print(total)
            
    except ValueError:
        print("Input not an integer.")
