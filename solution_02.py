from typing import TypeVar, List, Callable

T = TypeVar("T")  

def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Compares 2 elements using the comparator function and sorting manner
    param first: 1st element to compare
    param second: 2nd element to compare
    param comparator: function comparing 2 elements of type T
    param descending: indicates whether the comparison should be in descending order
    returns: true if the 1st element precedes the second according to the sorting order, else false
    """
    if descending:
        return comparator(second, first)
    else:
        return comparator(first, second)
    pass


def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts the elements of the list in-place in ascending/descending order using the selection sort algorithm
    param data: the list to be sorted
    param comparator: function to compare elements. by default, uses '<' operator to compare
    param descending: if true, sorts the list in descending order, else in ascending order
    returns: None
    """
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if do_comparison(data[j], data[min_index], comparator, descending):
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    pass


def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    Sorts the elements of the list in-place in ascending/descending order using the bubble sort algorithm
    param data: the list to be sorted
    param comparator: function to compare elements. by default, uses '<' operator to compare
    param descending: if true, sorts the list in descending order, else in ascending order
    returns: None
    """
    l = len(data)
    for i in range(l):
        for j in range(0, l - i - 1):
            if (comparator(data[j], data[j + 1]) and descending) or (
                    not comparator(data[j], data[j + 1]) and not descending):
                data[j], data[j + 1] = data[j + 1], data[j]


def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts the elements of the list in-place in ascending/descending order using the insertion sort algorithm
    param data: the list to be sorted
    param comparator: function to compare elements. by default, uses '<' operator to compare
    param descending: if true, sorts the list in descending order, else in ascending order
    returns: None
    """

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        if descending:
            while j >= 0 and comparator(data[j], key):
                data[j + 1] = data[j]
                j -= 1
        else:
            while j >= 0 and comparator(key, data[j]):
                data[j + 1] = data[j]
                j -= 1

        data[j + 1] = key


def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Sorts the list using a hybrid sort with merge sort and insertion sort
    param data: the list to be sorted
    param threshold: maximum size at whoch insertion sort will be used instead of merge sort
    param comparator: function to compare elements. by default, uses '<' operator to compare
    param descending: if true, sorts the list in descending order, else in ascending order
    returns: None
    """
    def merge(left: List[T], right: List[T]) -> List[T]:
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if do_comparison(left[i], right[j], comparator, descending):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    if len(data) <= 1:
        return

    if len(data) <= threshold:
        insertion_sort(data, comparator=comparator, descending=descending)
    else:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        hybrid_merge_sort(left, threshold=threshold, comparator=comparator, descending=descending)
        hybrid_merge_sort(right, threshold=threshold, comparator=comparator, descending=descending)
        merged = merge(left, right)

        data.clear()
        data.extend(merged)


def quicksort(data: List[T]) -> None:
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first: int, last: int) -> None:
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)


class Score:
    """
    Class that represents SAT scores
    NOTE: While it is possible to implement Python "magic methods" to prevent the need of a key function,
    this is not allowed for this application problems so students can learn how to create comparators of custom objects.
    Additionally, an individual section score can be outside the range [400, 800] and may not be a multiple of 10
    """

    __slots__ = ['english', 'math']

    def __init__(self, english: int, math: int) -> None:
        """
        Constructor for the Score class
        :param english: Score for the english portion of the exam
        :param math: Score for the math portion of the exam
        :return: None
        """
        self.english = english
        self.math = math

    def __repr__(self) -> str:
        """
        Represent the Score as a string
        :return: representation of the score
        """
        return str(self)

    def __str__(self) -> str:
        """
        Convert the Score to a string
        :return: string representation of the score
        """
        return f'<English: {self.english}, Math: {self.math}>'


def better_than_most(scores: List[Score], student_score: Score) -> str:
    """
    Determines if a student's SAT score (or part) is above the median of MSU student's SAT scores.
    param scores: list of Score objects representing the SAT score of every student.
    param student_score: Score object representing a student’s SAT score broken into two values: English and Math.
    returns: str: "Both"- if both scores are above median
                  "Math"- if math is above the median
                  "English"- if english is above median
                  "None" - if no score is above median
    """
    def compare_english(score1: Score, score2: Score) -> bool:
        return score1.english < score2.english

    def compare_math(score1: Score, score2: Score) -> bool:
        return score1.math < score2.math

    def find_median(sorted_scores: List[Score], subject: str) -> int:
        n = len(sorted_scores)
        if n % 2 == 1:
            return getattr(sorted_scores[n // 2], subject)
        else:
            return (getattr(sorted_scores[n // 2 - 1], subject) + getattr(sorted_scores[n // 2], subject)) // 2

    if not scores:
        return 'Both'

    english_scores = scores[:]
    hybrid_merge_sort(english_scores, comparator=compare_english)
    median_english = find_median(english_scores, 'english')

    math_scores = scores[:]
    hybrid_merge_sort(math_scores, comparator=compare_math)
    median_math = find_median(math_scores, 'math')

    result = []
    if student_score.english > median_english:
        result.append('English')
    if student_score.math > median_math:
        result.append('Math')

    if len(result) == 2:
        return 'Both'
    elif result:
        return result[0]
    else:
        return 'None'



