from simple_add_p import sum_of_squares_py


def test_sum_of_squares_py():
    numbers = list(range(11))
    # Timing the function
    result = sum_of_squares_py(numbers)
    assert result == 385
