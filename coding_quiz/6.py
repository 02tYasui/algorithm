from typing import List


def get_max_sequence_sum(numbers: List[int], operator=max) -> int:
    result_sequence, sum_sequence = 0, 0
    for num in numbers:
        sum_sequence = operator(num, sum_sequence + num)
        result_sequence = operator(result_sequence, sum_sequence)

    return result_sequence


def find_max_circular_sequence_sum(numbers: List[int]) -> int:
    # [1,2,3,-1,3,2,1]
    max_sequence_sum = get_max_sequence_sum(numbers)
    # invert_numbers = []
    # all_sum = 0
    # for num in numbers:
    #     all_sum += num
    #     invert_numbers.append(-num)

    # max_wrap_sequence = all_sum - (-get_max_sequence_sum(invert_numbers))
    max_wrap_sequence = sum(numbers) - get_max_sequence_sum(numbers, operator=min)

    return max(max_sequence_sum, max_wrap_sequence)


if __name__ == "__main__":
    print(find_max_circular_sequence_sum([1, -2, 3, 6, -1, 2, 4, -5, 2]))
