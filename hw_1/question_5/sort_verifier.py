from typing import Any

def is_sorted(data: list[Any]) -> bool:

    for i in range(1, len(data)):
        if data[i-1] > data[i]:
            return False
        
    return True
