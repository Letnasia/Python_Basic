import random
from typing import List


def bubble_sort(lst: list):
    # Do N bubble floats
    for n in range(len(lst)):
        # Float the bubble
        for i in range(1, len(lst) - n):
            #  check whether the left-side bubble must float up
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]


def bubble_sorted(lst: list) -> list:
    lst1 = [] + lst
    bubble_sort(lst1)
    return lst1


def is_sorted(lst: list) -> bool:
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True


def make_random_list(min_length: int, max_length: int = None) -> List[int]:
    if max_length is None:
        max_length = min_length
    length = random.randint(min_length, max_length)
    return [
        random.randint(-99999999, 99999999) for _ in range(length)
    ]


assert not is_sorted([7, 5, 9]), 'is_sorted 1'
assert is_sorted([7, 94, 654]), 'is_sorted 2'

for ff in range(1000):
    assert is_sorted(bubble_sorted(make_random_list(0, 99))), f'test {ff}'
