import random

NUM_TEST_CASES = [100, 1000, 10000, 100000]

def _gen_uniform_test_case(n: int) -> list[float]:
    return [random.uniform(0, 1) for _ in range(n)]

def _gen_gaussian_test_case(n: int) -> list[float]:
    return [random.gauss(0.5, 0.001) for _ in range(n)]

def create_uniform_test_cases():
    test_cases = []

    for test_case_size in NUM_TEST_CASES:
        new_data = _gen_uniform_test_case(test_case_size)
        test_cases.append(new_data)
    
    return test_cases

def create_gaussian_test_cases():
    test_cases = []
    
    for test_case_size in NUM_TEST_CASES:
        new_data = _gen_gaussian_test_case(test_case_size)
        test_cases.append(new_data)
    
    return test_cases
