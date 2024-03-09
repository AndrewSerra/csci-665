__author__ = "Andrew Serra"
'''
A program that checks if a village will be flooded before
all cracks can be repaired.

Author: Andrew Serra
Date: 02/14/2024
'''
import heapq

def is_village_flooding(thresh: int, drain_rate: int, cracks: list[tuple[int,int]]):
    '''
    Check whether the village will flood. Prints FLOOD, the time, and the 
    flood level if the village cannot be saved. If it can be saved, the output
    is SAFE, and the maximum flood level througout the time.

    @param thres      Integer        Threshold of the flood where the village 
                                     would be flooded
    @param drain_rate Integer        The rate of drainage that is automatically done
    @param cracks     Tuple(int,int) Time stamps of newly formed cracks and their
                                     flow rate.
    '''
    curr_t, curr_idx = 0, 0
    heap = []
    current_flood, max_flood = 0, 0

    while curr_t <= cracks[-1][0]:
        heapq.heapify(heap)

        while curr_idx < len(cracks) and curr_t == cracks[curr_idx][0]:
            heapq.heappush(heap, cracks[curr_idx][1] * -1)
            curr_idx += 1

        if len(heap):
            heapq.heappop(heap)

        current_flood += abs(sum(heap)) - drain_rate
        heap = list(map(lambda x: x-1, heap))

        if current_flood < 0:
            current_flood = 0

        if current_flood > max_flood:
            max_flood = current_flood

        if current_flood >= thresh:
            print("FLOOD")
            print(curr_t)
            print(current_flood)
            return

        curr_t += 1

    print("SAFE")
    print(max_flood)

if __name__ == "__main__":
    try:
        num_cracks = int(input().strip())
        thresh = int(input().strip())
        drain_per_t = int(input().strip())
        cracks_per_t = []

        for _ in range(num_cracks):
            crack = tuple(map(lambda x: int(x), input().strip().split()))
            cracks_per_t.append(crack)

        is_village_flooding(thresh, drain_per_t, cracks_per_t)
    except ValueError as e:
        print(f"Error converting values to integers: {e}")

