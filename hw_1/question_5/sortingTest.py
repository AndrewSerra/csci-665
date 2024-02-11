__author__="Andrew Serra"

from merge_sort_test import merge_sort_test
from insertion_sort_test import insertion_sort_test
from bucket_sort_test import bucket_sort_test

def run_tests():
    print("Merge Sort Test")
    merge_sort_test()

    print("Insertion Sort Test")
    insertion_sort_test()

    print("Bucket Sort Test")
    bucket_sort_test()

if __name__ == "__main__":
    run_tests()
