from typing import Optional


class Student:
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.age < other.age


def binary_search(lst, el) -> Optional[int]:
    if not list:
        return None

    def _search(left: int, right: int) -> Optional[int]:
        # Check whether the range is empty
        if left == right:
            # The range is empty: no indices in between left and right
            return None
        # Pick middle index
        middle = (left + right) // 2
        # Access its value
        middle_el = lst[middle]
        # See whether it's on the left branch
        if el < middle_el:
            return _search(left, middle)
        # See whether it's on the right branch
        if el > middle_el:
            return _search(middle + 1, right)
        # It's neither less nor greater: equal
        return middle

    return _search(0, len(lst))


assert binary_search([4, 7, 9], 5) is None
assert binary_search([4, 7, 9], 9) == 2
assert binary_search(['a', 'j', 'y'], 'b') is None
assert binary_search(['a', 'j', 'y'], 'a') == 0

assert binary_search([Student(4), Student(7), Student(9)], Student(9)) == 2
