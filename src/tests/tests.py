from simple_add_p import sum_of_squares


def test_make_table():
    numbers = list(range(11))
    # Timing the function
    result = sum_of_squares(numbers)
    assert result == 385
