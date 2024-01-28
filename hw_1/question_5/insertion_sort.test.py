import time
from data_generator import create_uniform_test_cases, create_gaussian_test_cases
from sort_verifier import is_sorted
from insertion_sort import insertion_sort


def print_test_info(length: int, data_dist: str):
    print(f"{data_dist.capitalize()} Test")
    print(f"n = {length}")


def merge_sort_test():
    uniform_data = create_uniform_test_cases()
    gaussian_data = create_gaussian_test_cases()

    for test_case in uniform_data:
        print_test_info(len(test_case), "uniform")
        
        t_start = time.time()
        sorted_tc = insertion_sort(test_case)
        elapsed = time.time() - t_start
        
        print(f"Successful: {is_sorted(sorted_tc)}")
        print(f"Time elapsed: {elapsed:5f} seconds\n")

    for test_case in gaussian_data:
        print_test_info(len(test_case), "gaussian")

        t_start = time.time()
        sorted_tc = insertion_sort(test_case)
        elapsed = time.time() - t_start
        
        print(f"Successful: {is_sorted(sorted_tc)}")
        print(f"Time elapsed: {elapsed:5f} seconds\n")


if __name__ == "__main__":
    merge_sort_test()
