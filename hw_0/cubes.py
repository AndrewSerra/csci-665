# Problem 1 - Cubes

if __name__ == "__main__":
    try:
        ceil = int(input())
        count = 0
        val = 0

        while val <= ceil:
            print(val)
            count += 1
            val = pow(count, 3)
        
    except ValueError:
        print("Input not an integer.")
