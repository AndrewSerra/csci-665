__author__="Andrew Serra"


def does_half_snowfall_exist(snowfall: list[int]) -> str:
    '''
    Determines if there is a three day period where half
    of the total snow has fallen.

    @param snowfall A list containing the cumulative snowfalls
                    for each day
    
    @returns "YES" if there is a period, "NO" if not
    '''
    target_level = snowfall[-1] // 2
    
    snowfall[-1] -= snowfall[-2]
    snowfall[-2] -= snowfall[-3]

    for i in range(len(snowfall)-3, 0, -1):
        snowfall[i] -= snowfall[i-1]
        
        if (snowfall[i] + snowfall[i+1] + snowfall[i+2]) > target_level:
            return "YES"

    return "NO"

def get_processed_snowfall(data: str) -> list[int]:
    '''
    Processes the input read from stdin.

    @params data A string containing the input of the cumulative
                 snowfall in one line.

    @returns A list of integers that contain the cumulative snowfall 
    '''
    return list(map(lambda x: int(x), data.strip().split(" ")))

if __name__ == "__main__":
    # Number of days of snowfall
    n = int(input())
    # Cumulative days of snowfall
    data = input()

    cumulative_snowfall = get_processed_snowfall(data)

    print(does_half_snowfall_exist(cumulative_snowfall))
