from collections import Counter
from typing import List


def min_count_remove(x: List[int], y: List[int]) -> None:
    counter_x = Counter(x)
    counter_y = Counter(y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]


if __name__ == "__main__":
    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
    print("x = ", x)
    print("y = ", y)
    min_count_remove(x, y)
    print("x = ", x)
    print("y = ", y)
