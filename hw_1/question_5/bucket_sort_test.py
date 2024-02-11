__author__="Andrew Serra"

import time
from utils.data_generator import create_uniform_test_cases, create_gaussian_test_cases
from utils.sort_verifier import is_sorted
from bucket_sort import bucket_sort


def print_test_info(length, data_dist):
    print(f"{data_dist.capitalize()} Test")
    print(f"n = {length}")


def bucket_sort_test():
    uniform_data = create_uniform_test_cases()
    gaussian_data = create_gaussian_test_cases()

    for test_case in uniform_data:
        print_test_info(len(test_case), "uniform")
        
        t_start = time.time()
        sorted_tc = bucket_sort(test_case)
        elapsed = time.time() - t_start
        
        print(f"Successful: {is_sorted(sorted_tc)}")
        print(f"Time elapsed: {elapsed:5f} seconds\n")

    for test_case in gaussian_data:
        print_test_info(len(test_case), "gaussian")

        t_start = time.time()
        sorted_tc = bucket_sort(test_case)
        elapsed = time.time() - t_start
        
        print(f"Successful: {is_sorted(sorted_tc)}")
        print(f"Time elapsed: {elapsed:5f} seconds\n")


if __name__ == "__main__":
    bucket_sort_test()
